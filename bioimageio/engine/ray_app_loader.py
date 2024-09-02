"""Provide main entrypoint."""

import asyncio
from ray import serve
import logging
import os
import sys
from starlette.requests import Request
from bioimageio.engine.ray_app_manager import ray_apps

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger("ray_app_launcher")
logger.setLevel(logging.INFO)

@serve.deployment(
    ray_actor_options={
        "runtime_env": {
            "pip": ["hypha-rpc"],
        }
    }
)
class HyphaRayAppManager:
    def __init__(self, server_url, workspace, token, ray_apps):
        from hypha_rpc.sync import connect_to_server

        self.server_url = server_url
        self._apps = ray_apps
        assert server_url, "Server URL is required"
        self._hypha_server = connect_to_server(
            {"server_url": server_url, "token": token, "workspace": workspace}
        )

        def create_service_function(name, app_bind, method_name):
            async def service_function(*args, **kwargs):
                method = getattr(app_bind, method_name)
                return await method.remote(*args, **kwargs)

            service_function.__name__ = name
            return service_function

        for app_id, app_info in self._apps.items():
            ray_serve_config = self.create_ray_serve_config(app_info)
            app_bind = serve.deployment(
                name=app_info.id, **ray_serve_config
            )(app_info.app_class).bind()
            methods = app_info["methods"]
            app_service = {
                "id": app_id,
                "name": app_info["name"],
                "description": app_info["description"],
                "config": {"visibility": "protected"},
            }
            for method in methods:
                print(f"Registering method {method} for app {app_id}")
                app_service[method] = create_service_function(method, app_bind, method)
            info = self._hypha_server.register_service(app_service, {"overwrite": True})
            print(
                f"Added service {app_id} with id {info.id}, use it at {self.server_url}/{workspace}/services/{info.id.split('/')[1]}"
            )
    
    def create_ray_serve_config(self, manifest):
        ray_serve_config = manifest.get(
            "ray_serve_config", {"ray_actor_options": {"runtime_env": {}}}
        )
        assert (
            "ray_actor_options" in ray_serve_config
        ), "ray_actor_options must be provided in ray_serve_config"
        assert (
            "runtime_env" in ray_serve_config["ray_actor_options"]
        ), "runtime_env must be provided in ray_actor_options"
        runtime_env = ray_serve_config["ray_actor_options"]["runtime_env"]
        if not runtime_env.get("pip"):
            runtime_env["pip"] = ["hypha-rpc"]
        else:
            if "hypha-rpc" not in runtime_env["pip"]:
                runtime_env["pip"].append("hypha-rpc")
        runtime_env["pip"].append(
            "https://github.com/bioimage-io/bioengine/archive/refs/heads/support-ray-apps.zip"
        )
        return ray_serve_config

    async def __call__(self, request: Request):
        # return a json object with the services
        services = {}
        for app_id, app_info in self._apps.items():
            services[app_id] = app_info["methods"]
        return services

server_url = os.environ.get("HYPHA_SERVER_URL")
workspace = os.environ.get("HYPHA_WORKSPACE")
token = os.environ.get("HYPHA_TOKEN")
app = HyphaRayAppManager.bind(server_url, workspace, token, ray_apps)

if __name__ == "__main__":
    serve.start()
    serve.run(app, name="bioengine-apps")
    import asyncio

    asyncio.get_event_loop().run_forever()
