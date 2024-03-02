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

import os
import json
import torch
import gc
import sys
import numpy as np
import traceback

# triton_python_backend_utils is available in every Triton Python model. You
# need to use this module to create inference requests and responses. It also
# contains some utility functions for extracting information from model_config
# and converting Triton input/output types to numpy types.
import triton_python_backend_utils as pb_utils

# make sure we can import the interactive_cellpose.py file
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../cellpose-train/1/")),
)
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

        self.gpu_mode = args["model_instance_kind"] == "GPU"
        self.model = None

    def initialize_model(self, corrid):
        """`initialize_model` is called when the model is being loaded. Implementing
        `initialize_model` function is optional. This function allows the model to
        load any state associated with this model.
        """
        print(f"{corrid}: Loading CellPose model {corrid} ...")
        default_save_path = os.path.join(self.model_root, corrid, "model.pth")
        if not os.path.exists(default_save_path):
            raise Exception(f"Model not found: {default_save_path}")

        # Instantiate the PyTorch model
        self.model = CellPoseInteractiveModel(
            model_dir=self.model_root,
            model_id=corrid,
            resume=True,
            default_save_path=default_save_path,
        )
        print(f"Cellpose model successfully initialized {corrid}.")

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
            # start_flag = pb_utils.get_input_tensor_by_name(request, "START").as_numpy()[
            #     0
            # ]
            # end_flag = pb_utils.get_input_tensor_by_name(request, "END").as_numpy()[0]
            # Get image
            in_0 = pb_utils.get_input_tensor_by_name(request, "image")
            image = in_0.as_numpy()
            assert len(image.shape) == 3
            model_id = str(request.correlation_id())
            try:
                param = pb_utils.get_input_tensor_by_name(request, "param")
                param = param.as_numpy().astype(np.bytes_)[0]  # assume it's a scalar
                param = str(np.char.decode(param, "UTF-8"))
                param = json.loads(param)
                reload = False
                if "reload" in param:
                    reload = param.pop("reload")
                if not self.model or self.model_id != model_id or reload:
                    with open(
                        os.path.join(self.model_root, model_id, "config.json"), "r"
                    ) as fil:
                        previous_param = json.loads(fil.read())
                    model_file_path = os.path.join(
                        self.model_root, model_id, "model.pth"
                    )
                    if not os.path.exists(model_file_path):
                        raise Exception(f"Model file not found: {model_file_path}")
                    print("Initialize model from " + model_file_path)

                    self.initialize_model(model_id)
                    self.model_id = model_id
                # model.net.load_state_dict(torch.load(model_file_path), strict=True)
                # full list of parameters can be found here: https://github.com/MouseLand/cellpose/blob/6fddd4da98219195a2d71041fb0e47cc69a4b3a6/cellpose/models.py#L101-L174
                test_image = np.expand_dims(image, axis=0)
                masks, styles = self.model.predict(
                    test_image, return_styles=True, **param
                )
                # Create output tensors. You need pb_utils.Tensor
                # objects to create pb_utils.InferenceResponse.
                out_tensor_0 = pb_utils.Tensor("mask", masks[0])  # uint16
                out_tensor_1 = pb_utils.Tensor("style", styles[0])  # float32

                # Create InferenceResponse. You can set an error here in case
                # there was a problem with handling this inference request.
                # Below is an example of how you can set errors in inference
                # response:
                #
                # pb_utils.InferenceResponse(
                #    output_tensors=..., TritonError("An error occured"))
                inference_response = pb_utils.InferenceResponse(
                    output_tensors=[out_tensor_0, out_tensor_1]
                )
                responses.append(inference_response)
            except Exception:
                responses.append(
                    pb_utils.InferenceResponse(
                        output_tensors=[],
                        error=pb_utils.TritonError(
                            "An error occurred: " + str(traceback.format_exc())
                        ),
                    )
                )

        # You should return a list of pb_utils.InferenceResponse. Length
        # of this list must match the length of `requests` list.
        return responses

    def finalize(self):
        """`finalize` is called only once when the model is being unloaded.
        Implementing `finalize` function is optional. This function allows
        the model to perform any necessary clean ups before exit.
        """
        print("Cleaning up cellpose...")
        gc.collect()
        if self.gpu_mode:
            torch.cuda.empty_cache()
