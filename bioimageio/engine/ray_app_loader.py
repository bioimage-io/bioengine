"""Provide main entrypoint."""
import asyncio
import re
from ray import serve
from pathlib import Path

from bioimageio.engine.load_ray_apps import load_all_apps, HyphaRayAppManager
import os

# from hypha_rpc.sync import connect_to_server

current_dir = Path(os.path.dirname(os.path.realpath(__file__)))
ray_apps = load_all_apps(current_dir)

# Getting config from environment
server_url = os.environ.get("HYPHA_SERVER_URL")
workspace = os.environ.get("HYPHA_WORKSPACE")
token = os.environ.get("HYPHA_TOKEN")

assert server_url, "Server URL is not provided"

app = HyphaRayAppManager.bind(server_url, workspace, token, ray_apps)


if __name__ == "__main__":
    serve.start()
    serve.run(app, name="bioengine-apps")
    import asyncio
    asyncio.get_event_loop().run_forever()
