from hypha_rpc import api
import numpy as np

class CellposeModel:
    def __init__(self):
        from cellpose import core
        # Check if GPU is available
        self.use_GPU = core.use_gpu()
        print('>>> GPU activated? %d' % self.use_GPU)
        
        # Initialize model caching attributes
        self.cached_model_type = None
        self.model = None

    def _load_model(self, model_type):
        from cellpose import models
        if self.model is None or model_type != self.cached_model_type:
            print(f'Loading model: {model_type}')
            self.model = models.Cellpose(gpu=self.use_GPU, model_type=model_type)
            self.cached_model_type = model_type
        else:
            print(f'Reusing cached model: {model_type}')
        return self.model

    def predict(self, images: list[np.ndarray], channels=None, diameter=None, flow_threshold=None, model_type='cyto3'):
        """Run segmentation on the provided images using the specified model type."""
        # Load the model, utilizing caching
        model = self._load_model(model_type)

        if channels is None:
            # Default channels if not provided
            channels = [[2, 3]] * len(images)
        
        # Perform segmentation using the model
        masks, flows, styles, diams = model.eval(images, diameter=diameter, flow_threshold=flow_threshold, channels=channels)
        
        # Prepare the response with masks and diameters
        results = {
            'masks': [mask.tolist() for mask in masks],  # Converting numpy arrays to lists for JSON serialization
            'diameters': diams  # List of estimated diameters for each image
        }

        return results

    def train(self, images, labels, config):
        """Train the model using the provided images and labels."""
        # This method would handle the training process.
        # Currently, returning a placeholder response.
        raise NotImplementedError("Training functionality not implemented yet")

# Export the CellposeModel class using Hypha RPC API
api.export(CellposeModel)
