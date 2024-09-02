import os
import sys
import secrets
import asyncio
import subprocess
import ray
from hypha_rpc import connect_to_server
from hypha_launcher.api import HyphaLauncher
from hypha_launcher.utils.log import get_logger
import fire

logger = get_logger()

async def start_server(host = "0.0.0.0", port = 9000, public_base_url = "", launch_all_apps = False):
    # get current file path so we can get the path of apps under the same directory
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    launcher = HyphaLauncher()
    minio_root_user = "minio_root_user"
    minio_root_password = secrets.token_urlsafe(16)
    info = await launcher.launch_s3_server(minio_root_user, minio_root_password)
    logger.info("S3 server launched at: %s", info["port"])
    print(info)
    command = [
        sys.executable,
        "-m",
        "hypha.server",
        f"--host={host}",
        f"--port={port}",
        f"--public-base-url={public_base_url}",
        "--startup-functions=bioimageio.engine:" + ("launch_all_bioengine_apps" if launch_all_apps else "register_bioengine_apps"),
        "--enable-s3",
        f"--endpoint-url=http://localhost:{info['port']}",
        f"--access-key-id={minio_root_user}",
        f"--secret-access-key={minio_root_password}",
    ]
    subprocess.run(command)

def connect_server(server_url, login_required=False):
    from engine import connect_server
    loop = asyncio.get_event_loop()
    loop.create_task(connect_server(server_url))
    loop.run_forever()

async def _run_ray_server_apps(address, ready_timeout):
    if not address:
        address = os.environ.get("RAY_ADDRESS")
    with ray.init(address=address) as client_context:
        dashboard_url = f"http://{client_context.dashboard_url}"
        logger.info(f"Dashboard URL: {dashboard_url}")
    server_url = os.environ.get("HYPHA_SERVER_URL")
    workspace = os.environ.get("HYPHA_WORKSPACE")
    token = os.environ.get("HYPHA_TOKEN")
    assert server_url, "HYPHA_SERVER_URL environment variable is not set"
    health_check_url = f"{server_url}/{workspace}/services/ray-apps"
    logger.info(f"Health check URL: {health_check_url}")
    shutdown_command = "serve shutdown -y" + (f" --address={dashboard_url}")
    server = await connect_to_server({"server_url": server_url, "token": token, "workspace": workspace})
    serve_command = f"serve run bioimageio.engine.ray_app_manager:app" + (f" --address={address}" if address else "")

    proc = None
    from simpervisor import SupervisedProcess
    import httpx
    
    async def ready_function(_):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(health_check_url)
                return response.status_code == 200
        except Exception as e:
            logger.warning(f"Error checking readiness: {str(e)}")
            return False
    
    async def serve_apps():
        nonlocal proc
        if proc:
            if await proc.ready():
                return f"Ray Apps Manager already started at {server_url}/{workspace}/services/{svc.id.split('/')[1]}"
        if proc:
            await proc.kill()
        command = [c.strip() for c in serve_command.split() if c.strip()]
        name = "ray-apps-manager"
        proc = SupervisedProcess(
            name,
            *command,
            env=os.environ.copy(),
            always_restart=False,
            ready_func=ready_function,
            ready_timeout=ready_timeout,
            log=logger,
        )

        try:
            await proc.start()

            is_ready = await proc.ready()

            if not is_ready and proc and proc.running:
                await proc.kill()
                raise Exception(f"External services ({name}) failed to start")
        except:
            if logger:
                logger.exception(f"External services ({name}) failed to start")
            raise
        return f"Ray Apps Manager started at {server_url}/{workspace}/services/{svc.id.split('/')[1]}"
    
    async def shutdown():
        nonlocal proc
        if proc:
            if proc.running:
                await proc.kill()
            proc = None
        else:
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, os.system, shutdown_command)  

    svc = await server.register_service({
        "name": "Ray App Manager",
        "id": "ray-app-manager",
        "config": {
            "visibility": "public",
            "run_in_executor": True,
        },
        "serve": serve_apps,
        "shutdown": shutdown
    })
    
    # Start apps serve    
    await serve_apps()

def serve_ray_apps(address: str=None, ready_timeout: int=120):
    loop = asyncio.get_event_loop()
    loop.create_task(_run_ray_server_apps(address, ready_timeout))
    loop.run_forever()

if __name__ == '__main__':
    fire.Fire({
        "start_server": start_server,
        "connect_server": connect_server,
        "serve_ray_apps": serve_ray_apps,
    })
