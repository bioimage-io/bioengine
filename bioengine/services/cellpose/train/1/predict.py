import os
from interactive_cellpose import CellPoseInteractiveModel

import numpy as np
import pickle
import imageio

import urllib.request
# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve("https://github.com/imjoy-team/imjoy-interactive-segmentation/releases/download/v0.1.0/test_samples_4.pkl", "test_samples_4.pkl")
test_samples = pickle.load(open("test_samples_4.pkl", "rb"))
urllib.request.urlretrieve("https://github.com/imjoy-team/imjoy-interactive-segmentation/releases/download/v0.1.0/train_samples_4.pkl", "train_samples_4.pkl")
train_samples = pickle.load(open("train_samples_4.pkl", "rb"))
print(len(train_samples), len(test_samples))

model_root = "./"
diam_mean = 30

epochs = 1
resume = False
channels = [1, 2]
corrid = "103"

pretrained_model = "cyto" #os.path.join(model_root, str(corrid), "model.pth")
os.makedirs(os.path.join(model_root, str(corrid)), exist_ok=True)
model = CellPoseInteractiveModel(
            model_dir=model_root,
            diam_mean=diam_mean,
            style_on=1,
            resume=resume,
            pretrained_model=pretrained_model,
            default_save_path=os.path.join(model_root, str(corrid), "model.pth"),
        )

iterations = 0

for i, sample in enumerate(test_samples):
    imageio.imwrite(f"inputs.png", sample[0])
    inputs = sample[0].astype("float32")[None, :, :, :]
    results = model.predict(inputs, channels=[1, 2], diameter=100)
    results = results[0]
    imageio.imwrite(f"before-test_result_{i}.png", results[:, :, 0].astype("uint8"))

for epoch in range(epochs):
    losses = []
    for (image, labels, info) in train_samples:
        flow = model.transform_labels(labels)
        x = np.expand_dims(image, axis=0)
        y = np.expand_dims(flow, axis=0)
        losses = []
        for _ in range(10):
            # x and y will be augmented for each step
            loss = model.train_on_batch(x, y, channels=(1, 2))
            losses.append(loss)
            iterations += 1
            print(f"iteration: {iterations}, loss: {loss}")

model.save()

for i, sample in enumerate(test_samples):
    imageio.imwrite(f"inputs.png", sample[0])
    inputs = sample[0].astype("float32")[None, :, :, :]
    results = model.predict(inputs, channels=[1, 2], diameter=100)
    results = results[0]
    imageio.imwrite(f"after-test_result_{i}.png", results[:, :, 0].astype("uint8"))