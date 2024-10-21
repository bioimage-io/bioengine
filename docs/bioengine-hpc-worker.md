# Launch BioEngine Work on HPC

This guide will show you how to launch a BioEngine workflow on an HPC cluster.

## Prerequisites

You will need the following on your HPC cluster:
 - You cluster should be slurm or other HPC cluster with a job scheduler
 - The cluster should support containerization (e.g. Docker or Apptainer)
 - The cluster should have internet access

## Step 1: Install BioEngine

Create a conda environemnt or load a python module, then install BioEngine:

```bash
pip install hypha-launcher
```

## Step 2: Launch BioEngine

Configure the following environment variables:
 - `HYPHA_LAUNCHER_STORE_DIR`: The directory for storing data for the bioengine, it should be a directory with enough space to store the models and data.
 - `HYPHA_HPC_JOB_TEMPLATE`: The default command template for submitting jobs to the HPC cluster, you can use the following template for slurm as an example: `srun -A Your-Slurm-Account -t 03:00:00 --gpus-per-node A100:1 {cmd}`. Please adjust the template according to your cluster configuration.
 - `BIOENGINE_SERVICE_ID`: The service ID for the bioengine worker, you can use `bioengine-hpc-worker` as an example. This id will be used to identify your instance, so please make it unique.


```bash
export HYPHA_LAUNCHER_STORE_DIR=/path/to/store/data
export HYPHA_HPC_JOB_TEMPLATE="srun -A Your-Slurm-Account -t 03:00:00 --gpus-per-node A100:1 {cmd}"
export BIOENGINE_SERVICE_ID="bioengine-hpc-worker"

python -m hypha_launcher launch_bioengine_worker --hypha-server-url https://hypha.bioimage.io --triton-service-id $BIOENGINE_SERVICE_ID
```

This will start a BioEngine worker on your HPC cluster, and it will take a while to pull the docker image, download the model and launch the worker.

## Step 3: Use the BioEngine Worker

Now you can access the BioEngine worker at `https://bioimage-io.github.io/bioengine-web-client/?server-url=https://hypha.bioimage.io&triton-service-id=bioengine-hpc-worker`
(please replace `server-url=https://hypha.bioimage.io` and `triton-service-id=bioengine-hpc-worker` with your server URL and service ID)

Now you should be able to run models using your own BioEngine worker on your HPC cluster.

You can also access the bioengine via the API, please check the [API documentation](./api.md) for more details. **Importantly, you will need to replace the server_url and service_id (default to `triton-client` in the API document) with your own server URL and service ID.**
