import os
import io
import urllib.request
import torch
import json
import numpy as np
import imageio
from pathlib import Path
from cellpose import utils, models, transforms, dynamics
from cellpose.plot import mask_rgb
from bioimageio.core.build_spec import build_model


class CellPoseInteractiveModel:
    def __init__(
        self,
        model_dir=None,
        type="cellpose",
        resume=True,
        pretrained_model=None,
        save_freq=None,
        use_gpu=True,
        diam_mean=30.0,
        learning_rate=0.001,
        default_save_path=None,
        model_id=None,
        data_root=None,
        **kwargs,
    ):
        assert type == "cellpose"
        assert model_dir is not None
        device, gpu = models.assign_device(True, use_gpu)
        self.gpu = gpu
        self.learning_rate = learning_rate
        self.model_dir = model_dir
        self.default_save_path = default_save_path
        self.diam_mean = diam_mean

        assert self.default_save_path is not None
        self.data_root = data_root or os.path.join(
            os.path.dirname(self.default_save_path), "data"
        )
        self._config = {
            "diam_mean": self.diam_mean,
            "default_save_path": self.default_save_path,
        }
        self._history = []
        if save_freq is None:
            if gpu:
                self.save_freq = 2000
            else:
                self.save_freq = 300
        else:
            self.save_freq = save_freq

        if pretrained_model in ["cyto", "nuclei"]:
            model_type = pretrained_model
            load_default_pretrained_model = True
            pretrained_model = None
        else:
            load_default_pretrained_model = False
            model_type = "cyto"

        if pretrained_model:
            self._config["parent"] = os.path.basename(pretrained_model)

        self.model = models.CellposeModel(
            gpu=gpu,
            device=device,
            torch=True,
            pretrained_model=pretrained_model,
            diam_mean=self.diam_mean,
            concatenation=False,
            **kwargs,
        )
        os.makedirs(self.model_dir, exist_ok=True)
        if resume:
            if self.default_save_path is None:
                raise Exception("default_save_path is None")
            if os.path.exists(self.default_save_path):
                print("Resuming model from " + self.default_save_path)
                self.load(self.default_save_path)
                # disable pretrained model
                load_default_pretrained_model = False
            else:
                print("Skipping resume, snapshot does not exist")
        # load pretrained model weights if not specified
        if load_default_pretrained_model:
            cp_model_dir = Path.home().joinpath(".cellpose", "models")
            os.makedirs(cp_model_dir, exist_ok=True)
            weights_path = cp_model_dir / (model_type + "torch_0")
            if not weights_path.exists():
                urllib.request.urlretrieve(
                    f"https://www.cellpose.org/models/{model_type}torch_0",
                    str(weights_path),
                )
            if not (cp_model_dir / f"size_{model_type}torch_0.npy").exists():
                urllib.request.urlretrieve(
                    f"https://www.cellpose.org/models/size_{model_type}torch_0.npy",
                    str(cp_model_dir / f"size_{model_type}torch_0.npy"),
                )

            print("loading default pretrained cellpose model from " + str(weights_path))
            if gpu:
                self.model.net.load_state_dict(
                    torch.load(str(weights_path)), strict=False
                )
            else:
                self.model.net.load_state_dict(
                    torch.load(str(weights_path), map_location=torch.device("cpu")),
                    strict=False,
                )
        self._iterations = 0
        # Note: we are using Adam for adaptive learning rate which is different from the SDG used by cellpose
        # this support to make the training more robust to different settings
        self.model.optimizer = torch.optim.Adam(
            self.model.net.parameters(), lr=self.learning_rate, weight_decay=1e-5
        )
        self.model._set_criterion()
        # make sure we override the model_id
        self.set_config("model_id", model_id)

    def get_model_id(self):
        """get the model id"""
        return self._config.get("model_id")

    def set_config(self, key, value=None):
        """set the config"""
        if value is None and isinstance(key, dict):
            # assume key is a dictionary
            self._config.update(key)
        else:
            self._config[key] = value

    def get_config(self):
        """augment the images and labels
        Parameters
        --------------
        None

        Returns
        ------------------
        config: dict
            a dictionary contains the following keys:
            1) `batch_size` the batch size for training
        """
        return self._config

    def transform_labels(self, label_image):
        """transform the labels which will be used as training target
        Parameters
        --------------
        label_image: array [width, height, channel]
            a label image

        Returns
        ------------------
        array [width, height, channel]
            the transformed label image
        """
        assert label_image.ndim == 3 and label_image.shape[2] == 1
        label_image = label_image[:, :, 0]
        train_flows = dynamics.labels_to_flows(
            [label_image],
            files=None,
            use_gpu=self.model.gpu,
            device=self.model.device,
            skel=self.model.skel,
        )
        return train_flows[0].transpose(1, 2, 0)

    def augment(self, images, labels, channels=(1, 2)):
        """augment the images and labels
        Parameters
        --------------
        images: array [batch_size, width, height, channel]
            a batch of input images

        labels: array [batch_size, width, height, channel]
            a batch of labels

        Returns
        ------------------
        (images, labels) both are: array [batch_size, width, height, channel]
            augmented images and labels
        """
        images = [images[i].transpose(2, 0, 1) for i in range(images.shape[0])]
        labels = [labels[i].transpose(2, 0, 1) for i in range(labels.shape[0])]

        nimg = len(images)
        # check that arrays are correct size
        if nimg != len(labels):
            raise ValueError("train images and labels not same length")
        if labels[0].ndim < 2 or images[0].ndim < 2:
            raise ValueError(
                "training images or labels are not at least two-dimensional"
            )

        # make data correct shape and normalize it so that 0 and 1 are 1st and 99th percentile of data
        images, _, _ = transforms.reshape_and_normalize_data(
            images, test_data=None, channels=channels, normalize=True
        )

        # compute average cell diameter
        diam_train = np.array(
            [utils.diameters(labels[k][0])[0] for k in range(len(labels))]
        )
        diam_train[diam_train < 5] = 5.0
        scale_range = 0.5
        rsc = diam_train / self.model.diam_mean
        # TODO: control the random seed
        # now passing in the full train array, need the labels for distance field
        imgi, lbl, scale = transforms.random_rotate_and_resize(
            images,
            Y=labels,
            rescale=rsc,
            scale_range=scale_range,
            unet=self.model.unet,
            inds=np.arange(nimg),
            skel=self.model.skel,
        )
        return imgi, lbl

    def train(
        self,
        images,
        labels,
        channels=(1, 2),
    ):
        imgi, lbl = self.augment(images, labels, channels=channels)
        train_loss = self.model._train_step(imgi, lbl)
        self._iterations += len(images)
        if self._iterations % self.save_freq == 0:
            self.save()
        return train_loss

    def train_on_batch(self, X, y, channels=(1, 2)):
        """train the model for one iteration
        Parameters
        --------------
        X: array [batch_size, width, height, channel]
            the input image with 2 channels

        y: array [batch_size, width, height, channel]
            the mask (a.k.a label) image with one unique pixel value for one object
            if the shape is [1, width, height], then y is the label image
            otherwise, it should have channel=4 where the 1st channel is the label image
            and the other 3 channels are the precomputed flow image

        Returns
        ------------------
        loss value
        """
        assert X.shape[0] == y.shape[0] and X.ndim == 4

        return self.train(X, y, channels=channels)

    def predict(
        self,
        X,
        diameter=30.0,
        channels=(1, 2),
        return_styles=False,
        **kwargs,
    ):
        """predict the model for one input image
        Parameters
        --------------
        X: array [batch_size, width, height, channel]
            the input image with 2 channels

        Returns
        ------------------
        array [batch_size, width, height, channel]
            the predicted label image
        """
        assert X.ndim == 4
        X = [X[i].transpose(2, 0, 1) for i in range(X.shape[0])]
        masks, flows, styles = self.model.eval(
            X,
            channels=channels,
            diameter=diameter,
            net_avg=False,
            **kwargs,
        )
        # io.masks_flows_to_seg(image, masks, flows, diams, image_name, channels)
        # io.save_masks(path, masks, flows, image_name, png=True, tif=False)
        if return_styles:
            return (
                np.stack([np.expand_dims(mask, axis=2) for mask in masks], axis=0),
                styles,
            )
        else:
            return np.stack([np.expand_dims(mask, axis=2) for mask in masks], axis=0)

    def can_overwrite(self, token):
        """check if the model can be overwritten"""
        model_token = self._config.get("model_token")
        if not model_token or model_token == token:
            return True
        return False

    def get_weights(self):
        """Get model weights in bytes."""
        buf = io.BytesIO()
        self.model.net.save_model(buf)
        buf.seek(0)
        return buf.read()

    def save(self, file_path=None):
        """save the model
        Parameters
        --------------
        file_path: string
            the model file path

        Returns
        ------------------
        None
        """
        if file_path is None and self.default_save_path is not None:
            file_path = self.default_save_path
        assert isinstance(file_path, str)
        self.model.net.save_model(file_path)
        with open(os.path.join(os.path.dirname(file_path), "config.json"), "w") as fil:
            fil.write(json.dumps(self.get_config()))

        # append the history and clear it
        with open(os.path.join(os.path.dirname(file_path), "history.csv"), "a") as fil:
            # fil.write("image,labels,steps,seed\n")
            for history in self._history:
                fil.write(",".join(map(str, history)) + "\n")
        self._history = []

    def _save_data_array(self, data):
        buf = io.BytesIO()
        np.save(buf, data)
        hash_code = str(hash(buf))
        file_name = os.path.join(self.data_root, hash_code + ".npy")
        if not os.path.exists(file_name):
            with open(file_name, "wb") as fil:
                fil.write(buf.getbuffer())
        return hash_code

    def record_training_history(self, image, labels, steps, seed):
        image_hash = self._save_data_array(image)
        labels_hash = self._save_data_array(labels)
        self._history.append((image_hash, labels_hash, steps, seed))
        return {
            "image": image_hash,
            "labels": labels_hash,
            "steps": steps,
            "seed": seed,
        }

    def load(self, file_path):
        """load the model
        Parameters
        --------------
        file_path: string
            the model file path

        Returns
        ------------------
        None
        """
        with open(os.path.join(os.path.dirname(file_path), "config.json"), "r") as fil:
            self.set_config(json.loads(fil.read()))
        self.diam_mean = self._config.get("diam_mean", self.diam_mean)
        if self.gpu:
            self.model.net.load_state_dict(torch.load(file_path), strict=True)
        else:
            self.model.net.load_state_dict(
                torch.load(file_path, map_location=torch.device("cpu")),
                strict=True,
            )

    def export(
        self,
        format,
        output_path,
        test_image,
        test_mask,
        license="CC-BY-4.0",
        documentation=None,
        description=None,
        author_info=None,
    ):
        """export the model into different format
        Parameters
        --------------
        format: string
            the model format to be exported
        output_path: string
            the file path to the exported model

        Returns
        ------------------
        None
        """
        assert format == "bioimageio"
        root = os.path.dirname(output_path)
        name = f"CellPose-{self._config.get('model_id')}"
        assert test_image.ndim == 4 and test_mask.ndim == 4
        np.save(f"{root}/test_image.npy", test_image)
        np.save(f"{root}/test_mask.npy", test_mask)
        with open(f"{root}/README.md", "w") as fil:
            if documentation:
                fil.write(f"{documentation}\n")
            else:
                fil.write(f"# {name}\n")
                if description:
                    fil.write(f"{description}\n")
        test_image = test_image[0].astype("uint8")
        test_mask = mask_rgb(test_mask[0])
        print(test_image.shape, test_mask.shape)
        combined = np.concatenate([test_image, test_mask], axis=1)
        imageio.imwrite(f"{root}/cover.png", combined)
        build_model(
            self.default_save_path,
            weight_type="pytorch_state_dict",
            source=__file__ + ":CellPoseInteractiveModel",
            test_inputs=[f"{root}/test_image.npy"],
            test_outputs=[f"{root}/test_mask.npy"],
            output_path=output_path,
            name=name,
            description=description or "A CellPose model trained with the BioEngine.",
            authors=[author_info] if author_info else [],
            license=license or "CC-BY-4.0",
            documentation=f"{root}/README.md",
            covers=[f"{root}/cover.png"],
            tags=["cellpose", "segmentation"],
            cite={},
            parent=self._config.get("parent"),
            root=root,
            model_kwargs=None,
            preprocessing=None,
            postprocessing=None,
        )
        return open(output_path, "rb").read()
