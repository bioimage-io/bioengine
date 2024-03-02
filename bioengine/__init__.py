from bioengine.app_loader import load_apps
import logging

logger = logging.getLogger(__name__)

def connect_server(server_url):
    raise NotImplementedError("This function is not implemented yet.")

async def register_bioengine_apps(server):
    for app in load_apps():
        logger.info(f"Registering service {app.name}")
        await app.run(server)
        logger.info(f"Service {app.name} registered.")
