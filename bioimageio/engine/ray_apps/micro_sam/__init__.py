import io
from logging import getLogger
from typing import Union
from hypha_rpc import api
import numpy as np

class MicroSAM:
    def __init__(self, model_timeout: int = 3600, embedding_timeout: int = 600):
        from cachetools import TTLCache

        # Set up logger
        self.logger = getLogger(__name__)
        self.logger.setLevel("INFO")
        # Define model URLs
        self.model_urls = {
            "vit_b": "https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth",
            "vit_b_lm": "https://uk1s3.embassy.ebi.ac.uk/public-datasets/bioimage.io/diplomatic-bug/1/files/vit_b.pt",
            "vit_b_em_organelles": "https://uk1s3.embassy.ebi.ac.uk/public-datasets/bioimage.io/noisy-ox/1/files/vit_b.pt",
        }
        # Set up cache with per-item time-to-live
        self.models = TTLCache(
            maxsize=len(self.model_urls), ttl=model_timeout
        )  # TODO: what if multiple users download the same model?
        self.embeddings = TTLCache(maxsize=np.inf, ttl=embedding_timeout)

    def _load_model(self, model_name: str):
        import torch
        import requests
        from segment_anything import sam_model_registry
    
        if model_name not in self.model_urls:
            raise ValueError(
                f"Model {model_name} not found. Available models: {list(self.model_urls.keys())}"
            )
        # Check cache first
        if model_name in self.models:
            return self.models[model_name]

        # Download model if not in cache (takes approx. 4 seconds)
        model_url = self.model_urls[model_name]
        self.logger.info(f"Loading model {model_name} from {model_url}...")
        response = requests.get(model_url)
        if response.status_code != 200:
            raise RuntimeError(f"Failed to download model from {model_url}")
        buffer = io.BytesIO(response.content)

        # Load model state
        device = "cuda" if torch.cuda.is_available() else "cpu"
        ckpt = torch.load(buffer, map_location=device)
        model_type = model_name[:5]
        sam = sam_model_registry[model_type]()
        sam.load_state_dict(ckpt)

        # Cache the model
        self.logger.info(f"Caching model {model_name} (device={device})...")
        self.models[model_name] = sam

        return sam

    def _to_image(self, input_):
        
        # we require the input to be uint8
        if input_.dtype != np.dtype("uint8"):
            # first normalize the input to [0, 1]
            input_ = input_.astype("float32") - input_.min()
            input_ = input_ / input_.max()
            # then bring to [0, 255] and cast to uint8
            input_ = (input_ * 255).astype("uint8")
        if input_.ndim == 2:
            image = np.concatenate([input_[..., None]] * 3, axis=-1)
        elif input_.ndim == 3 and input_.shape[-1] == 3:
            image = input_
        else:
            raise ValueError(
                f"Invalid input image of shape {input_.shape}. Expect either 2D grayscale or 3D RGB image."
            )
        return image

    def compute_embedding(
        self, model_name: str, image: np.ndarray, context: dict = None
    ) -> bool:
        from segment_anything import SamPredictor

        user_id = context["user"].get("id")
        if not user_id:
            self.logger.info("User ID not found in context.")
            return False
        sam = self._load_model(model_name)
        self.logger.info(f"User {user_id} - computing embedding...")
        predictor = SamPredictor(sam)
        predictor.set_image(self._to_image(image))
        # Save computed predictor values
        self.logger.info(f"User {user_id} - caching embedding...")
        predictor_dict = {
            "model_name": model_name,
            "original_size": predictor.original_size,
            "input_size": predictor.input_size,
            "features": predictor.features,  # embedding
            "is_image_set": predictor.is_image_set,
        }
        self.embeddings[user_id] = predictor_dict
        return True

    def reset_embedding(self, context: dict = None) -> bool:
        user_id = context["user"].get("id")
        if user_id not in self.embeddings:
            self.logger.info(f"User {user_id} not found in cache.")
            return False
        else:
            self.logger.info(f"User {user_id} - resetting embedding...")
            del self.embeddings[user_id]
            return True

    def segment(
        self,
        point_coordinates: Union[list, np.ndarray],
        point_labels: Union[list, np.ndarray],
        context: dict = None,
    ) -> list:
        from kaibu_utils import mask_to_features
        from segment_anything import SamPredictor
        user_id = context["user"].get("id")
        if user_id not in self.embeddings:
            self.logger.info(f"User {user_id} not found in cache.")
            return []
        self.logger.info(
            f"User {user_id} - segmenting with model {self.embeddings[user_id]['model_name']}..."
        )
        # Load the model with the pre-computed embedding
        sam = self._load_model(self.embeddings[user_id]["model_name"])
        predictor = SamPredictor(sam)
        for key, value in self.embeddings[user_id].items():
            if key != "model_name":
                setattr(predictor, key, value)
        # Run the segmentation
        self.logger.debug(
            f"User {user_id} - point coordinates: {point_coordinates}, {point_labels}"
        )
        if isinstance(point_coordinates, list):
            point_coordinates = np.array(point_coordinates, dtype=np.float32)
        if isinstance(point_labels, list):
            point_labels = np.array(point_labels, dtype=np.float32)
        mask, scores, logits = predictor.predict(
            point_coords=point_coordinates[
                :, ::-1
            ],  # SAM has reversed XY conventions
            point_labels=point_labels,
            multimask_output=False,
        )
        self.logger.debug(f"User {user_id} - predicted mask of shape {mask.shape}")
        features = mask_to_features(mask[0])
        return features


api.export(MicroSAM)
