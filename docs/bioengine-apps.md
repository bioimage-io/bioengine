### BioEngine Apps Development

Developing BioEngine Apps involves creating both user interfaces (UI Apps) and computational backends (Compute Apps). These apps work together to provide a seamless experience for bioimage analysis and AI-powered tasks. This guide offers a comprehensive overview of how developers can build and contribute BioEngine Apps, leveraging modern web technologies, the BioEngine platform, and its associated tools.

#### 1. Developing UI Apps with ImJoy

**Overview:**
UI Apps are web-based interfaces that allow users to interact with BioEngine. They are designed to be intuitive, responsive, and capable of handling various tasks such as image uploading, configuring analysis parameters, visualizing results, and managing workflows.

**Key Concepts in ImJoy:**
ImJoy is a flexible platform that supports multiple plugin types, allowing developers to create web-based plugins that can serve as UI Apps in BioEngine. These plugins can be integrated with the backend services provided by BioEngine Compute Apps, making them powerful tools for bioimage analysis.

**Step-by-Step Guide to Developing a UI App:**

1. **Understanding ImJoy Plugin Types:**
   - **Window Plugins:** For building web UI using HTML, CSS, and JavaScript.
   - **Web-Worker Plugins:** For performing computations in a separate browser thread.
   - **Web-Python Plugins:** For running Python code in the browser using WebAssembly and Pyodide.
   - **Native-Python Plugins:** For heavy computations on local or remote servers.

2. **Creating Your First ImJoy Plugin:**
   - Start with a simple plugin that uses ImJoy’s API to interact with users and perform basic tasks.
   - Example:
     ```html
     <config lang="json">
     {
       "name": "Image Viewer",
       "type": "window",
       "version": "0.1.0"
     }
     </config>
     <script lang="javascript">
     class ImJoyPlugin{
         async setup(){
             await api.log("Plugin initialized");
         }
         async run(){
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

3. **Enhancing UI with External Libraries:**
   - Utilize CSS frameworks like Bootstrap or Bulma for styling, and integrate JavaScript frameworks like React or Vue.js for building dynamic UIs.
   - Example of integrating Bulma:
     ```html
     <config lang="json">
     {
       "requirements": ["https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css"]
     }
     </config>
     <window>
         <div class="container">
             <button class="button is-primary">Click me</button>
         </div>
     </window>
     ```

4. **Connecting the UI to Compute Apps:**
   - Use ImJoy’s RPC system to interact with Compute Apps running on BioEngine, allowing for remote function calls and data exchange between the UI and backend services.
   - Example of using RPC:
     ```javascript
     async function processImage() {
         const server = await hyphaWebsocketClient.connectToServer({"server_url": "https://ai.imjoy.io"});
         const svc = await server.getService("image-processing-service");
         const result = await svc.process({ image: base64Image });
         displayResult(result);
     }
     ```

5. **Deploying and Sharing Your UI App:**
   - Deploy the UI App on ImJoy or other platforms and share it with users by providing a URL or hosting it on platforms like GitHub.

#### 2. Developing Compute Apps

**Overview:**
Compute Apps are the backend services that perform the heavy computations required by BioEngine applications. These apps can be developed to run either as Hypha services in independent containers or directly on workstations, typically equipped with GPUs.

**Options for Deploying Compute Apps:**

1. **Running as a Hypha Service:**
   - Develop Compute Apps as Hypha services and deploy them in independent containers, which can be scaled and managed through Kubernetes.

2. **Running on Local Workstations:**
   - Developers can run Compute Apps directly on their workstations, leveraging local GPUs for intensive computations. This is particularly useful for development, testing, or specific tasks requiring immediate access to hardware resources.

**Submitting Compute Apps to BioEngine:**
If developers want to submit their Compute App to the BioEngine platform, they need to wrap it as a BioEngine Ray app. This involves creating a specific structure, including an entry point script and a manifest file, and then submitting the app via a GitHub pull request.

**Step-by-Step Guide to Submitting a Compute App:**

1. **Developing the Compute App:**
   - Start by implementing the core logic of your app, such as image processing or AI model inference. Use libraries like TensorFlow, PyTorch, or OpenCV to handle the computational tasks.
   - Example for a Cellpose model:
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

2. **Creating the Manifest File:**
   - Prepare a `manifest.yaml` file that describes the app, including its runtime environment, dependencies, and Ray configuration.
   - Example:
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

3. **Submitting the App:**
   - Submit your Compute App to BioEngine by creating a new folder in the [BioEngine repository](https://github.com/bioimage-io/bioengine/tree/main/bioimageio/engine) and adding the `__init__.py` and `manifest.yaml` files. 
   - Create a GitHub pull request (PR) with these files, and the BioEngine team will review your submission and decide whether to include it in the platform.

**Running the Compute App Locally or on a Server:**
After submission, developers can continue to run their Compute Apps locally or on a server using Ray and Hypha, ensuring they meet performance and scalability requirements before or after integration with the BioEngine platform.

#### Conclusion

By following this guide, developers can create and contribute BioEngine Apps that integrate intuitive user interfaces with powerful backend computations. The flexibility of the BioEngine platform, combined with tools like ImJoy and Hypha, provides developers with the means to build, deploy, and scale applications that meet the growing needs of the bioimage analysis community. Whether running on local hardware or as part of a larger cloud infrastructure, BioEngine Apps enable cutting-edge research and collaboration in life sciences.