import logging
import sys, os
import asyncio
from hypha.utils import launch_external_services
from pathlib import Path


logger = logging.getLogger(__name__)

async def hypha_startup(server):
    file_path = Path(os.path.abspath(__file__)).parent / "run_imagej.py"
    server_url = server.config.local_base_url
    workspace = server.config.workspace
    token = await server.generate_token()
    service_id = "imagej"
    # TODO: download the conda env and unpack it
    # Then launch the code inside the conda env
    await launch_external_services(
        server,
       f"{sys.executable} {file_path} --server-url={server_url} --service-id={service_id} --workspace={workspace} --token={token}",
        name=service_id,
        check_services=[service_id],
        timeout=100,
    )
    logger.info("ImageJ service is ready.")

    
