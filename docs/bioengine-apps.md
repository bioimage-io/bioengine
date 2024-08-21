# BioEngine Apps

## 1. Introduction

**BioEngine** is an advanced web platform designed to democratize AI in life sciences by offering cloud-powered tools for bioimage analysis. It enables users to create interactive annotation tools, host AI models for inference and training, and integrate these capabilities seamlessly into existing workflows. BioEngine's architecture consists of several key components, including **Hypha**, **NVIDIA Triton Inference Server**, **Ray**, and **ImJoy plugins**. These components work together to support two main types of applications:

- **UI Apps**: Web-based applications that interact with BioEngine's Compute Apps through the Hypha server.
- **Compute Apps**: Applications that provide computational services, such as AI model inference and training, which can be accessed by UI Apps.

This documentation will guide you through the steps to create and deploy both UI and Compute Apps using the BioEngine platform.

---

## 2. Architecture Overview

The architecture of BioEngine is designed to be modular, scalable, and easy to integrate with various bioimaging software environments. Below is an overview of the core components:

- **Hypha**: The central communication hub of BioEngine, Hypha is an RPC-based framework that facilitates communication between different components of the platform. It orchestrates the interactions between UI Apps and Compute Apps, enabling real-time data exchange and service discovery.
  
- **NVIDIA Triton Inference Server**: This server handles AI model inference, allowing BioEngine to efficiently manage GPU resources. Triton supports multiple AI frameworks, including TensorFlow, PyTorch, and ONNX, making it versatile for various bioimage analysis tasks.
  
- **Ray**: Ray is a distributed computing framework used in BioEngine for scalable AI model training and inference. It manages distributed tasks across a cluster, ensuring efficient use of computational resources.
  
- **ImJoy Plugins**: ImJoy is a plugin-based architecture that allows users to create interactive, web-based tools that can communicate with BioEngine's Compute Apps. These plugins can be customized to perform specific tasks, such as image processing or AI model inference.

![BioEngine Architecture](path_to_architecture_image)

The diagram above illustrates how these components interact within the BioEngine platform. UI Apps communicate with the Hypha server, which routes requests to the appropriate Compute App for processing.

---

## 3. Getting Started

### Prerequisites

To create BioEngine Apps, you need to ensure that the following prerequisites are met:

- **Hypha Server**: The Hypha server should be set up and running. This server will act as the central communication point for your BioEngine Apps.
- **Docker**: Docker should be installed on your system to manage containerized applications. For larger deployments, Kubernetes should be configured.
- **Programming Knowledge**: Basic knowledge of JavaScript (for UI Apps) and Python (for Compute Apps) is required.

### Installation

1. **Clone the BioEngine repository**:

   ```bash
   git clone https://github.com/your-org/bioengine.git
   cd bioengine
   ```

2. **Set up the environment**:

   Ensure that Docker is installed on your system. For Kubernetes deployments, set up your cluster using the provided Helm charts.

3. **Deploy the BioEngine stack**:

   Use Docker Compose for local deployment or Kubernetes for scalable deployment. 

   For Docker Compose:
   
   ```bash
   docker-compose up -d
   ```

   For Kubernetes:
   
   ```bash
   kubectl apply -f k8s-deployment.yaml
   ```

4. **Access the BioEngine Dashboard**:

   Once the deployment is complete, access the BioEngine dashboard by navigating to `http://localhost:PORT` in your browser. The dashboard provides access to the API documentation and management interfaces for your BioEngine Apps.

---

## 4. Creating a BioEngine UI App

### Example UI App

The following example demonstrates how to create a simple UI App that connects to the BioEngine platform and registers a service for AI model inference.

```html
<script type="module">
  import { connectToServer } from "https://cdn.jsdelivr.net/npm/hypha-rpc@0.20.27/dist/hypha-rpc-websocket.mjs";

  const server = await connectToServer({
    server_url: "https://ai.aicell.io",
    workspace: "default",
  });

  server.export({
    id: "my-ui-service",
    getImage() {
      // Logic to retrieve and return an image for processing
      return "data:image/png;base64,...";
    },
  });
</script>
```

**Explanation**:
- **Connecting to the Hypha server**: The `connectToServer` function initiates a WebSocket connection to the Hypha server, using the provided server URL and workspace ID.
- **Registering the service**: The `server.export` function registers a service named `my-ui-service` that can retrieve an image from the UI for processing by a Compute App.

### Detailed Steps:

1. **Develop the UI Logic**:
   - Implement the logic for your UI App. This could involve creating an interface for users to upload images, adjust settings, or visualize results.

2. **Connect to Hypha Server**:
   - Use the provided API to establish a connection to the Hypha server. This connection allows your UI App to discover and interact with Compute Apps registered on the same server.

3. **Register UI Services**:
   - Define and register services within your UI App that will interact with Compute Apps. For example, a `getImage` service might allow a Compute App to request an image for AI model inference.

4. **Deploy and Test the UI App**:
   - Once the UI App is developed, deploy it within your BioEngine environment. Load the app in a browser and test its functionality by interacting with the registered Compute Apps.

---

## 5. Creating a BioEngine Compute App

### Example Compute App

Here’s an example of a Compute App that provides an interface for a Cellpose AI model used for cell segmentation. This app is built using Ray and is designed to be accessible via the Hypha server.

```python
from hypha_rpc import api

class CellposeModel:
    def __init__(self):
        # Load the pre-trained Cellpose model
        self.model = load_cellpose_model()

    def predict(self, image: str) -> str:
        # Perform prediction using the loaded model
        results = self.model.predict(image)
        return results

    def train(self, data: str, config: str) -> str:
        # Train the model with provided data and configuration
        training_results = self.model.train(data, config)
        return training_results

api.export(CellposeModel, {"name": "cellpose"})
```

**Explanation**:
- **Loading the Model**: The `CellposeModel` class initializes by loading the pre-trained Cellpose model, which is used for cell segmentation.
- **Predict and Train Methods**: The `predict` method takes an image as input and returns segmentation results. The `train` method allows users to train the model with new data and configuration settings.
- **Exporting the Service**: The `api.export` function registers the `CellposeModel` as a service on the Hypha server, making it accessible to UI Apps.

### Detailed Steps:

1. **Define the Compute App Logic**:
   - Implement the core logic for your Compute App, which might involve loading AI models, processing data, or handling training tasks.

2. **Connect to Hypha Server**:
   - Use the Hypha RPC API to export your Compute App as a service. This makes your app discoverable and accessible to other components within the BioEngine platform.

3. **Deploy the Compute App**:
   - Containerize your Compute App using Docker, and deploy it within your BioEngine environment. Ensure it is registered with the Hypha server and is ready to handle requests from UI Apps.

4. **Test and Optimize**:
   - Test the Compute App by sending requests from a UI App. Monitor performance and optimize as needed, particularly if working with large datasets or complex models.

---

## 6. Technical Explanation

**Communication between UI Apps and Compute Apps**:
- The **Hypha server** acts as a middleware, facilitating communication between UI Apps and Compute Apps. It handles service registration, discovery, and message routing.
- **WebSocket connections** are used for real-time data exchange, allowing UI Apps to interact with Compute Apps without significant delays.
- **Service Registration**: Each service within a UI or Compute App is registered with the Hypha server, enabling seamless discovery and interaction between different components.

**Resource Management**:
- **Ray** efficiently manages distributed computing tasks across a cluster, ensuring that available resources are used effectively. This is particularly important for training large AI models or processing high-throughput data.
- **NVIDIA Triton** optimizes AI model inference by dynamically scheduling tasks based on system load and user demand, ensuring that GPU resources are allocated where needed.

---

## 7. Example Workflow

**Step-by-Step Workflow**:

1. **Develop and Deploy the Compute App**:
   - Write the model logic in Python, implement necessary methods for prediction and training, and containerize the app.
   - Deploy the Compute App in a Docker or Kubernetes environment, ensuring it connects to the Hypha server.

2. **Develop the UI App**:
   - Create a user-friendly web interface using JavaScript/TypeScript. Implement services that will interact with the Compute App for tasks like image retrieval and result visualization.

3. **Test the Integration**:
   - Load the UI App in a browser, interact with the Compute App by sending requests, and visualize the results. Test various scenarios to ensure robustness and reliability.

4. **Optimize and Deploy**:
   - Optimize both the UI and Compute Apps based on performance testing. Once ready, deploy

 them in the production environment for end-users.

---

## 8. Results

**Expected Outcomes**:

- **Real-time AI Inference**: Users can perform real-time AI model inference directly from the browser, with results processed and returned by the Compute App.
- **Scalable AI Model Training**: The Compute App, powered by Ray, can handle large-scale model training, distributing tasks across multiple nodes to accelerate the process.
- **Interactive Visualization**: The UI App provides immediate feedback and visualization of results, allowing users to interact with and adjust their analysis in real-time.

**Case Study**:
- **Cell Segmentation with Cellpose**: A UI App was developed to upload cell images, which were then processed by a Compute App running the Cellpose model. The results were visualized directly within the UI, enabling researchers to refine their analysis parameters on the fly.

---

## 9. Conclusion

Creating BioEngine Apps allows you to harness the power of cloud-based AI tools for bioimage analysis. With its modular architecture and support for both UI and Compute Apps, BioEngine offers flexibility and scalability, making advanced bioimage analysis accessible to a broad audience. Whether developing a simple annotation tool or a complex AI model training pipeline, BioEngine provides the necessary infrastructure to bring your projects to life.

**Future Directions**:
- Continued development will focus on enhancing scalability, optimizing resource management, and expanding support for additional AI frameworks and bioimaging tools.

---

## 10. Acknowledgements

- **EU Horizon Europe**: This project is funded by the EU’s Horizon Europe program, grant no. 101057970, which supports research and innovation in advanced technologies.
- **NVIDIA**: Thanks to NVIDIA for providing the Triton Inference Server and computing credits, which are integral to the BioEngine platform's performance.
- **Bioimaging Community**: Special thanks to the testers and participants in the AI4Life Stockholm Hackathon 2023 for their valuable feedback, which has helped refine BioEngine's features.

**Contact and Support**:
- **Community Feedback**: We encourage you to try BioEngine and share your experiences on our GitHub issues page or the image.sc forum. Your input is crucial for the continual refinement of this platform.
- **Support**: For any questions or support, please contact us via the details provided on the BioEngine dashboard.