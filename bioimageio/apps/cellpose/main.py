from hypha_launcher.utils.container import ContainerEngine
from pathlib import Path
from pyotritonclient import get_config, execute
from functools import partial
import logging

logger = logging.getLogger(__name__)

container_engine = ContainerEngine()
TRITON_IMAGE = "docker://nvcr.io/nvidia/tritonserver:23.03-py3"


async def hypha_startup(server):
    # get current dir
    current_dir = Path(__file__).parent
    host_port = "9302"
    logger.info(f"Pulling triton image {TRITON_IMAGE}")
    container_engine.pull_image(TRITON_IMAGE)
    logger.info(f"Starting triton server at port {host_port}")
    container_engine.run_command(
        f'bash -c "tritonserver --model-repository=/models --log-verbose=3 --log-info=1 --log-warning=1 --log-error=1 --model-control-mode=poll --exit-on-error=false --repository-poll-secs=10 --allow-grpc=False --http-port={host_port}"',  # noqa
        TRITON_IMAGE,
        ports={host_port: host_port},
        volumes={str(current_dir): "/models"},
    )
    
    server_url = f"http://localhost:{host_port}"
    logger.info(f"Triton server is running at {server_url}")

    svc = await server.register_service({
        "name": "CellPose",
        "id": "cellpose",
        "config": {
            "visibility": "public"
        },
        "train": partial(execute, server_url=server_url, model_name="cellpose-train"),
        "train_config": partial(get_config, server_url=server_url, model_name="cellpose-train"),
        "predict": partial(execute, server_url=server_url, model_name="cellpose-predict"),
        "predict_config": partial(get_config, server_url=server_url, model_name="cellpose-predict"),
    })
    
    logger.info(f"CellPose service is registered as `{svc['id']}`")