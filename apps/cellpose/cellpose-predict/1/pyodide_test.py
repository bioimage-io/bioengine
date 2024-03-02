import micropip

await micropip.install("pyotritonclient")

import io
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from js import fetch
from pyotritonclient import get_config, execute_model


async def fetch_image(url, name=None, grayscale=False, size=None):
    response = await fetch(url)
    bytes = await response.arrayBuffer()
    bytes = bytes.to_py()
    buffer = io.BytesIO(bytes)
    buffer.name = name or url.split("?")[0].split("/")[1]
    image = Image.open(buffer)
    if grayscale:
        image = image.convert("L")
    if size:
        image = image.resize(size=size)
    image = np.array(image)
    return image


# obtain the model config
config = await get_config("https://triton.imjoy.io", "cellpose-python")

image = await fetch_image("https://static.imjoy.io/img/img02.png")
image = image.astype("float32")

# Paramerters for model.eval(), see here for more details: https://github.com/MouseLand/cellpose/blob/6fddd4da98219195a2d71041fb0e47cc69a4b3a6/cellpose/models.py#L101-L174
param = {"diameter": 30, "model_type": "cyto"}

# run inference
results = await execute_model(
    [image.transpose(2, 0, 1), param], config=config, decode_bytes=True
)
mask = results["mask"]

# display the output
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(image.astype("uint8"))
ax1.set_title("input image")
ax2.imshow(mask[0])
ax2.set_title("predicted mask")
plt.show()
