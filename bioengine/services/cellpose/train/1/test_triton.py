import asyncio
from pyotritonclient import SequenceExcutor, execute
import numpy as np
import pickle
import imageio

# import urllib.request
# Download the file from `url` and save it locally under `file_name`:
# urllib.request.urlretrieve("https://github.com/imjoy-team/imjoy-interactive-segmentation/releases/download/v0.1.0/test_samples_4.pkl", "test_samples_4.pkl")
test_samples = pickle.load(open("test_samples_4.pkl", "rb"))
# urllib.request.urlretrieve("https://github.com/imjoy-team/imjoy-interactive-segmentation/releases/download/v0.1.0/train_samples_4.pkl", "train_samples_4.pkl")
train_samples = pickle.load(open("train_samples_4.pkl", "rb"))
print(len(train_samples), len(test_samples))


(image, labels, info) = train_samples[0]

model_id = 102

# set pretrained_model to None if you want to train from scratch
pretrained_model = "cyto"

# set model_token to a string if you want to protect the model
# from overwriting by other users
model_token = None
epochs = 10


async def train():
    seq = SequenceExcutor(
        server_url="https://ai.imjoy.io/triton",
        model_name="cellpose-train",
        decode_json=True,
        sequence_id=model_id,
    )
    for epoch in range(epochs):
        losses = []
        for (image, labels, info) in train_samples:
            inputs = [
                image.astype("float32"),
                labels.astype("uint16"),
                {
                    "steps": 64,
                    "pretrained_model": pretrained_model,
                    "resume": True,
                    "model_token": model_token,
                    "channels": [1, 2],
                    "diam_mean": 30,
                },
            ]
            result = await seq.step(inputs, select_outputs=["info"])
            losses.append(result["info"][0]["loss"])
        avg_loss = np.array(losses).mean()
        print(f"Epoch {epoch}  loss={avg_loss}")

    valid_image = test_samples[0][0].astype("float32")
    valid_labels = np.zeros_like(labels).astype("uint16")
    result = await seq.end(
        [
            valid_image,
            valid_labels,
            {
                "resume": True,
                "model_token": model_token,
                "channels": [1, 2],
                "diameter": 100.0,
                "model_format": "bioimageio",
            },
        ],
        decode_json=True,
        select_outputs=["model", "info"],
    )
    # Save the weights
    model_package = result["model"][0]
    filename = result["info"][0]["model_files"][0]
    with open(filename, "wb") as fil:
        fil.write(model_package)
    print(f"Model package saved to {filename}")


async def predict():
    # Start the prediction
    seq = SequenceExcutor(
        server_url="https://ai.imjoy.io/triton",
        model_name="cellpose-predict",
        decode_json=True,
        sequence_id=model_id,
    )
    for i, sample in enumerate(test_samples):
        inputs = [sample[0].astype("float32"), {"channels": [1, 2], "diameter": 100}]
        results = await seq.step(inputs, select_outputs=["mask"])
        imageio.imwrite(f"test_result_{i}.png", results["mask"].astype("uint8"))
        print(results["mask"].shape, results["mask"].mean())

    await seq.end()


loop = asyncio.get_event_loop()
loop.run_until_complete(train())
loop.run_until_complete(predict())
