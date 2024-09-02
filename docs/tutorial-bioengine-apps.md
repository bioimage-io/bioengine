# Step-by-Step Tutorial: How to Create BioEngine Apps

Welcome to the tutorial on creating BioEngine Apps! In this guide, we'll walk you through the process of developing and submitting both UI and Compute Apps for the BioEngine platform. Whether you're building a user interface or a computational backend, this tutorial will help you get started and contribute your app to the BioEngine ecosystem.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

1. **Basic Programming Skills:** Familiarity with Python, JavaScript, and web development concepts.
2. **Development Environment:**
   - Python 3.7 or higher installed on your machine.
   - A modern web browser (e.g., Chrome, Firefox).
   - Git installed for version control.
3. **Tools and Libraries:**
   - Install the necessary Python packages:
     ```bash
     pip install hypha-rpc
     pip install ray
     ```

## Step 1: Set Up Your Development Environment

1. **Clone the BioEngine Repository:**
   - Start by cloning the BioEngine GitHub repository to your local machine:
     ```bash
     git clone https://github.com/bioimage-io/bioengine.git
     cd bioengine/bioimageio/engine
     ```

2. **Create a New Folder for Your App:**
   - Inside the `bioengine/bioimageio/engine` directory, create a new folder for your app:
     ```bash
     mkdir my-bioengine-app
     cd my-bioengine-app
     ```

## Step 2: Develop the Compute App

Compute Apps are the backend services that perform computations. In this example, we'll create a simple Compute App using Cellpose for cell segmentation.

1. **Create the `__init__.py` File:**
   - This file will contain the main logic for your Compute App. Here’s an example using the Cellpose model:
     ```python
     from hypha_rpc import api
     import numpy as np

     class CellposeModel:
         def __init__(self):
             from cellpose import core
             self.use_GPU = core.use_gpu()
             print('>>> GPU activated? %d' % self.use_GPU)
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
             model = self._load_model(model_type)
             if channels is None:
                 channels = [[2, 3]] * len(images)
             masks, flows, styles, diams = model.eval(images, diameter=diameter, flow_threshold=flow_threshold, channels=channels)
             results = {
                 'masks': [mask.tolist() for mask in masks],
                 'diameters': diams
             }
             return results

         def train(self, images, labels, config):
             raise NotImplementedError("Training functionality not implemented yet")

     api.export(CellposeModel)
     ```

2. **Create the `manifest.yaml` File:**
   - This file contains metadata and configuration for your app:
     ```yaml
     name: Cellpose
     id: cellpose
     description: Cellpose is a generalist algorithm for cell and nucleus segmentation
     runtime: ray
     entrypoint: __init__.py
     ray_serve_config:
       ray_actor_options:
         num_gpus: 1
         runtime_env:
           pip:
             - opencv-python-headless==4.2.0.34
             - cellpose==3.0.11
             - torch==2.3.1
             - torchvision==0.18.1 
       autoscaling_config:
         downscale_delay_s: 1
         min_replicas: 0
         max_replicas: 2
     ```

## Step 3: Develop the UI App

UI Apps are web-based interfaces that interact with the Compute Apps. In this example, we’ll create a simple ImJoy plugin for image visualization and interaction with the Compute App.

1. **Create a New File for the UI App:**
   - In the `my-bioengine-app` folder, create a file named `image_viewer.imjoy.html`:
     ```html
     <config lang="json">
     {
       "name": "Image Viewer",
       "type": "window",
       "version": "0.1.0"
     }
     </config>
     <script lang="javascript">
     class ImJoyPlugin {
         async setup() {
             await api.log("Plugin initialized");
         }
         async run() {
             await api.alert("Hello from ImJoy!");
         }
     }
     api.export(new ImJoyPlugin());
     </script>
     <window>
         <div>
             <h1>Hello, World!</h1>
             <p>Welcome to your first ImJoy plugin.</p>
         </div>
     </window>
     ```

2. **Connect the UI App to the Compute App:**
   - Modify the `image_viewer.imjoy.html` file to connect to the Cellpose Compute App:
     ```html
     <script lang="javascript">
     class ImJoyPlugin {
         async setup() {
             this.server = await hyphaWebsocketClient.connectToServer({"server_url": "https://ai.imjoy.io"});
             this.cellposeService = await this.server.getService("cellpose");
             await api.log("Plugin initialized");
         }

         async run() {
             const result = await this.cellposeService.predict({images: [/* image data */]});
             await api.alert("Segmentation result: " + JSON.stringify(result));
         }
     }
     api.export(new ImJoyPlugin());
     </script>
     ```

## Step 4: Testing Your BioEngine App

1. **Run the Compute App:**
   - If you're running the Compute App locally:
     ```bash
     python __init__.py
     ```

2. **Test the UI App:**
   - Open the ImJoy web app: [ImJoy.io](https://imjoy.io/#/app)
   - Drag and drop the `image_viewer.imjoy.html` file into the ImJoy interface.
   - Run the plugin and check the console for outputs.

## Step 5: Submitting Your App to BioEngine

1. **Prepare Your Files for Submission:**
   - Ensure that your `__init__.py` and `manifest.yaml` files are complete and tested.

2. **Create a Pull Request:**
   - Push your changes to a new branch in your forked GitHub repository.
   - Create a pull request (PR) to the main BioEngine repository with your new app folder.

3. **Submit Your PR:**
   - Provide a detailed description of your app, including its functionality, dependencies, and any special instructions.
   - The BioEngine team will review your submission and provide feedback or merge it into the main repository.

## Conclusion

Congratulations! You've created and submitted a BioEngine App. This tutorial has guided you through the development of both UI and Compute Apps, from setup to submission. By contributing to BioEngine, you’re helping to expand a powerful platform for bioimage analysis and AI-driven research.

If you have any questions or need further assistance, feel free to reach out to the BioEngine community on GitHub or through our support channels. Happy coding!

