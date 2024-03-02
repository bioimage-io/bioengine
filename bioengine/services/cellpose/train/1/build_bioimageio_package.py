import os
import numpy as np

# first new model: add thresholding of outputs as post-processing
# the convenience function `build_model` creates a biomageio model spec compatible package (=zipped folder)
from bioimageio.core.build_spec import build_model

# create a subfolder to store the files for the new model
model_root = "./new_model"
os.makedirs(model_root, exist_ok=True)

# create the expected output tensor (= outputs thresholded at 0.5)
threshold = 0.5
new_output = prediction > threshold
new_output_path = f"{model_root}/new_test_output.npy"
np.save(new_output_path, new_output)


postprocessing = []

# get the model architecture
# note that this is only necessary for pytorch state dict models
model_source = get_architecture_source(rdf_doi)

# we use the `parent` field to indicate that the new model is created based on
# the nucleus segmentation model we have obtained from bioimage.io
# this field is optional and only needs to be given for models that are created based on
# other models from bioimage.io
# the parent is specified via it's doi and the hash of the weight file
weight_file = model_resource.weights["pytorch_state_dict"].source
with open(weight_file, "rb") as f:
    weight_hash = hashlib.sha256(f.read()).hexdigest()
parent = (rdf_doi, weight_hash)

# the name of the new model and where to save the zipped model package
name = "new-model1"
zip_path = os.path.join(model_root, f"{name}.zip")

# `build_model` needs some additional information about the model, like citation information
# all this additional information is passed as plain python types and will be converted into the bioimageio representation internally
# for more informantion, check out the function signature
# https://github.com/bioimage-io/core-bioimage-io-python/blob/main/bioimageio/core/build_spec/build_model.py#L252
cite = {cite_entry.text: cite_entry.url for cite_entry in model_resource.cite}
new_model_raw = build_model(
    weight_file,
    test_inputs=model_resource.test_inputs,
    test_outputs=[new_output_path],
    output_path=zip_path,
    name=name,
    description="nucleus segmentation model with thresholding",
    authors=[{"name": "Jane Doe"}],
    license="CC-BY-4.0",
    documentation=model_resource.documentation,
    covers=[str(cover) for cover in model_resource.covers],
    tags=["nucleus-segmentation"],
    cite=cite,
    parent=parent,
    root=model_root,
    source=model_source,
    model_kwargs=model_resource.kwargs,
    preprocessing=preprocessing,
    postprocessing=postprocessing,
)
