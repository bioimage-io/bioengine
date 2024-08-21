import asyncio
from bioimageio.engine.app_loader import load_apps
import logging
from functools import partial

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
        
async def list_apps(apps):
    return {app.id: app.name for app in apps.values()}

async def launch(server, apps, app_id, context=None):
    if app_id not in apps:
        raise ValueError(f"App with id {app_id} is not found.")
    app = apps[app_id]
    if app is None:
        raise ValueError(f"App with id {app_id} is not found.")
    return await app.run(server)

async def launch_all_apps(server, apps, continue_on_error=True, context=None):
    futures = []
    app_names = []
    for app in apps.values():
        app_names.append(app.name)
        logger.info(f"Registering service {app.name}")
        futures.append(run_app_with_error_logging(app, server, continue_on_error))

    results = await asyncio.gather(*futures)
    summary = {name: ("✅" if result is None else "❌") for name, result in zip(app_names, results)}
    
    for app_name, status in summary.items():
        print(f"{app_name}: {status}")
        
    return summary

async def register_bioengine_apps(server):
    apps = load_apps()
    logger.info("Starting the bioengine apps launcher service...")
    svc = await server.register_service(
        {
            "id": "bioengine-apps-launcher",
            "type": "bioengine-apps-launcher",
            "config": {"require_context": True, "visibility": "public"},
            "launch_all_apps": partial(launch_all_apps, server, apps),
            "launch": partial(launch, server, apps),
            "list": partial(list_apps, apps),
        }
    )
    logger.info(f"bioengine apps launcher service is registered as `{svc['id']}`")

async def launch_all_bioengine_apps(server):
    await register_bioengine_apps(server)
    apps = load_apps()
    logger.info("Starting all bioengine apps...")
    await launch_all_apps(server, apps, continue_on_error=True)
    logger.info("All bioengine apps are started.")

        