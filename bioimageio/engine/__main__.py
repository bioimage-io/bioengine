import sys
import secrets
import asyncio
import subprocess
from hypha_launcher.api import HyphaLauncher
from hypha_launcher.utils.log import get_logger

import fire

logger = get_logger()

async def start_server(host = "0.0.0.0", port = 9000, public_base_url = ""):
    # get current file path so we can get the path of apps under the same directory
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    launcher = HyphaLauncher()
    minio_root_user = secrets.token_urlsafe(16)
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
        "--startup-functions=bioimageio.engine:register_bioengine_apps",
        "--enable-s3",
        f"--endpoint-url=http://localhost:{info['port']}",
        f"--access-key-id={minio_root_user}",
        f"--secret-access-key={minio_root_password}",
    ]
    subprocess.run(command)

def connect_server(server_url, login_required=False):
    from engine import connect_server
    server_url = server_url
    loop = asyncio.get_event_loop()
    loop.create_task(connect_server(server_url))
    loop.run_forever()


if __name__ == '__main__':
    fire.Fire({
        "start_server": start_server,
        "connect_server": connect_server
    })
