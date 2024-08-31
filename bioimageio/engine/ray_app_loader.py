"""Provide main entrypoint."""
import asyncio
import re
from ray import serve
import logging
import yaml
import os
import sys
from pathlib import Path
import urllib.request
from starlette.requests import Request

from hypha_rpc.utils import ObjectProxy



logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger("app_launcher")
logger.setLevel(logging.INFO)


def load_app(app_file, manifest):
    """Load app file."""
    if os.path.isfile(app_file):
        with open(app_file, "r", encoding="utf-8") as fil:
            content = fil.read()
    elif app_file.startswith("http"):
        with urllib.request.urlopen(app_file) as response:
            content = response.read().decode("utf-8")
        # remove query string
        app_file = app_file.split("?")[0]
    else:
        raise Exception(f"Invalid input app file path: {app_file}")

    if app_file.endswith(".py"):
        app_info = ObjectProxy.fromDict(manifest)
        import hypha_rpc
        def export(app_class):
            # make sure app_class is a class, not an instance
            if not isinstance(app_class, type):
                raise RuntimeError("exported object must be a class")
            app_info.app_class = app_class
        hypha_rpc.api = ObjectProxy(export=export)
        exec(content, globals())  # pylint: disable=exec-used
        logger.info(f"App loaded: {app_info.name}")
        # load manifest file if exists
        return app_info
    else:
        raise RuntimeError(f"Invalid script file type ({app_file})")


def load_all_apps(apps_dir: Path) -> dict:
    ray_apps = {}
    for sub_dir in apps_dir.iterdir():
        # check the subfolder for apps
        # there should be a file named "manifest.yaml" in the subfolder
        # if yes, load the app
        # by parsing the manifest.yaml file first,
        # find the entrypoint key with the file path
        # set it to app_file
        if sub_dir.is_dir():
            manifest_file = sub_dir / "manifest.yaml"
            if manifest_file.is_file():
                with open(manifest_file, "r") as f:
                    manifest = yaml.safe_load(f)
                
                # make sure the app_id is in lower case, no spaces, only underscores, letters, and numbers
                pattern = r"^[a-z0-9_]*$"
                assert re.match(pattern, manifest["id"]), "App ID must be in lower case, no spaces, only underscores, letters, and numbers"

                assert manifest["runtime"] == "ray", "Only ray apps are supported"
                app_file = sub_dir / manifest["entrypoint"]

                if app_file.is_file() and app_file.suffix == ".py":
                    app_info = load_app(str(app_file), manifest)
                    ray_serve_config = manifest.get("ray_serve_config", {"ray_actor_options": {"runtime_env": {}}})
                    assert "ray_actor_options" in ray_serve_config, "ray_actor_options must be provided in ray_serve_config"
                    assert "runtime_env" in ray_serve_config["ray_actor_options"], "runtime_env must be provided in ray_actor_options"
                    runtime_env = ray_serve_config["ray_actor_options"]["runtime_env"]
                    if not runtime_env.get("pip"):
                        runtime_env["pip"] = ["hypha-rpc", "https://github.com/bioimage-io/bioengine/archive/refs/heads/support-ray-apps.zip"]
                    else:
                        if "hypha-rpc" not in runtime_env["pip"]:
                            runtime_env["pip"].append("hypha-rpc")
                            runtime_env["pip"].append("https://github.com/bioimage-io/bioengine/archive/refs/heads/support-ray-apps.zip")
                    app_deployment = serve.deployment(name=app_info.id, **ray_serve_config)(app_info.app_class).bind()
                    manifest["app_bind"] = app_deployment
                    manifest["methods"] = [m for m in dir(app_info.app_class) if not m.startswith("_")]
                    ray_apps[app_info.id] = manifest
                    
    print("Loaded apps:", ray_apps.keys())

    assert len(ray_apps) > 0, "No apps loaded"
    return ray_apps

@serve.deployment(ray_actor_options={"runtime_env": {"pip": ["hypha-rpc"]}})
class HyphaRayAppManager:
    def __init__(self, server_url, workspace, token, ray_apps):
        from hypha_rpc.sync import connect_to_server
        self.server_url = server_url
        self._apps = ray_apps
        self._hypha_server = connect_to_server({"server_url": server_url, "token": token, "workspace": workspace})

        def create_service_function(name, app_bind, method_name):
            async def service_function(*args, **kwargs):
                method = getattr(app_bind, method_name)
                return await method.remote(*args, **kwargs)
            service_function.__name__ = name
            return service_function

        for app_id, app_info in self._apps.items():
            app_bind = app_info["app_bind"]
            methods = app_info["methods"]
            app_service = {
                "id": app_id,
                "name": app_info["name"],
                "description": app_info["description"],
                "config":{
                    "visibility": "protected"
                },
            }
            for method in methods:
                print(f"Registering method {method} for app {app_id}")
                app_service[method] = create_service_function(method, app_bind, method)
            info = self._hypha_server.register_service(app_service, {"overwrite":True})
            print(f"Added service {app_id} with id {info.id}, use it at {self.server_url}/{workspace}/services/{info.id.split('/')[1]}")
    
    async def __call__(self, request: Request):
        # return a json object with the services
        services = {}
        for app_id, app_info in self._apps.items():
            services[app_id] = app_info["methods"]
        return services
    


current_dir = Path(os.path.dirname(os.path.realpath(__file__)))
server_url = os.environ.get("HYPHA_SERVER_URL")
if not server_url:
    workspace = os.environ.get("HYPHA_WORKSPACE")
    token = os.environ.get("HYPHA_TOKEN")
    apps_dir = Path(os.environ.get("HYPHA_RAY_APPS_DIR", str(current_dir / "ray_apps")))

    # Getting config from environment
    ray_apps = load_all_apps(apps_dir)
    assert apps_dir.exists(), f"Apps directory does not exist: {apps_dir}"

    app = HyphaRayAppManager.bind(server_url, workspace, token, ray_apps)
else:
    logger.info("Ray app manager not started, no server url provided")

if __name__ == "__main__":
    serve.start()
    serve.run(app, name="bioengine-apps")
    import asyncio
    asyncio.get_event_loop().run_forever()
