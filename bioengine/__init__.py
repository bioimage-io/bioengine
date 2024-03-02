import asyncio
from bioengine.app_loader import load_apps
import logging

logger = logging.getLogger(__name__)

def connect_server(server_url):
    raise NotImplementedError("This function is not implemented yet.")

async def run_app_with_error_logging(app, server, continue_on_error):
    try:
        return await app.run(server)
    except Exception as e:
        logger.error(f"Error running service {app.name}: {str(e)}")
        if not continue_on_error:
            raise
        else:
            return e

async def register_bioengine_apps(server, continue_on_error=False):
    futures = []
    app_names = []
    for app in load_apps():
        app_names.append(app.name)
        logger.info(f"Registering service {app.name}")
        futures.append(run_app_with_error_logging(app, server, continue_on_error))

    results = await asyncio.gather(*futures)
    summary = {name: ("✔️" if result is not None else "❌") for name, result in zip(app_names, results)}
    
    for app_name, status in summary.items():
        print(f"{app_name}: {status}")
