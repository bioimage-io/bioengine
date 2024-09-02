"""Provide ray app loader."""

import asyncio
from ray import serve
import logging
import os
import sys
from starlette.requests import Request
from bioimageio.engine.ray_app_loader import ray_apps

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger("ray_app_launcher")
logger.setLevel(logging.INFO)


@serve.deployment(
    ray_actor_options={
        "runtime_env": {
            "pip": [
                "hypha-rpc",
                "https://github.com/bioimage-io/bioengine/archive/refs/heads/main.zip",
            ]
        }
    }
)
class HyphaRayAppManager:
    def __init__(self, server_url, workspace, token, ray_apps):
        from hypha_rpc.sync import connect_to_server

        self.server_url = server_url
        self._apps = ray_apps
        self._ongoing_requests = {}  # Track ongoing requests per app and method
        self._scale_down_flags = {}  # Flags to mark apps for scaling down

        assert server_url, "Server URL is required"
        self._hypha_server = connect_to_server(
            {"server_url": server_url, "token": token, "workspace": workspace}
        )

        def create_service_function(app_id, method_name, app_bind):
            key = f"{app_id}:{method_name}"
            self._ongoing_requests[key] = 0  # Initialize counter
            self._scale_down_flags[app_id] = False  # Initialize scale down flag

            async def service_function(*args, **kwargs):
                # Mark other apps to scale down if they are not the current app
                self.mark_apps_for_scaling_down(app_id)

                # Track the start of a request
                self._ongoing_requests[key] += 1
                logger.info(
                    f"Starting request for {key}, ongoing: {self._ongoing_requests[key]}"
                )

                try:
                    method = getattr(app_bind, method_name)
                    results = await method.remote(*args, **kwargs)
                    return results
                except Exception as e:
                    # Log the error and raise it
                    logger.error(f"Error in {key}: {str(e)}")
                    raise
                finally:
                    # Track the end of a request
                    self._ongoing_requests[key] -= 1
                    logger.info(
                        f"Completed request for {key}, ongoing: {self._ongoing_requests[key]}"
                    )

                    # If no ongoing requests and flag is set, scale down
                    if (
                        self._ongoing_requests[key] == 0
                        and self._scale_down_flags[app_id]
                    ):
                        self.scale_down_if_idle(app_id)

            service_function.__name__ = method_name
            return service_function

        for app_id, app_info in self._apps.items():
            app_bind = app_info["app_bind"]
            methods = app_info["methods"]
            app_service = {
                "id": app_id,
                "name": app_info["name"],
                "description": app_info["description"],
                "config": {"visibility": "public"},
            }
            if app_info.get("service_config"):
                svc_config = app_info["service_config"]
                app_service["config"].update(svc_config)

            for method in methods:
                logger.info(f"Registering method {method} for app {app_id}")
                app_service[method] = create_service_function(app_id, method, app_bind)
            info = self._hypha_server.register_service(app_service, {"overwrite": True})
            logger.info(
                f"Added service {app_id} with id {info.id}, use it at {self.server_url}/{workspace}/services/{info.id.split('/')[1]}"
            )

        apps = {}
        for app_id, app_info in self._apps.items():
            apps[app_id] = app_info["methods"]

        info = self._hypha_server.register_service(
            {
                "id": "ray-apps",
                "name": app_info["name"],
                "description": app_info["description"],
                "config": {"visibility": "public"},
                "apps": apps,
            },
            {"overwrite": True},
        )
        logger.info(f"Registered Ray Apps service with id {info.id}")

    def mark_apps_for_scaling_down(self, current_app_id):
        # Iterate through all apps to set scale down flags
        for app_id, app_info in self._apps.items():
            if app_id != current_app_id:  # Skip the current app
                for method_name in app_info["methods"]:
                    key = f"{app_id}:{method_name}"
                    if self._ongoing_requests.get(key, 0) > 0:
                        self._scale_down_flags[app_id] = True
                        logger.info(
                            f"Marked {app_id} for scaling down after completion"
                        )

    def scale_down_if_idle(self, app_id):
        pass
        # deployment_handle = serve.get_deployment_handle(app_id)
        # deployment_handle.options(num_replicas=0).deploy()
        # logger.info(f"Scaled down deployment {app_id} due to inactivity")

    async def __call__(self, request: Request):
        # Return a JSON object with the services
        services = {}
        for app_id, app_info in self._apps.items():
            services[app_id] = app_info["methods"]
        return services


# Environment variables for connecting to the Hypha server
server_url = os.environ.get("HYPHA_SERVER_URL")
workspace = os.environ.get("HYPHA_WORKSPACE")
token = os.environ.get("HYPHA_TOKEN")

# Bind the deployment
app = HyphaRayAppManager.bind(server_url, workspace, token, ray_apps)

if __name__ == "__main__":
    serve.start()
    serve.run(app)
    asyncio.get_event_loop().run_forever()
