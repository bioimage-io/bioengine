
## Creating the environment

For triton with python 3.10
```
export PYTHONNOUSERSITE=True
conda create -n cellpose-triton python=3.10 -y # we use 3.10 so we don't need to provide the stub
conda activate cellpose-triton
# Install cellpose with patch: https://github.com/MouseLand/cellpose/pull/331
conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch -y
conda install -c conda-forge libstdcxx-ng=12 -y # see here https://github.com/triton-inference-server/server/issues/5933#issuecomment-1589767408
pip install git+https://github.com/oeway/cellpose.git@patch-1#egg=cellpose
pip install matplotlib bioimageio.core
pip install conda-pack==0.7.0
conda-pack
```

For triton with python 3.8
```
export PYTHONNOUSERSITE=True
conda create -n cellpose-triton python=3.8 # we use 3.8 so we don't need to provide the stub
# Install cellpose with patch: https://github.com/MouseLand/cellpose/pull/331
pip install git+https://github.com/oeway/cellpose.git@patch-1#egg=cellpose
pip uninstall torch
conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c nvidia
conda install conda-pack
conda-pack
```

