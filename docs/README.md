# BioEngine

[Tutorial for I2K 2022](https://slides.imjoy.io/?slides=https://raw.githubusercontent.com/oeway/slides/master/2022/i2k-2022-bioengine-workshop.md)

## Getting started

```python
async def run_model(image):
    server = await connect_to_server(
        {"server_url": "https://hypha.bioimage.io/", "method_timeout": 3000}
    )
    triton = await server.get_service("triton-client")

    # Run inference
    ret = await triton.execute(
        inputs=[{"inputs": [image], "model_id": "conscientious-seashell"}],
        model_name="bioengine-model-runner",
        serialization="imjoy",
    )
    result = ret["result"]
    mask = result['outputs'][0]
    return mask
```

<!-- ImJoyPlugin: { "type": "web-python", "requirements": ["numpy", "imjoy-rpc"]} -->
```python
import numpy as np
from imjoy_rpc import api
from imjoy_rpc.hypha import connect_to_server

async def run_model(image):
    server = await connect_to_server(
        {"server_url": "https://hypha.bioimage.io/", "method_timeout": 3000}
    )
    triton = await server.get_service("triton-client")

    # Run inference
    ret = await triton.execute(
        inputs=[{"inputs": [image], "model_id": "conscientious-seashell"}],
        model_name="bioengine-model-runner",
        serialization="imjoy",
    )
    result = ret["result"]
    mask = result['outputs'][0]
    return mask

async def setup():
    image = np.random.randint(0, 255, (1, 3, 256, 256))
    mask = await run_model(image)
    await api.alert(str(mask.shape))

api.export({"setup": setup})
```
