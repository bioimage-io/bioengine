<img src='https://raw.githubusercontent.com/bioimage-io/bioengine/main/docs/img/bioengine-logo-black.svg' width='600'>

# BioEngine: Your AI Engine for Advanced BioImage Analysis

BioEngine revolutionizes bioimage analysis by harnessing the power of cutting-edge AI within a flexible, containerized environment. This Python package, built on the robust foundation of [hypha](https://github.com/amun-ai/hypha), is meticulously designed to facilitate the deployment and execution of sophisticated bioimage analysis models and workflows. It offers a seamless, user-friendly interface through HTTP API and RPC, simplifying the integration of AI technologies into bioimage analysis without the need for intricate setup or deep technical expertise.

Understanding the diverse needs of the bioimage community, BioEngine provides a public server available at [https://hypha.bioimage.io](https://hypha.bioimage.io). This server acts as a crucial support hub for the BioImage Model Zoo ([https://bioimage.io](https://bioimage.io)), enabling users to test run models directly or connect through community-developed tools. This initiative not only fosters collaboration but also amplifies the accessibility of advanced AI tools across the field.

Recognizing the paramount importance of data privacy and the need for scalable solutions, BioEngine is designed for versatility. It can be easily deployed across a range of environments—from personal laptops and lab workstations to high-performance computing (HPC) systems and Kubernetes clusters. This adaptability ensures that regardless of your setup, BioEngine can be integrated smoothly, eliminating data transmission concerns and enhancing scalability. To support this wide range of deployment scenarios, we offer specialized toolkits tailored to meet the specific requirements of each platform.

BioEngine stands as a beacon for developers and researchers alike, providing an accessible gateway to the forefront of AI-powered bioimage analysis. By simplifying complex processes and fostering an environment of innovation, BioEngine is not just a tool but a partner in advancing the boundaries of bioimage research.

## BioEngine Apps: Extending BioEngine's Capabilities

### What Are BioEngine Apps?

BioEngine Apps are specialized applications designed to leverage the full power of the BioEngine platform. These apps are divided into two categories:
- **UI Apps**: User-facing applications that provide interactive interfaces for data upload, parameter configuration, and result visualization. These apps are typically developed using web technologies such as ImJoy, React, or Vue.js, and run directly in the user's web browser.
- **Compute Apps**: Backend services that handle the heavy computational tasks, such as AI model inference, training, and data processing. Compute Apps can be deployed in cloud environments or run on local workstations with GPU support, depending on the computational requirements.

### How to Develop BioEngine Apps

Developing BioEngine Apps is a straightforward process that allows you to create both UI and Compute Apps to extend the functionality of the BioEngine platform. Here’s how you can get started:

1. **UI Apps Development**: 
   - UI Apps are designed to provide an interface for users to interact with the BioEngine’s backend services. You can use web development frameworks like ImJoy, React, or Vue.js to build these applications.
   - To connect your UI App with BioEngine services, you can use the `hypha-rpc` library, which facilitates real-time communication between the UI and backend services.
   - For more detailed steps and code examples, refer to the [BioEngine Apps Development Documentation](./bioengine-apps.md).

2. **Compute Apps Development**:
   - Compute Apps handle the backend processing tasks such as AI model inference, data analysis, and more. These apps can either be developed as services running in independent containers or executed directly on local workstations with GPU support.
   - To contribute your Compute App to BioEngine, wrap it as a Ray app and provide the necessary configuration files, then submit it via a pull request to the BioEngine GitHub repository.
   - Detailed guidelines for developing and submitting Compute Apps are available in the [BioEngine Apps Tutorial](./tutorial-bioengine-apps.md).

## Installation

You can set up the BioEngine worker on your own HPC by following the instructions in the [BioEngine HPC worker guide](./bioengine-hpc-worker.md).

## Using the BioEngine

You can access the BioEngine directly from the [BioImage.IO website](https://bioimage.io). For most models, you will find a test run button to execute it with your own images.

To use the BioEngine, you can try it with:
 - [bioengine-web-client](https://bioimage-io.github.io/bioengine-web-client/): A simple web app which allows you to run models from the BioImage Model Zoo.
 - [BioImage Model Zoo](https://bioimage.io): A repository of models for bioimage analysis, click any model and scroll down to the section about "Test this model".

## Development

BioEngine is an engine running behind the scenes, allowing developers to interact with it via Python, JavaScript, or any other language that supports HTTP. Please refer to our [API documentation](api.md) for more information.

## Tutorial
 - Developing BioEngine Apps: [Tutorial](./tutorial-bioengine-apps.md)
To get started with BioEngine, please see:
 - [BioEngine tutorial for "Microscopy data analysis: machine learning and the BioImage Archive virtual course" hosted by EMBL-EBI](https://imjoy-notebook.netlify.app/lab/index.html?load=https://raw.githubusercontent.com/bioimage-io/bioengine/main/notebooks/bioengine-tutorial-embl-2024.ipynb&open=1) (NOTE: In case of issues running the notebook, please try to start this notebook in Chrome, using incognito mode).
 - [BioEngine Tutorial for I2K 2023](https://slides.imjoy.io/?slides=https://raw.githubusercontent.com/bioimage-io/BioEngine/main/slides/i2k-2023-bioengine-workshop.md).

Please read the full documentation at: [BioEngine Documentation](https://bioimage-io.github.io/bioengine/).

## Deployment Toolkits

You are welcome to deploy your own BioEngine in your own workstation, HPC or Kubernetes cluster. We provide toolkits for support various settings, currently the following instructions are provided:
 * [x] HPC: [Deployment instructions](bioengine-hpc-worker.md)
   - [x]Slurm
   - other cluster setting please submit an issue
 * [x] Kubernetes: [Deployment instructions](k8s-toolkit.md)
