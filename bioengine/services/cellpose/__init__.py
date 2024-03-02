
import tritonclient

async def hypha_startup(server):
    hypha_launcher = await server.get_service("hypha-launcher")
    triton_server = await hypha_launcher.launch(image="nvcr.io/nvidia/tritonserver:22.04-py3", command="tritonserver --model-repository=/models", name="triton", ports=[8000])
    
    async def train(**kwargs):
        return tritonclient.execute(**kwargs, server_url=triton_server.server_url)

    await server.register_service({
        "id": "cellpose",
        "name": "Cellpose",
        "description": "A service to run cellpose",
        "config":{
            "visibility": "public",
            "run_in_executor": True,
        },
        "train": train,
    })

print("Hypha startup script loaded")