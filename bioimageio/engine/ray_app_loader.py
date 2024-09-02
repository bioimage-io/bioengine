"""Provide ray app manager."""
import re
from ray import serve
import logging
import yaml
import os
import sys
from pathlib import Path
import urllib.request

from hypha_rpc.utils import ObjectProxy


logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger("ray_app_manager")
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
            # expose the app class to the current module
            globals()[app_class.__name__] = app_class

        hypha_rpc.api = ObjectProxy(export=export)
        exec(content, globals())
        logger.info(f"App loaded: {app_info.name}")
        # load manifest file if exists
        return app_info
    else:
        raise RuntimeError(f"Invalid script file type ({app_file})")

def create_ray_serve_config(app_info):
    ray_serve_config = app_info.get(
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
        "https://github.com/bioimage-io/bioengine/archive/refs/heads/main.zip"
    )
    return ray_serve_config

def load_all_apps() -> dict:
    current_dir = Path(os.path.dirname(os.path.realpath(__file__)))
    apps_dir = current_dir / "ray_apps"
    ray_apps = {}
    for sub_dir in apps_dir.iterdir():
        if sub_dir.is_dir():
            manifest_file = sub_dir / "manifest.yaml"
            if manifest_file.is_file():
                with open(manifest_file, "r") as f:
                    manifest = yaml.safe_load(f)

                # make sure the app_id is in lower case, no spaces, only underscores, letters, and numbers
                pattern = r"^[a-z0-9_]*$"
                assert re.match(
                    pattern, manifest["id"]
                ), "App ID must be in lower case, no spaces, only underscores, letters, and numbers"

                assert manifest["runtime"] == "ray", "Only ray apps are supported"
                app_file = sub_dir / manifest["entrypoint"]
    
                app_info = load_app(str(app_file), manifest)
                ray_serve_config = create_ray_serve_config(app_info)
                # runtime_env["env_vars"] = dict(os.environ)
                app_deployment = serve.deployment(
                    name=app_info.id, **ray_serve_config
                )(app_info.app_class).bind()
                app_info.app_bind = app_deployment
                app_info.methods = [
                    m for m in dir(app_info.app_class) if not m.startswith("_")
                ]
                ray_apps[app_info.id] = app_info

    print("Loaded apps:", ray_apps.keys())

    assert len(ray_apps) > 0, "No apps loaded"
    return ray_apps


ray_apps = load_all_apps()