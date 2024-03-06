<img src='https://raw.githubusercontent.com/bioimage-io/bioengine/main/docs/img/bioengine-logo-black-acc.svg' width='600'>

# BioEngine: Your AI Engine for Advanced BioImage Analysis

BioEngine revolutionizes bioimage analysis by harnessing the power of cutting-edge AI within a flexible, containerized environment. This Python package, built on the robust foundation of [hypha](https://github.com/amun-ai/hypha), is meticulously designed to facilitate the deployment and execution of sophisticated bioimage analysis models and workflows. It offers a seamless, user-friendly interface through HTTP API and RPC, simplifying the integration of AI technologies into bioimage analysis without the need for intricate setup or deep technical expertise.

Understanding the diverse needs of the bioimage community, BioEngine provides a public server available at [https://hypha.bioimage.io](https://hypha.bioimage.io). This server acts as a crucial support hub for the BioImage Model Zoo ([https://bioimage.io](https://bioimage.io)), enabling users to test run models directly or connect through community-developed tools. This initiative not only fosters collaboration but also amplifies the accessibility of advanced AI tools across the field.

Recognizing the paramount importance of data privacy and the need for scalable solutions, BioEngine is designed for versatility. It can be easily deployed across a range of environments—from personal laptops and lab workstations to high-performance computing (HPC) systems and Kubernetes clusters. This adaptability ensures that regardless of your setup, BioEngine can be integrated smoothly, eliminating data transmission concerns and enhancing scalability. To support this wide range of deployment scenarios, we offer specialized toolkits tailored to meet the specific requirements of each platform.

BioEngine stands as a beacon for developers and researchers alike, providing an accessible gateway to the forefront of AI-powered bioimage analysis. By simplifying complex processes and fostering an environment of innovation, BioEngine is not just a tool but a partner in advancing the boundaries of bioimage research.

## Installation

```bash
pip install bioimageio.engine
```

## Using the BioEngine

You can access the BioEngine directly from the [BioImage.IO website](https://bioimage.io), for most of the models, you will find a test run button to execute it with your own images.



To use the BioEngine, you can try it with:
 - [bioengine-web-client](https://bioimage-io.github.io/bioengine-web-client/): A simple web app which allows you to run models from the BioImage Model Zoo.
 - [BioImage Model Zoo](https://bioimage.io): A repository of models for bioimage analysis, click any model and scroll down to the section about "Test this model".
 

## Development

BioEngine is an engine running behind the scenes, developers can interact with it python, javascript code or any other language that supports HTTP. Please take a look at our [API document](api.md).


Here is a simple example of how to use BioEngine in Python:

```python
import imageio
import asyncio
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

# Load your image
image = imageio.imread("https://samples.fiji.sc/new-lenna.jpg")
asyncio.run(run_model(image))
```

## Tutorial

To get started with BioEngine, please see our [tutorial for I2K 2023](https://slides.imjoy.io/?slides=https://raw.githubusercontent.com/bioimage-io/BioEngine/main/slides/i2k-2023-bioengine-workshop.md).

Please read the documentation at: https://bioimage-io.github.io/bioengine/

## TODO

+ Runtime types support via hypha-launcher:
   * [ ] HPC: Slurm / PBS / LFS ...
   * [ ] Conda environment
   * [ ] Docker / Apptainer / podman ...
   * [ ] Web Browser
   * [ ] pytriton(python package)
   * [ ] SSH + X(other runtime types)
   * [ ] K8S
