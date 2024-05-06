# Copyright (c) 2020, NVIDIA CORPORATION. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# patch for fix "urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]" error
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import json
import os
import random
import torch
import numpy as np

# triton_python_backend_utils is available in every Triton Python model. You
# need to use this module to create inference requests and responses. It also
# contains some utility functions for extracting information from model_config
# and converting Triton input/output types to numpy types.
import triton_python_backend_utils as pb_utils
from interactive_cellpose import CellPoseInteractiveModel


class TritonPythonModel:
    """Your Python model must use the same class name. Every Python model
    that is created must have "TritonPythonModel" as the class name.
    """

    def initialize(self, args):
        """`initialize` is called only once when the model is being loaded.
        Implementing `initialize` function is optional. This function allows
        the model to intialize any state associated with this model.

        Parameters
        ----------
        args : dict
          Both keys and values are strings. The dictionary keys and values are:
          * model_config: A JSON string containing the model configuration
          * model_instance_kind: A string containing model instance kind
          * model_instance_device_id: A string containing model instance device ID
          * model_repository: Model repository path
          * model_version: Model version
          * model_name: Model name
        """
        self.gpu_mode = args["model_instance_kind"] == "GPU"
        self.model = None
        self.iterations = 0
        model_snapshots_directory = os.environ.get("MODEL_SNAPSHOTS_DIRECTORY")
        if model_snapshots_directory:
            assert os.path.exists(
                model_snapshots_directory
            ), f'Model snapshots directory "{model_snapshots_directory}" (from env virable MODEL_SNAPSHOTS_DIRECTORY) does not exist'
            self.model_root = os.path.join(model_snapshots_directory, "cellpose-models")
        else:
            self.model_root = os.path.join(
                os.path.dirname(__file__), "../../../cellpose-models"
            )
        os.makedirs(self.model_root, exist_ok=True)
        self.data_root = os.path.join(os.path.dirname(self.model_root), "data")
        os.makedirs(self.data_root, exist_ok=True)

        # You must parse model_config. JSON string is not parsed here
        model_config = json.loads(args["model_config"])

        # Get info configuration
        output0_config = pb_utils.get_output_config_by_name(model_config, "info")

        # Convert Triton types to numpy types
        self.output0_dtype = pb_utils.triton_string_to_numpy(
            output0_config["data_type"]
        )

    def initialize_model(
        self,
        corrid,
        default_save_path,
        pretrained_model=None,
        diam_mean=30.0,
        resume=False,
        data_root=None,
        seed=0,
    ):
        """`initialize_model` is called when the model is being loaded. Implementing
        `initialize_model` function is optional. This function allows the model to
        load any state associated with this model.
        if pretrained_model is set to 'cyto' or 'nuclei', then the default cellpose model will be loaded
        """
        print(f"Initializing CellPoseInteractiveModel {corrid}...")
        os.makedirs(os.path.join(self.model_root, str(corrid)), exist_ok=True)
        if pretrained_model and pretrained_model not in ["cyto", "nuclei"]:
            pretrained_model = os.path.join(
                self.model_root, str(pretrained_model), "model.pth"
            )
        random.seed(seed)
        np_seed = random.randint(0, 4294967295)
        np.random.seed(np_seed)
        self.iterations = 0
        # Instantiate the PyTorch model
        self.model = CellPoseInteractiveModel(
            model_dir=self.model_root,
            model_id=corrid,
            diam_mean=diam_mean,
            resume=resume,
            pretrained_model=pretrained_model,
            default_save_path=default_save_path,
            data_root=data_root,
        )
        self.model.save()
        print(f"CellPoseInteractiveModel successfully initialized {corrid}.")

    def execute(self, requests):
        """`execute` must be implemented in every Python model. `execute`
        function receives a list of pb_utils.InferenceRequest as the only
        argument. This function is called when an inference is requested
        for this model. Depending on the batching configuration (e.g. Dynamic
        Batching) used, `requests` may contain multiple requests. Every
        Python model, must create one pb_utils.InferenceResponse for every
        pb_utils.InferenceRequest in `requests`. If there is an error, you can
        set the error argument when creating a pb_utils.InferenceResponse.

        Parameters
        ----------
        requests : list
          A list of pb_utils.InferenceRequest

        Returns
        -------
        list
          A list of pb_utils.InferenceResponse. The length of this list must
          be the same as `requests`
        """
        responses = []
        # Every Python backend must iterate over everyone of the requests
        # and create a pb_utils.InferenceResponse for each of them.
        for request in requests:
            corrid = request.correlation_id()
            start_flag = pb_utils.get_input_tensor_by_name(request, "START").as_numpy()[
                0
            ]
            end_flag = pb_utils.get_input_tensor_by_name(request, "END").as_numpy()[0]
            param = pb_utils.get_input_tensor_by_name(request, "param")
            param = param.as_numpy().astype(np.bytes_)[0]  # assume it's a scalar
            param = str(np.char.decode(param, "UTF-8"))
            param = json.loads(param)
            default_save_path = os.path.join(self.model_root, str(corrid), "model.pth")

            # Get input image
            image = pb_utils.get_input_tensor_by_name(request, "image").as_numpy()
            if len(image.shape) != 3 or image.shape[2] != 3:
                responses.append(
                    pb_utils.InferenceResponse(
                        output_tensors=[],
                        error=pb_utils.TritonError(
                            f"Unexpected image shape: {image.shape} vs (H, W, 3)"
                        ),
                    )
                )
                continue

            # Get labels image
            labels = pb_utils.get_input_tensor_by_name(request, "labels").as_numpy()
            if len(labels.shape) != 3 or labels.shape[2] != 1:
                responses.append(
                    pb_utils.InferenceResponse(
                        output_tensors=[],
                        error=pb_utils.TritonError(
                            f"Unexpected labels shape: {labels.shape} vs (H, W, 1)"
                        ),
                    )
                )
                continue

            steps = param.get("steps", 1)
            steps = min(steps, 128)

            pretrained_model = param.get("pretrained_model")
            resume = param.get("resume")
            if resume is None and os.path.exists(default_save_path):
                responses.append(
                    pb_utils.InferenceResponse(
                        output_tensors=[],
                        error=pb_utils.TritonError(
                            f"Model file already exists, please set `resume` to True or False explicitly in the `param`"
                        ),
                    )
                )
                continue

            if not self.model or self.model.get_model_id() != corrid or start_flag:
                if self.model:
                    self.model.save()
                self.initialize_model(
                    corrid,
                    default_save_path=default_save_path,
                    pretrained_model=pretrained_model,
                    diam_mean=param.get("diam_mean", 30.0),
                    resume=resume,
                    data_root=self.data_root,
                    seed=param.get("seed", 0),
                )

            if self.model and not self.model.can_overwrite(
                param.get("previous_model_token", param.get("model_token"))
            ):
                responses.append(
                    pb_utils.InferenceResponse(
                        output_tensors=[],
                        error=pb_utils.TritonError(
                            f"A protected model with the samed sequence_id ({corrid}) already"
                            " exists, please provide a valid model_token or previous_model_token to overwrite the model or use a different sequence_id."
                        ),
                    )
                )
                continue

            # Skip training if end_flag is set
            if start_flag or not end_flag:
                flow = self.model.transform_labels(labels)
                x = np.expand_dims(image, axis=0)
                y = np.expand_dims(flow, axis=0)
                losses = []
                seed = random.randint(0, 4294967295)
                np.random.seed(seed)
                for _ in range(steps):
                    # x and y will be augmented for each step
                    loss = self.model.train_on_batch(
                        x, y, channels=param.get("channels", (1, 2))
                    )
                    losses.append(loss)
                    self.iterations += 1
                    print(f"iteration: {self.iterations}, loss: {loss}")
                history_record = self.model.record_training_history(
                    image, labels, steps, seed
                )
                avg_loss = np.array(losses).mean()
                print(f"iterations:{self.iterations}, Loss: {avg_loss}")

                # Create output tensors. You need pb_utils.Tensor
                # objects to create pb_utils.InferenceResponse.
                info = {
                    "loss": avg_loss,
                    "iterations": self.iterations,
                    "history_record": history_record,
                }
            if end_flag:
                info = {"model_files": []}
                model_files = []
                if param.get("model_format") == "bioimageio":
                    test_image = np.expand_dims(image, axis=0)
                    test_mask = self.model.predict(
                        test_image,
                        channels=param.get("channels", (1, 2)),
                        diameter=param.get("diameter", 30.0),
                    )
                    output_path = os.path.join(
                        os.path.dirname(default_save_path), "model-bioimageio.zip"
                    )
                    package = self.model.export(
                        "bioimageio",
                        output_path,
                        test_image,
                        test_mask,
                        license=param.get("license"),
                        description=param.get("description"),
                        author_info=param.get("author_info"),
                        documentation=param.get("documentation"),
                    )
                    print(f"CellPose model exported to {output_path}")
                    model_files.append(package)
                    info["model_files"].append(
                        f"cellpose-bioimageio-{self.model.get_model_id()}.zip"
                    )
                else:
                    model_files.append(self.model.get_weights())
                    info["model_files"].append(
                        f"cellpose-{self.model.get_model_id()}.pth"
                    )
                bytes_data = str.encode(json.dumps(info), "utf-8")
                np_bytes_data = np.array([bytes_data], dtype=np.object_)
                out_tensor_0 = pb_utils.Tensor("info", np_bytes_data)
                np_bytes_data = np.array(model_files, dtype=np.object_)
                out_tensor_1 = pb_utils.Tensor("model", np_bytes_data)
                inference_response = pb_utils.InferenceResponse(
                    output_tensors=[out_tensor_0, out_tensor_1]
                )
                # Save to the model snapshots folder
                self.model.save()
                print(f"Model ({corrid}) saved.")
                self.model = None
            else:
                bytes_data = str.encode(json.dumps(info), "utf-8")
                np_bytes_data = np.array([bytes_data], dtype=np.object_)
                out_tensor_0 = pb_utils.Tensor("info", np_bytes_data)
                inference_response = pb_utils.InferenceResponse(
                    output_tensors=[out_tensor_0]
                )
            responses.append(inference_response)

        # You should return a list of pb_utils.InferenceResponse. Length
        # of this list must match the length of `requests` list.
        return responses

    def finalize(self):
        """`finalize` is called only once when the model is being unloaded.
        Implementing `finalize` function is optional. This function allows
        the model to perform any necessary clean ups before exit.
        """
        print("Cleaning up cellpose-cyto-train...")
        self.model = None
        if self.gpu_mode:
            torch.cuda.empty_cache()
