"""Provide main entrypoint."""
import asyncio
from ray import serve
import logging
import os
import sys
from pathlib import Path
import urllib.request
from starlette.requests import Request
from starlette.responses import HTMLResponse

from hypha_rpc.utils import ObjectProxy
from hypha_rpc.sync import connect_to_server

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger("app_launcher")
logger.setLevel(logging.INFO)


def load_app(plugin_file):
    """Load app file."""
    if os.path.isfile(plugin_file):
        with open(plugin_file, "r", encoding="utf-8") as fil:
            content = fil.read()
    elif plugin_file.startswith("http"):
        with urllib.request.urlopen(plugin_file) as response:
            content = response.read().decode("utf-8")
        # remove query string
        plugin_file = plugin_file.split("?")[0]
    else:
        raise Exception(f"Invalid input app file path: {plugin_file}")

    if plugin_file.endswith(".py"):
        app_config = ObjectProxy()
        import hypha_rpc
        def export(app_class, config=None):
            app_config.update(config or {})
            app_config.app_class = app_class
        hypha_rpc.api = ObjectProxy(export=export)
        exec(content, globals())  # pylint: disable=exec-used
        logger.info("Plugin executed")
        return app_config
    else:
        raise RuntimeError(f"Invalid script file type ({plugin_file})")

@serve.deployment
class HyphaApp:
    def __init__(self, server_url, workspace, token, services):
        self.server_url = server_url
        self._services = services
        self._hypha_server = connect_to_server({"server_url": server_url, "token": token, "workspace": workspace})
        svc = {
            "name": "Ray Functions",
            "id": "ray-functions",
            "config": {
                "visibility": "protected"
            },
        }

        def create_service_function(name, service_handle):
            async def service_function(*args, **kwargs):
                return await service_handle.translate.remote(*args, **kwargs)
            service_function.__name__ = name
            return service_function

        for service_name, service_bind in self._services.items():
            svc[service_name] = create_service_function(service_name, service_bind)

        info = self._hypha_server.register_service(svc, {"overwrite":True})
        print("Hypha service info:", info)
        self.info = info
    
    async def __call__(self, request: Request):
        redirect_url = f"{self.server_url}/{self.info.config.workspace}/services/{self.info.id.split('/')[1]}/translator?text=hello"
        return HTMLResponse(
            """
            <html>
                <head>
                    <meta http-equiv="refresh" content="2; URL='{}'" />
                </head>
                <body>
                    <p>Redirecting to Hypha...</p>
                    <h1>Services:</h1>
                    <ul>
                        {}
                    </ul>
                </body>
            </html>
            """.format(redirect_url, "\n".join([f"<li>{name}</li>" for name in self._services.keys()]))
        )
    

current_dir = Path(os.path.dirname(os.path.realpath(__file__)))

ray_apps = {}
apps_dir = current_dir / "ray_apps"
for app_file in apps_dir.iterdir():
    if app_file.is_file() and app_file.suffix == ".py" and app_file.stem != "__init__":
        load_app(str(app_file))
        app_info = load_app(str(app_file))
        app_deployment = serve.deployment(name=app_info.name)(app_info.app_class).bind()
        ray_apps[app_info.name] = app_deployment

# Getting config from environment
server_url = os.environ.get("HYPHA_SERVER_URL")
workspace = os.environ.get("HYPHA_WORKSPACE")
token = os.environ.get("HYPHA_TOKEN")

assert server_url, "Server URL is not provided"

app = HyphaApp.bind(server_url, workspace, token, ray_apps)

if __name__ == "__main__":
    serve.start()
    serve.run(app, name="hypha-apps")
    import asyncio
    asyncio.get_event_loop().run_forever()
