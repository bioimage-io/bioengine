# BioEngine API

Under the hood, BioEngine uses [Hypha](https://ha.amun.ai/) to orchestrate the services provided in the containers. We uses the `imjoy-rpc` client to communicate to the Hypha server for model execution.

We provide a free public server for the BioEngine available at https://ai.imjoy.io.

>[!IMPORTANT]
> This server is meant for testing and evaluation purposes.
> Please only use it to process small amounts of data to avoid overloading our server!

The following documentation uses `https://ai.imjoy.io` as the server_url - it can be changed to use to different server if desired.

If you are interested in setting up your own BioEngine server, please check our _preliminary repo_ for run BioEngine locally (tested on a Macbook pro): https://github.com/oeway/bioengine. 
>[!WARNING]
> The on-premise deployment is under development, it's not completely ready yet.


## Using BioEngine in Python

First install the `imjoy-rpc` library:

```bash
pip install imjoy-rpc
```

Use the following code to connect to the server and access the service. The code first connects to the server and then gets the service by its ID. The service can then be used like a normal Python object.

Similarily, you can also use the `connect_to_server_sync` function to connect to the server synchronously (available since `imjoy-rpc>=0.5.25.post0`).


<!-- tabs:start -->
#### Asynchronous Client

```python
import asyncio
import numpy as np
from imjoy_rpc.hypha import connect_to_server

async def main():
    server = await connect_to_server(
        {"name": "test client", "server_url": "https://ai.imjoy.io", "method_timeout": 3000}
    )
    triton = await server.get_service("triton-client")

    # Create a fake image
    image = np.random.randint(0, 255, (1, 3, 256, 256))

    # Run inference
    ret = await triton.execute(
        inputs=[{"inputs": [image], "model_id": "conscientious-seashell"}],
        model_name="bioengine-model-runner",
        serialization="imjoy",
    )
    result = ret["result"]


    mask = result['outputs'][0]
    return mask

if __name__ == "__main__":
    asyncio.run(main())
```

#### Synchronous Client

```python
import numpy as np
from imjoy_rpc.hypha.sync import connect_to_server

def main():
    server = connect_to_server(
        {"name": "test client", "server_url": "https://ai.imjoy.io", "method_timeout": 3000}
    )
    triton = server.get_service("triton-client")

    # Create a fake image
    image = np.random.randint(0, 255, (1, 3, 256, 256))

    # Run inference
    ret = triton.execute(
        inputs=[{"inputs": [image], "model_id": "conscientious-seashell"}],
        model_name="bioengine-model-runner",
        serialization="imjoy",
    )
    result = ret["result"]


    mask = result['outputs'][0]
    return mask

if __name__ == "__main__":
    main()
```

<!-- tabs:end -->

> [!NOTE]
> In Python, the recommended way to interact with the server to use asynchronous functions with `asyncio`. However, if you need to use synchronous functions,
> you can use `from imjoy_rpc.hypha.sync import login, connect_to_server` (available since `imjoy-rpc>=0.5.25.post0`) instead.
> The have the exact same arguments as the asynchronous versions. For more information, see [Synchronous Wrapper](/imjoy-rpc?id=synchronous-wrapper)

> <strong>💡 Tip </strong><br>
> For QT-based applications, e.g. napari, imswitch, use the synchronous api.

## Using the BioEingine in JavaScript

Include the following script in your HTML file to load the `imjoy-rpc` client:

```html
<script src="https://cdn.jsdelivr.net/npm/imjoy-rpc@0.5.6/dist/hypha-rpc-websocket.min.js"></script>
```

Use the following code in JavaScript to connect to the hypha server and access the bioenigne service via the `triton-client`:

```javascript
async function main(){
    const server = await hyphaWebsocketClient.connectToServer({"server_url": "https://ai.imjoy.io"})
    const svc = await server.getService("triton-client")
    // encode the image, similar to np.random.randint(0, 255, (1, 3, 256, 256))
    // see https://github.com/imjoy-team/imjoy-rpc/blob/master/imjoy-rpc-v2.md#data-type-representation
    image = {_rtype: "ndarray", _rvalue: new ArrayBuffer(1*3*256*256), _rshape: [1, 3, 256, 256], _rdtype: "uint8"}
    ret = await triton.execute({
        inputs: [{"inputs": [image], "model_id": "conscientious-seashell"}],
        model_name: "bioengine-model-runner",
        serialization: "imjoy",
        _rkwargs: true
    })
    result = ret["result"]
    mask = result['outputs'][0]
    console.log(mask)
}
```

## BioEngine Example Notebook

[![lite-badge]](https://jupyter.imjoy.io/lab/index.html?load=https://raw.githubusercontent.com/bioimage-io/BioEngine/main/notebooks/1-bioengine-engine-tutorial.ipynb&open=1)

[lite-badge]: https://jupyterlite.rtfd.io/en/latest/_static/badge.svg

## Issues

Please sumbit an [Github issue](https://github.com/bioimage-io/BioEngine/issues) if you experienced any issue with the BioEngine api access.

