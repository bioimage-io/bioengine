import os
import numpy as np
import imageio
from interactive_cellpose import CellPoseInteractiveModel

this_dir = os.path.dirname(__file__)
image = imageio.imread(os.path.join(this_dir, "img02.png"))
labels = imageio.imread(os.path.join(this_dir, "img02_labels.png"))
model = CellPoseInteractiveModel(
    model_dir=os.path.join(this_dir, "__celpose_models__"),
    style_on=1,
    default_diameter=30,
    resume=False,
    pretrained_model=False,
)
flow = model.transform_labels(labels[:, :, None])
x = np.expand_dims(image, axis=0)
y = np.expand_dims(flow, axis=0)
print(f"Training one batch: {x.shape}, {y.shape}")
for i in range(100):
    loss = model.train_on_batch(x, y)
    print(f"Loss: {loss}")
