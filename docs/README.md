<img src='https://raw.githubusercontent.com/bioimage-io/bioengine/main/docs/img/bioengine-logo-black.svg' width='600'>

# BioEngine: Your AI Engine for Advanced BioImage Analysis

BioEngine revolutionizes bioimage analysis by harnessing the power of cutting-edge AI within a flexible, containerized environment. This Python package, built on the robust foundation of [hypha](https://github.com/amun-ai/hypha), is meticulously designed to facilitate the deployment and execution of sophisticated bioimage analysis models and workflows. It offers a seamless, user-friendly interface through HTTP API and RPC, simplifying the integration of AI technologies into bioimage analysis without the need for intricate setup or deep technical expertise.

Understanding the diverse needs of the bioimage community, BioEngine provides a public server available at [https://hypha.bioimage.io](https://hypha.bioimage.io). This server acts as a crucial support hub for the BioImage Model Zoo ([https://bioimage.io](https://bioimage.io)), enabling users to test run models directly or connect through community-developed tools. This initiative not only fosters collaboration but also amplifies the accessibility of advanced AI tools across the field.

Recognizing the paramount importance of data privacy and the need for scalable solutions, BioEngine is designed for versatility. It can be easily deployed across a range of environments—from personal laptops and lab workstations to high-performance computing (HPC) systems and Kubernetes clusters. This adaptability ensures that regardless of your setup, BioEngine can be integrated smoothly, eliminating data transmission concerns and enhancing scalability. To support this wide range of deployment scenarios, we offer specialized toolkits tailored to meet the specific requirements of each platform.

BioEngine stands as a beacon for developers and researchers alike, providing an accessible gateway to the forefront of AI-powered bioimage analysis. By simplifying complex processes and fostering an environment of innovation, BioEngine is not just a tool but a partner in advancing the boundaries of bioimage research.

## Installation

You can setup the BioEngine worker on your own HPC by following the instructions in the [BioEngine HPC worker](./bioengine-hpc-worker.md) guide.

## Using the BioEngine

You can access the BioEngine directly from the [BioImage.IO website](https://bioimage.io), for most of the models, you will find a test run button to execute it with your own images.



To use the BioEngine, you can try it with:
 - [bioengine-web-client](https://bioimage-io.github.io/bioengine-web-client/): A simple web app which allows you to run models from the BioImage Model Zoo.
 - [BioImage Model Zoo](https://bioimage.io): A repository of models for bioimage analysis, click any model and scroll down to the section about "Test this model".


## Development

BioEngine is an engine running behind the scenes, developers can interact with it python, javascript code or any other language that supports HTTP. Please take a look at our [API document](api.md).

## Tutorial

To get started with BioEngine, please see
 - [BioEngine tutorial for "Microscopy data analysis: machine learning and the BioImage Archive virtual course" hosted by EMBL-EBI](https://imjoy-notebook.netlify.app/lab/index.html?load=https://raw.githubusercontent.com/bioimage-io/bioengine/main/notebooks/bioengine-tutorial-embl-2024.ipynb&open=1) (NOTE: In case of issue in running the notebook, please try to start this notebook in Chrome, using incognito mode)
 - [BioEngine Tutorial for I2K 2023](https://slides.imjoy.io/?slides=https://raw.githubusercontent.com/bioimage-io/BioEngine/main/slides/i2k-2023-bioengine-workshop.md).

Please read the documentation at: https://bioimage-io.github.io/bioengine/

## Deployment toolkits

You are welcome to deploy your own BioEngine in your own workstation, HPC or Kubernetes cluster. We provide toolkits for support various settings, currently the following instructions are provided:
 * [x] HPC: [Deployment instructions](bioengine-hpc-worker.md)
   - [x]Slurm
   - other cluster setting please submit an issue
 * [x] Kubernetes: [Deployment instructions](k8s-toolkit.md)

## TODO

+ Runtime types support via hypha-launcher:
   * [x] HPC: Slurm / PBS / LFS ...
   * [ ] Conda environment
   * [x] Docker / Apptainer / podman ...
   * [ ] Web Browser
   * [ ] pytriton(python package)
   * [ ] SSH + X(other runtime types)
   * [x] K8S


pip install --target=/tmp/pip -U https://github.com/bioimage-io/bioengine/archive/refs/heads/main.zip

export PYTHONPATH=/tmp/pip:$PYTHONPATH:/tmp/pip

serve shutdown --address=http://service-ray-cluster:8265 -y && HYPHA_SERVER_URL=https://hypha.aicell.io HYPHA_WORKSPACE=bioengine-apps HYPHA_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FtdW4uYWkvIiwic3ViIjoiYXdha2UtY2l0cmluZS05OTYxNDc2MyIsImF1ZCI6Imh0dHBzOi8vYW11bi1haS5ldS5hdXRoMC5jb20vYXBpL3YyLyIsImlhdCI6MTcyNTIxNTc4NywiZXhwIjoxNzI5MDU0MTcxLCJzY29wZSI6IndzOmJpb2VuZ2luZS1hcHBzI3J3IHdpZDpiaW9lbmdpbmUtYXBwcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImh0dHBzOi8vYW11bi5haS9yb2xlcyI6WyJhZG1pbiJdLCJodHRwczovL2FtdW4uYWkvZW1haWwiOiJvZXdheTAwN0BnbWFpbC5jb20ifQ.2DtFsQeLSqKIsBy1ect4BlygjUMjWMUJZcLkAmcSSrg serve run bioimageio.engine.ray_app_manager:app --address=ray://service-ray-cluster:20002



HYPHA_SERVER_URL=https://hypha.aicell.io HYPHA_WORKSPACE=bioengine-apps HYPHA_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FtdW4uYWkvIiwic3ViIjoiYXdha2UtY2l0cmluZS05OTYxNDc2MyIsImF1ZCI6Imh0dHBzOi8vYW11bi1haS5ldS5hdXRoMC5jb20vYXBpL3YyLyIsImlhdCI6MTcyNTIxNTc4NywiZXhwIjoxNzI5MDU0MTcxLCJzY29wZSI6IndzOmJpb2VuZ2luZS1hcHBzI3J3IHdpZDpiaW9lbmdpbmUtYXBwcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImh0dHBzOi8vYW11bi5haS9yb2xlcyI6WyJhZG1pbiJdLCJodHRwczovL2FtdW4uYWkvZW1haWwiOiJvZXdheTAwN0BnbWFpbC5jb20ifQ.2DtFsQeLSqKIsBy1ect4BlygjUMjWMUJZcLkAmcSSrg python -m bioimageio.engine serve_ray_apps --address=ray://service-ray-cluster:20002




(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,587 E 648 648] logging.cc:343: PC: @     0x7f122829600b  (unknown)  raise
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @     0x7f12285b3420  1440643216  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @     0x7f12263c935a         80  __cxxabiv1::__terminate()
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @     0x7f1226b9934a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @     0x7f1226d1e902         96  std::_Sp_counted_ptr_inplace<>::_M_dispose()
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @     0x7f1226b9934a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @     0x7f1226c546f2        144  std::default_delete<>::operator()()
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @     0x7f1226ccca8d       1168  ray::core::CoreWorker::~CoreWorker()
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @     0x7f1226b9934a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @     0x7f1226d03534       1152  ray::core::CoreWorkerProcessImpl::RunWorkerTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @     0x7f1226d0369d         32  ray::core::CoreWorkerProcess::RunTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @     0x7f1226b06937         32  __pyx_pw_3ray_7_raylet_10CoreWorker_7run_task_loop()
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,589 E 648 648] logging.cc:343:     @           0x539080  (unknown)  method_vectorcall_NOARGS
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) [2024-08-31 14:46:03,591 E 648 648] logging.cc:343:     @           0x87b120  (unknown)  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) Fatal Python error: Aborted
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) 
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) Stack (most recent call first):
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 876 in main_loop
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/workers/default_worker.py", line 289 in <module>
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) 
(ServeReplica:default:HyphaRayAppManager pid=648, ip=10.42.6.166) Extension modules: msgpack._cmsgpack, psutil._psutil_linux, psutil._psutil_posix, setproctitle, yaml._yaml, _brotli, charset_normalizer.md, uvloop.loop, ray._raylet, pvectorc, ujson, grpc._cython.cygrpc, numpy.core._multiarray_umath, numpy.core._multiarray_tests, numpy.linalg._umath_linalg, numpy.fft._pocketfft_internal, numpy.random._common, numpy.random.bit_generator, numpy.random._bounded_integers, numpy.random._mt19937, numpy.random.mtrand, numpy.random._philox, numpy.random._pcg64, numpy.random._sfc64, numpy.random._generator, pandas._libs.tslibs.np_datetime, pandas._libs.tslibs.dtypes, pandas._libs.tslibs.base, pandas._libs.tslibs.nattype, pandas._libs.tslibs.timezones, pandas._libs.tslibs.tzconversion, pandas._libs.tslibs.ccalendar, pandas._libs.tslibs.fields, pandas._libs.tslibs.timedeltas, pandas._libs.tslibs.timestamps, pandas._libs.properties, pandas._libs.tslibs.offsets, pandas._libs.tslibs.parsing, pandas._libs.tslibs.conversion, pandas._libs.tslibs.period, pandas._libs.tslibs.vectorized, pandas._libs.ops_dispatch, pandas._libs.missing, pandas._libs.hashtable, pandas._libs.algos, pandas._libs.interval, pandas._libs.tslib, pandas._libs.lib, pandas._libs.hashing, pyarrow.lib, pyarrow._hdfsio, pandas._libs.ops, numexpr.interpreter, pyarrow._compute, pandas._libs.arrays, pandas._libs.index, pandas._libs.join, pandas._libs.sparse, pandas._libs.reduction, pandas._libs.indexing, pandas._libs.internals, pandas._libs.writers, pandas._libs.window.aggregations, pandas._libs.window.indexers, pandas._libs.reshape, pandas._libs.tslibs.strptime, pandas._libs.groupby, pandas._libs.testing, pandas._libs.parsers, pandas._libs.json, pyarrow._json (total: 71)
(ServeReplica:default:HyphaRayAppManager pid=2712) Exception raised in creation task: The actor died because of an error raised in its creation task, ray::SERVE_REPLICA::default#HyphaRayAppManager#e7zors3c:ServeReplica:default:HyphaRayAppManager.__init__() (pid=2712, ip=10.42.5.206, actor_id=cfc0984b7cc4904e0f1e32e105000000, repr=<ray.serve._private.replica.ServeReplica:default:HyphaRayAppManager object at 0x7f0adb21f490>)
(ServeReplica:default:HyphaRayAppManager pid=2712)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 449, in result
(ServeReplica:default:HyphaRayAppManager pid=2712)     return self.__get_result()
(ServeReplica:default:HyphaRayAppManager pid=2712)            ^^^^^^^^^^^^^^^^^^^
(ServeReplica:default:HyphaRayAppManager pid=2712)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
(ServeReplica:default:HyphaRayAppManager pid=2712)     raise self._exception
(ServeReplica:default:HyphaRayAppManager pid=2712)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeReplica:default:HyphaRayAppManager pid=2712)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 266, in __init__
(ServeReplica:default:HyphaRayAppManager pid=2712)     deployment_def = cloudpickle.loads(serialized_deployment_def)
(ServeReplica:default:HyphaRayAppManager pid=2712)                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeReplica:default:HyphaRayAppManager pid=2712) ModuleNotFoundError: No module named 'hypha_rpc'
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,765 E 2712 2712] logging.cc:115: Stack trace: 
(ServeReplica:default:HyphaRayAppManager pid=2712)  /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x103216a) [0x7f0bf35b416a] ray::operator<<()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x10351b2) [0x7f0bf35b71b2] ray::TerminateHandler()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/bin/../lib/libstdc++.so.6(+0xb135a) [0x7f0bf241535a] __cxxabiv1::__terminate()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/bin/../lib/libstdc++.so.6(+0xb13c5) [0x7f0bf24153c5]
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x7f7990) [0x7f0bf2d79990] std::thread::_State_impl<>::~_State_impl()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x65b34a) [0x7f0bf2bdd34a] std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x7e0902) [0x7f0bf2d62902] std::_Sp_counted_ptr_inplace<>::_M_dispose()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x65b34a) [0x7f0bf2bdd34a] std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x7166f2) [0x7f0bf2c986f2] std::default_delete<>::operator()()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(_ZN3ray4core10CoreWorkerD1Ev+0xfd) [0x7f0bf2d10a8d] ray::core::CoreWorker::~CoreWorker()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x65b34a) [0x7f0bf2bdd34a] std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(_ZN3ray4core21CoreWorkerProcessImpl26RunWorkerTaskExecutionLoopEv+0x124) [0x7f0bf2d47534] ray::core::CoreWorkerProcessImpl::RunWorkerTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(_ZN3ray4core17CoreWorkerProcess20RunTaskExecutionLoopEv+0x1d) [0x7f0bf2d4769d] ray::core::CoreWorkerProcess::RunTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2712) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x5c8937) [0x7f0bf2b4a937] __pyx_pw_3ray_7_raylet_10CoreWorker_7run_task_loop()
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager() [0x539080] method_vectorcall_NOARGS
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager(PyObject_Vectorcall+0x31) [0x51e6a1] PyObject_Vectorcall
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager(_PyEval_EvalFrameDefault+0x6a7) [0x5116e7] _PyEval_EvalFrameDefault
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager() [0x5cbeda] _PyEval_Vector
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager(PyEval_EvalCode+0x9f) [0x5cb5af] PyEval_EvalCode
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager() [0x5ec6a7] run_eval_code_obj
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager() [0x5e8240] run_mod
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager() [0x5fd192] pyrun_file
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager(_PyRun_SimpleFileObject+0x19f) [0x5fc55f] _PyRun_SimpleFileObject
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager(_PyRun_AnyFileObject+0x43) [0x5fc283] _PyRun_AnyFileObject
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager(Py_RunMain+0x2ee) [0x5f6efe] Py_RunMain
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager(Py_BytesMain+0x39) [0x5bbc79] Py_BytesMain
(ServeReplica:default:HyphaRayAppManager pid=2712) /lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf3) [0x7f0bf42c2083] __libc_start_main
(ServeReplica:default:HyphaRayAppManager pid=2712) ray::ServeReplica:default:HyphaRayAppManager() [0x5bbac3]
(ServeReplica:default:HyphaRayAppManager pid=2712) 
(ServeReplica:default:HyphaRayAppManager pid=2712) *** SIGABRT received at time=1725140764 on cpu 12 ***
(ServeReplica:default:HyphaRayAppManager pid=2712) PC: @     0x7f0bf42e100b  (unknown)  raise
(ServeReplica:default:HyphaRayAppManager pid=2712)     @     0x7f0bf45fe420  (unknown)  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=2712)     @     0x7f0bf241535a         80  __cxxabiv1::__terminate()
(ServeReplica:default:HyphaRayAppManager pid=2712)     @     0x7f0bf2bdd34a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2712)     @     0x7f0bf2d62902         96  std::_Sp_counted_ptr_inplace<>::_M_dispose()
(ServeReplica:default:HyphaRayAppManager pid=2712)     @     0x7f0bf2bdd34a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2712)     @     0x7f0bf2c986f2        144  std::default_delete<>::operator()()
(ServeReplica:default:HyphaRayAppManager pid=2712)     @     0x7f0bf2d10a8d       1168  ray::core::CoreWorker::~CoreWorker()
(ServeReplica:default:HyphaRayAppManager pid=2712)     @     0x7f0bf2bdd34a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2712)     @     0x7f0bf2d47534       1152  ray::core::CoreWorkerProcessImpl::RunWorkerTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2712)     @     0x7f0bf2d4769d         32  ray::core::CoreWorkerProcess::RunTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2712)     @     0x7f0bf2b4a937         32  __pyx_pw_3ray_7_raylet_10CoreWorker_7run_task_loop()
(ServeReplica:default:HyphaRayAppManager pid=2712)     @           0x539080  (unknown)  method_vectorcall_NOARGS
(ServeReplica:default:HyphaRayAppManager pid=2712)     @           0x87b120  (unknown)  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343: *** SIGABRT received at time=1725140764 on cpu 12 ***
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343: PC: @     0x7f0bf42e100b  (unknown)  raise
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @     0x7f0bf45fe420  (unknown)  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @     0x7f0bf241535a         80  __cxxabiv1::__terminate()
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @     0x7f0bf2bdd34a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @     0x7f0bf2d62902         96  std::_Sp_counted_ptr_inplace<>::_M_dispose()
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @     0x7f0bf2bdd34a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @     0x7f0bf2c986f2        144  std::default_delete<>::operator()()
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @     0x7f0bf2d10a8d       1168  ray::core::CoreWorker::~CoreWorker()
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @     0x7f0bf2bdd34a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @     0x7f0bf2d47534       1152  ray::core::CoreWorkerProcessImpl::RunWorkerTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @     0x7f0bf2d4769d         32  ray::core::CoreWorkerProcess::RunTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @     0x7f0bf2b4a937         32  __pyx_pw_3ray_7_raylet_10CoreWorker_7run_task_loop()
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,776 E 2712 2712] logging.cc:343:     @           0x539080  (unknown)  method_vectorcall_NOARGS
(ServeReplica:default:HyphaRayAppManager pid=2712) [2024-08-31 14:46:04,777 E 2712 2712] logging.cc:343:     @           0x87b120  (unknown)  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=2712) Fatal Python error: Aborted
(ServeReplica:default:HyphaRayAppManager pid=2712) 
(ServeReplica:default:HyphaRayAppManager pid=2712) Stack (most recent call first):
(ServeReplica:default:HyphaRayAppManager pid=2712)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 876 in main_loop
(ServeReplica:default:HyphaRayAppManager pid=2712)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/workers/default_worker.py", line 289 in <module>
(ServeReplica:default:HyphaRayAppManager pid=2712) 
(ServeReplica:default:HyphaRayAppManager pid=2712) Extension modules: msgpack._cmsgpack, psutil._psutil_linux, psutil._psutil_posix, setproctitle, yaml._yaml, _brotli, charset_normalizer.md, uvloop.loop, ray._raylet, pvectorc, grpc._cython.cygrpc, numpy.core._multiarray_umath, numpy.core._multiarray_tests, numpy.linalg._umath_linalg, numpy.fft._pocketfft_internal, numpy.random._common, numpy.random.bit_generator, numpy.random._bounded_integers, numpy.random._mt19937, numpy.random.mtrand, numpy.random._philox, numpy.random._pcg64, numpy.random._sfc64, numpy.random._generator, pandas._libs.tslibs.np_datetime, pandas._libs.tslibs.dtypes, pandas._libs.tslibs.base, pandas._libs.tslibs.nattype, pandas._libs.tslibs.timezones, pandas._libs.tslibs.tzconversion, pandas._libs.tslibs.ccalendar, pandas._libs.tslibs.fields, pandas._libs.tslibs.timedeltas, pandas._libs.tslibs.timestamps, pandas._libs.properties, pandas._libs.tslibs.offsets, pandas._libs.tslibs.parsing, pandas._libs.tslibs.conversion, pandas._libs.tslibs.period, pandas._libs.tslibs.vectorized, pandas._libs.ops_dispatch, pandas._libs.missing, pandas._libs.hashtable, pandas._libs.algos, pandas._libs.interval, pandas._libs.tslib, pandas._libs.lib, pandas._libs.hashing, pyarrow.lib, pyarrow._hdfsio, pandas._libs.ops, pyarrow._compute, pandas._libs.arrays, pandas._libs.index, pandas._libs.join, pandas._libs.sparse, pandas._libs.reduction, pandas._libs.indexing, pandas._libs.internals, pandas._libs.writers, pandas._libs.window.aggregations, pandas._libs.window.indexers, pandas._libs.reshape, pandas._libs.tslibs.strptime, pandas._libs.groupby, pandas._libs.testing, pandas._libs.parsers, pandas._libs.json, pyarrow._json (total: 69)
(ServeController pid=2630) ERROR 2024-08-31 14:46:04,832 controller 2630 deployment_state.py:656 - Exception when allocating Replica(id='e7zors3c', deployment='HyphaRayAppManager', app='default'):
(ServeController pid=2630) Traceback (most recent call last):
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/deployment_state.py", line 641, in check_ready
(ServeController pid=2630)     ) = ray.get(self._allocated_obj_ref)
(ServeController pid=2630)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/auto_init_hook.py", line 21, in auto_init_wrapper
(ServeController pid=2630)     return fn(*args, **kwargs)
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/client_mode_hook.py", line 103, in wrapper
(ServeController pid=2630)     return func(*args, **kwargs)
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 2613, in get
(ServeController pid=2630)     values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
(ServeController pid=2630)                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 863, in get_objects
(ServeController pid=2630)     raise value
(ServeController pid=2630) ray.exceptions.ActorDiedError: The actor died because of an error raised in its creation task, ray::SERVE_REPLICA::default#HyphaRayAppManager#e7zors3c:ServeReplica:default:HyphaRayAppManager.__init__() (pid=2712, ip=10.42.5.206, actor_id=cfc0984b7cc4904e0f1e32e105000000, repr=<ray.serve._private.replica.ServeReplica:default:HyphaRayAppManager object at 0x7f0adb21f490>)
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 449, in result
(ServeController pid=2630)     return self.__get_result()
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
(ServeController pid=2630)     raise self._exception
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 266, in __init__
(ServeController pid=2630)     deployment_def = cloudpickle.loads(serialized_deployment_def)
(ServeController pid=2630)                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630) ModuleNotFoundError: No module named 'hypha_rpc'
(ServeController pid=2630) Traceback (most recent call last):
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/deployment_state.py", line 641, in check_ready
(ServeController pid=2630)     ) = ray.get(self._allocated_obj_ref)
(ServeController pid=2630)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/auto_init_hook.py", line 21, in auto_init_wrapper
(ServeController pid=2630)     return fn(*args, **kwargs)
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/client_mode_hook.py", line 103, in wrapper
(ServeController pid=2630)     return func(*args, **kwargs)
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 2613, in get
(ServeController pid=2630)     values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
(ServeController pid=2630)                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 863, in get_objects
(ServeController pid=2630)     raise value
(ServeController pid=2630) ray.exceptions.ActorDiedError: The actor died because of an error raised in its creation task, ray::SERVE_REPLICA::default#HyphaRayAppManager#e7zors3c:ServeReplica:default:HyphaRayAppManager.__init__() (pid=2712, ip=10.42.5.206, actor_id=cfc0984b7cc4904e0f1e32e105000000, repr=<ray.serve._private.replica.ServeReplica:default:HyphaRayAppManager object at 0x7f0adb21f490>)
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 449, in result
(ServeController pid=2630)     return self.__get_result()
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
(ServeController pid=2630)     raise self._exception
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 266, in __init__
(ServeController pid=2630)     deployment_def = cloudpickle.loads(serialized_deployment_def)
(ServeController pid=2630)                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630) ModuleNotFoundError: No module named 'hypha_rpc'
(ServeController pid=2630) INFO 2024-08-31 14:46:04,835 controller 2630 deployment_state.py:2182 - Replica(id='e7zors3c', deployment='HyphaRayAppManager', app='default') is stopped.
(ServeController pid=2630) INFO 2024-08-31 14:46:04,836 controller 2630 deployment_state.py:1844 - Adding 1 replica to Deployment(name='HyphaRayAppManager', app='default').
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) Exception raised in creation task: The actor died because of an error raised in its creation task, ray::SERVE_REPLICA::default#HyphaRayAppManager#j1xovdel:ServeReplica:default:HyphaRayAppManager.__init__() (pid=712, ip=10.42.6.166, actor_id=9d9b982f4a90c6a6257c811705000000, repr=<ray.serve._private.replica.ServeReplica:default:HyphaRayAppManager object at 0x7f8410a47990>)
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 449, in result
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     return self.__get_result()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)            ^^^^^^^^^^^^^^^^^^^
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     raise self._exception
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 266, in __init__
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     deployment_def = cloudpickle.loads(serialized_deployment_def)
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ModuleNotFoundError: No module named 'hypha_rpc'
(ServeController pid=2630) ERROR 2024-08-31 14:46:06,455 controller 2630 deployment_state.py:656 - Exception when allocating Replica(id='j1xovdel', deployment='HyphaRayAppManager', app='default'):
(ServeController pid=2630) Traceback (most recent call last):
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/deployment_state.py", line 641, in check_ready
(ServeController pid=2630)     ) = ray.get(self._allocated_obj_ref)
(ServeController pid=2630)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/auto_init_hook.py", line 21, in auto_init_wrapper
(ServeController pid=2630)     return fn(*args, **kwargs)
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/client_mode_hook.py", line 103, in wrapper
(ServeController pid=2630)     return func(*args, **kwargs)
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 2613, in get
(ServeController pid=2630)     values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
(ServeController pid=2630)                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 863, in get_objects
(ServeController pid=2630)     raise value
(ServeController pid=2630) ray.exceptions.ActorDiedError: The actor died because of an error raised in its creation task, ray::SERVE_REPLICA::default#HyphaRayAppManager#j1xovdel:ServeReplica:default:HyphaRayAppManager.__init__() (pid=712, ip=10.42.6.166, actor_id=9d9b982f4a90c6a6257c811705000000, repr=<ray.serve._private.replica.ServeReplica:default:HyphaRayAppManager object at 0x7f8410a47990>)
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 449, in result
(ServeController pid=2630)     return self.__get_result()
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
(ServeController pid=2630)     raise self._exception
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 266, in __init__
(ServeController pid=2630)     deployment_def = cloudpickle.loads(serialized_deployment_def)
(ServeController pid=2630)                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630) ModuleNotFoundError: No module named 'hypha_rpc'
(ServeController pid=2630) Traceback (most recent call last):
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/deployment_state.py", line 641, in check_ready
(ServeController pid=2630)     ) = ray.get(self._allocated_obj_ref)
(ServeController pid=2630)         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/auto_init_hook.py", line 21, in auto_init_wrapper
(ServeController pid=2630)     return fn(*args, **kwargs)
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/client_mode_hook.py", line 103, in wrapper
(ServeController pid=2630)     return func(*args, **kwargs)
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 2613, in get
(ServeController pid=2630)     values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
(ServeController pid=2630)                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 863, in get_objects
(ServeController pid=2630)     raise value
(ServeController pid=2630) ray.exceptions.ActorDiedError: The actor died because of an error raised in its creation task, ray::SERVE_REPLICA::default#HyphaRayAppManager#j1xovdel:ServeReplica:default:HyphaRayAppManager.__init__() (pid=712, ip=10.42.6.166, actor_id=9d9b982f4a90c6a6257c811705000000, repr=<ray.serve._private.replica.ServeReplica:default:HyphaRayAppManager object at 0x7f8410a47990>)
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 449, in result
(ServeController pid=2630)     return self.__get_result()
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
(ServeController pid=2630)     raise self._exception
(ServeController pid=2630)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 266, in __init__
(ServeController pid=2630)     deployment_def = cloudpickle.loads(serialized_deployment_def)
(ServeController pid=2630)                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeController pid=2630) ModuleNotFoundError: No module named 'hypha_rpc'
(ServeController pid=2630) INFO 2024-08-31 14:46:06,461 controller 2630 deployment_state.py:2182 - Replica(id='j1xovdel', deployment='HyphaRayAppManager', app='default') is stopped.
(ServeController pid=2630) ERROR 2024-08-31 14:46:06,463 controller 2630 application_state.py:770 - The deployments ['HyphaRayAppManager'] are UNHEALTHY.
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,578 E 712 712] logging.cc:115: Stack trace: 
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)  /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x103216a) [0x7f857911716a] ray::operator<<()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x10351b2) [0x7f857911a1b2] ray::TerminateHandler()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/bin/../lib/libstdc++.so.6(+0xb135a) [0x7f8577f7035a] __cxxabiv1::__terminate()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/bin/../lib/libstdc++.so.6(+0xb13c5) [0x7f8577f703c5]
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x7f7990) [0x7f85788dc990] std::thread::_State_impl<>::~_State_impl()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x65b34a) [0x7f857874034a] std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x7e0902) [0x7f85788c5902] std::_Sp_counted_ptr_inplace<>::_M_dispose()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x65b34a) [0x7f857874034a] std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x7166f2) [0x7f85787fb6f2] std::default_delete<>::operator()()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(_ZN3ray4core10CoreWorkerD1Ev+0xfd) [0x7f8578873a8d] ray::core::CoreWorker::~CoreWorker()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x65b34a) [0x7f857874034a] std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(_ZN3ray4core21CoreWorkerProcessImpl26RunWorkerTaskExecutionLoopEv+0x124) [0x7f85788aa534] ray::core::CoreWorkerProcessImpl::RunWorkerTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(_ZN3ray4core17CoreWorkerProcess20RunTaskExecutionLoopEv+0x1d) [0x7f85788aa69d] ray::core::CoreWorkerProcess::RunTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x5c8937) [0x7f85786ad937] __pyx_pw_3ray_7_raylet_10CoreWorker_7run_task_loop()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager() [0x539080] method_vectorcall_NOARGS
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager(PyObject_Vectorcall+0x31) [0x51e6a1] PyObject_Vectorcall
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager(_PyEval_EvalFrameDefault+0x6a7) [0x5116e7] _PyEval_EvalFrameDefault
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager() [0x5cbeda] _PyEval_Vector
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager(PyEval_EvalCode+0x9f) [0x5cb5af] PyEval_EvalCode
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager() [0x5ec6a7] run_eval_code_obj
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager() [0x5e8240] run_mod
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager() [0x5fd192] pyrun_file
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager(_PyRun_SimpleFileObject+0x19f) [0x5fc55f] _PyRun_SimpleFileObject
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager(_PyRun_AnyFileObject+0x43) [0x5fc283] _PyRun_AnyFileObject
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager(Py_RunMain+0x2ee) [0x5f6efe] Py_RunMain
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager(Py_BytesMain+0x39) [0x5bbc79] Py_BytesMain
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) /usr/lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf3) [0x7f8579e1e083] __libc_start_main
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) ray::ServeReplica:default:HyphaRayAppManager() [0x5bbac3]
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) 
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) *** SIGABRT received at time=1725140766 on cpu 8 ***
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) PC: @     0x7f8579e3d00b  (unknown)  raise
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @     0x7f857a15a420  (unknown)  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @     0x7f8577f7035a         80  __cxxabiv1::__terminate()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @     0x7f857874034a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @     0x7f85788c5902         96  std::_Sp_counted_ptr_inplace<>::_M_dispose()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @     0x7f857874034a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @     0x7f85787fb6f2        144  std::default_delete<>::operator()()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @     0x7f8578873a8d       1168  ray::core::CoreWorker::~CoreWorker()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @     0x7f857874034a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @     0x7f85788aa534       1152  ray::core::CoreWorkerProcessImpl::RunWorkerTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @     0x7f85788aa69d         32  ray::core::CoreWorkerProcess::RunTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @     0x7f85786ad937         32  __pyx_pw_3ray_7_raylet_10CoreWorker_7run_task_loop()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @           0x539080  (unknown)  method_vectorcall_NOARGS
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)     @           0x87b120  (unknown)  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,628 E 712 712] logging.cc:343: *** SIGABRT received at time=1725140766 on cpu 8 ***
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,628 E 712 712] logging.cc:343: PC: @     0x7f8579e3d00b  (unknown)  raise
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @     0x7f857a15a420  (unknown)  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @     0x7f8577f7035a         80  __cxxabiv1::__terminate()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @     0x7f857874034a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @     0x7f85788c5902         96  std::_Sp_counted_ptr_inplace<>::_M_dispose()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @     0x7f857874034a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @     0x7f85787fb6f2        144  std::default_delete<>::operator()()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @     0x7f8578873a8d       1168  ray::core::CoreWorker::~CoreWorker()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @     0x7f857874034a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @     0x7f85788aa534       1152  ray::core::CoreWorkerProcessImpl::RunWorkerTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @     0x7f85788aa69d         32  ray::core::CoreWorkerProcess::RunTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @     0x7f85786ad937         32  __pyx_pw_3ray_7_raylet_10CoreWorker_7run_task_loop()
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,630 E 712 712] logging.cc:343:     @           0x539080  (unknown)  method_vectorcall_NOARGS
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) [2024-08-31 14:46:06,632 E 712 712] logging.cc:343:     @           0x87b120  (unknown)  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) Fatal Python error: Aborted
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) 
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) Stack (most recent call first):
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 876 in main_loop
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/workers/default_worker.py", line 289 in <module>
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) 
(ServeReplica:default:HyphaRayAppManager pid=712, ip=10.42.6.166) Extension modules: msgpack._cmsgpack, psutil._psutil_linux, psutil._psutil_posix, setproctitle, yaml._yaml, _brotli, charset_normalizer.md, uvloop.loop, ray._raylet, pvectorc, ujson, grpc._cython.cygrpc, numpy.core._multiarray_umath, numpy.core._multiarray_tests, numpy.linalg._umath_linalg, numpy.fft._pocketfft_internal, numpy.random._common, numpy.random.bit_generator, numpy.random._bounded_integers, numpy.random._mt19937, numpy.random.mtrand, numpy.random._philox, numpy.random._pcg64, numpy.random._sfc64, numpy.random._generator, pandas._libs.tslibs.np_datetime, pandas._libs.tslibs.dtypes, pandas._libs.tslibs.base, pandas._libs.tslibs.nattype, pandas._libs.tslibs.timezones, pandas._libs.tslibs.tzconversion, pandas._libs.tslibs.ccalendar, pandas._libs.tslibs.fields, pandas._libs.tslibs.timedeltas, pandas._libs.tslibs.timestamps, pandas._libs.properties, pandas._libs.tslibs.offsets, pandas._libs.tslibs.parsing, pandas._libs.tslibs.conversion, pandas._libs.tslibs.period, pandas._libs.tslibs.vectorized, pandas._libs.ops_dispatch, pandas._libs.missing, pandas._libs.hashtable, pandas._libs.algos, pandas._libs.interval, pandas._libs.tslib, pandas._libs.lib, pandas._libs.hashing, pyarrow.lib, pyarrow._hdfsio, pandas._libs.ops, numexpr.interpreter, pyarrow._compute, pandas._libs.arrays, pandas._libs.index, pandas._libs.join, pandas._libs.sparse, pandas._libs.reduction, pandas._libs.indexing, pandas._libs.internals, pandas._libs.writers, pandas._libs.window.aggregations, pandas._libs.window.indexers, pandas._libs.reshape, pandas._libs.tslibs.strptime, pandas._libs.groupby, pandas._libs.testing, pandas._libs.parsers, pandas._libs.json, pyarrow._json (total: 71)
Traceback (most recent call last):
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/scripts.py", line 548, in run
    serve.run(app, blocking=should_block, name=name, route_prefix=route_prefix)
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/api.py", line 578, in run
    handle = _run(
             ^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/api.py", line 529, in _run
    client.deploy_application(
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/client.py", line 45, in check
    return f(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/client.py", line 280, in deploy_application
    self._wait_for_application_running(name)
  File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/client.py", line 228, in _wait_for_application_running
    raise RuntimeError(
RuntimeError: Deploying application default failed: The deployments ['HyphaRayAppManager'] are UNHEALTHY.
2024-08-31 14:46:06,884 ERR scripts.py:591 -- Received unexpected error, see console logs for more details. Shutting down...
(ServeController pid=2630) INFO 2024-08-31 14:46:06,891 controller 2630 deployment_state.py:1844 - Adding 1 replica to Deployment(name='HyphaRayAppManager', app='default').
(ServeController pid=2630) INFO 2024-08-31 14:46:07,027 controller 2630 deployment_state.py:1860 - Removing 1 replica from Deployment(name='HyphaRayAppManager', app='default').
(ServeReplica:default:HyphaRayAppManager pid=2786) Exception raised in creation task: The actor died because of an error raised in its creation task, ray::SERVE_REPLICA::default#HyphaRayAppManager#6f9fpp9q:ServeReplica:default:HyphaRayAppManager.__init__() (pid=2786, ip=10.42.5.206, actor_id=98018efb2d49c97b2ead4a0c05000000, repr=<ray.serve._private.replica.ServeReplica:default:HyphaRayAppManager object at 0x7f8e28190e10>)
(ServeReplica:default:HyphaRayAppManager pid=2786)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 456, in result
(ServeReplica:default:HyphaRayAppManager pid=2786)     return self.__get_result()
(ServeReplica:default:HyphaRayAppManager pid=2786)            ^^^^^^^^^^^^^^^^^^^
(ServeReplica:default:HyphaRayAppManager pid=2786)   File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
(ServeReplica:default:HyphaRayAppManager pid=2786)     raise self._exception
(ServeReplica:default:HyphaRayAppManager pid=2786)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeReplica:default:HyphaRayAppManager pid=2786)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/serve/_private/replica.py", line 266, in __init__
(ServeReplica:default:HyphaRayAppManager pid=2786)     deployment_def = cloudpickle.loads(serialized_deployment_def)
(ServeReplica:default:HyphaRayAppManager pid=2786)                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ServeReplica:default:HyphaRayAppManager pid=2786) ModuleNotFoundError: No module named 'hypha_rpc'
(ServeController pid=2630) INFO 2024-08-31 14:46:08,422 controller 2630 deployment_state.py:2182 - Replica(id='6f9fpp9q', deployment='HyphaRayAppManager', app='default') is stopped.
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,469 E 2786 2786] logging.cc:115: Stack trace: 
(ServeReplica:default:HyphaRayAppManager pid=2786)  /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x103216a) [0x7f8e50a5016a] ray::operator<<()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x10351b2) [0x7f8e50a531b2] ray::TerminateHandler()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/bin/../lib/libstdc++.so.6(+0xb135a) [0x7f8e4f8b135a] __cxxabiv1::__terminate()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/bin/../lib/libstdc++.so.6(+0xb13c5) [0x7f8e4f8b13c5]
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x7f7990) [0x7f8e50215990] std::thread::_State_impl<>::~_State_impl()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x65b34a) [0x7f8e5007934a] std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x7e0902) [0x7f8e501fe902] std::_Sp_counted_ptr_inplace<>::_M_dispose()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x65b34a) [0x7f8e5007934a] std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x7166f2) [0x7f8e501346f2] std::default_delete<>::operator()()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(_ZN3ray4core10CoreWorkerD1Ev+0xfd) [0x7f8e501aca8d] ray::core::CoreWorker::~CoreWorker()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x65b34a) [0x7f8e5007934a] std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(_ZN3ray4core21CoreWorkerProcessImpl26RunWorkerTaskExecutionLoopEv+0x124) [0x7f8e501e3534] ray::core::CoreWorkerProcessImpl::RunWorkerTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(_ZN3ray4core17CoreWorkerProcess20RunTaskExecutionLoopEv+0x1d) [0x7f8e501e369d] ray::core::CoreWorkerProcess::RunTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2786) /home/ray/anaconda3/lib/python3.11/site-packages/ray/_raylet.so(+0x5c8937) [0x7f8e4ffe6937] __pyx_pw_3ray_7_raylet_10CoreWorker_7run_task_loop()
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager() [0x539080] method_vectorcall_NOARGS
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager(PyObject_Vectorcall+0x31) [0x51e6a1] PyObject_Vectorcall
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager(_PyEval_EvalFrameDefault+0x6a7) [0x5116e7] _PyEval_EvalFrameDefault
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager() [0x5cbeda] _PyEval_Vector
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager(PyEval_EvalCode+0x9f) [0x5cb5af] PyEval_EvalCode
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager() [0x5ec6a7] run_eval_code_obj
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager() [0x5e8240] run_mod
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager() [0x5fd192] pyrun_file
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager(_PyRun_SimpleFileObject+0x19f) [0x5fc55f] _PyRun_SimpleFileObject
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager(_PyRun_AnyFileObject+0x43) [0x5fc283] _PyRun_AnyFileObject
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager(Py_RunMain+0x2ee) [0x5f6efe] Py_RunMain
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager(Py_BytesMain+0x39) [0x5bbc79] Py_BytesMain
(ServeReplica:default:HyphaRayAppManager pid=2786) /lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf3) [0x7f8e5175e083] __libc_start_main
(ServeReplica:default:HyphaRayAppManager pid=2786) ray::ServeReplica:default:HyphaRayAppManager() [0x5bbac3]
(ServeReplica:default:HyphaRayAppManager pid=2786) 
(ServeReplica:default:HyphaRayAppManager pid=2786) *** SIGABRT received at time=1725140768 on cpu 24 ***
(ServeReplica:default:HyphaRayAppManager pid=2786) PC: @     0x7f8e5177d00b  (unknown)  raise
(ServeReplica:default:HyphaRayAppManager pid=2786)     @     0x7f8e51a9a420  235815216  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=2786)     @     0x7f8e4f8b135a         80  __cxxabiv1::__terminate()
(ServeReplica:default:HyphaRayAppManager pid=2786)     @     0x7f8e5007934a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2786)     @     0x7f8e501fe902         96  std::_Sp_counted_ptr_inplace<>::_M_dispose()
(ServeReplica:default:HyphaRayAppManager pid=2786)     @     0x7f8e5007934a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2786)     @     0x7f8e501346f2        144  std::default_delete<>::operator()()
(ServeReplica:default:HyphaRayAppManager pid=2786)     @     0x7f8e501aca8d       1168  ray::core::CoreWorker::~CoreWorker()
(ServeReplica:default:HyphaRayAppManager pid=2786)     @     0x7f8e5007934a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2786)     @     0x7f8e501e3534       1152  ray::core::CoreWorkerProcessImpl::RunWorkerTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2786)     @     0x7f8e501e369d         32  ray::core::CoreWorkerProcess::RunTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2786)     @     0x7f8e4ffe6937         32  __pyx_pw_3ray_7_raylet_10CoreWorker_7run_task_loop()
(ServeReplica:default:HyphaRayAppManager pid=2786)     @           0x539080  (unknown)  method_vectorcall_NOARGS
(ServeReplica:default:HyphaRayAppManager pid=2786)     @           0x87b120  (unknown)  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343: *** SIGABRT received at time=1725140768 on cpu 24 ***
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343: PC: @     0x7f8e5177d00b  (unknown)  raise
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @     0x7f8e51a9a420  235815216  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @     0x7f8e4f8b135a         80  __cxxabiv1::__terminate()
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @     0x7f8e5007934a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @     0x7f8e501fe902         96  std::_Sp_counted_ptr_inplace<>::_M_dispose()
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @     0x7f8e5007934a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @     0x7f8e501346f2        144  std::default_delete<>::operator()()
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @     0x7f8e501aca8d       1168  ray::core::CoreWorker::~CoreWorker()
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @     0x7f8e5007934a         32  std::_Sp_counted_base<>::_M_release()
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @     0x7f8e501e3534       1152  ray::core::CoreWorkerProcessImpl::RunWorkerTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @     0x7f8e501e369d         32  ray::core::CoreWorkerProcess::RunTaskExecutionLoop()
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @     0x7f8e4ffe6937         32  __pyx_pw_3ray_7_raylet_10CoreWorker_7run_task_loop()
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,481 E 2786 2786] logging.cc:343:     @           0x539080  (unknown)  method_vectorcall_NOARGS
(ServeReplica:default:HyphaRayAppManager pid=2786) [2024-08-31 14:46:08,482 E 2786 2786] logging.cc:343:     @           0x87b120  (unknown)  (unknown)
(ServeReplica:default:HyphaRayAppManager pid=2786) Fatal Python error: Aborted
(ServeReplica:default:HyphaRayAppManager pid=2786) 
(ServeReplica:default:HyphaRayAppManager pid=2786) Stack (most recent call first):
(ServeReplica:default:HyphaRayAppManager pid=2786)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/worker.py", line 876 in main_loop
(ServeReplica:default:HyphaRayAppManager pid=2786)   File "/home/ray/anaconda3/lib/python3.11/site-packages/ray/_private/workers/default_worker.py", line 289 in <module>
(ServeReplica:default:HyphaRayAppManager pid=2786) 
(ServeReplica:default:HyphaRayAppManager pid=2786) Extension modules: msgpack._cmsgpack, psutil._psutil_linux, psutil._psutil_posix, setproctitle, yaml._yaml, _brotli, charset_normalizer.md, uvloop.loop, ray._raylet, pvectorc, grpc._cython.cygrpc, numpy.core._multiarray_umath, numpy.core._multiarray_tests, numpy.linalg._umath_linalg, numpy.fft._pocketfft_internal, numpy.random._common, numpy.random.bit_generator, numpy.random._bounded_integers, numpy.random._mt19937, numpy.random.mtrand, numpy.random._philox, numpy.random._pcg64, numpy.random._sfc64, numpy.random._generator, pandas._libs.tslibs.np_datetime, pandas._libs.tslibs.dtypes, pandas._libs.tslibs.base, pandas._libs.tslibs.nattype, pandas._libs.tslibs.timezones, pandas._libs.tslibs.tzconversion, pandas._libs.tslibs.ccalendar, pandas._libs.tslibs.fields, pandas._libs.tslibs.timedeltas, pandas._libs.tslibs.timestamps, pandas._libs.properties, pandas._libs.tslibs.offsets, pandas._libs.tslibs.parsing, pandas._libs.tslibs.conversion, pandas._libs.tslibs.period, pandas._libs.tslibs.vectorized, pandas._libs.ops_dispatch, pandas._libs.missing, pandas._libs.hashtable, pandas._libs.algos, pandas._libs.interval, pandas._libs.tslib, pandas._libs.lib, pandas._libs.hashing, pyarrow.lib, pyarrow._hdfsio, pandas._libs.ops, pyarrow._compute, pandas._libs.arrays, pandas._libs.index, pandas._libs.join, pandas._libs.sparse, pandas._libs.reduction, pandas._libs.indexing, pandas._libs.internals, pandas._libs.writers, pandas._libs.window.aggregations, pandas._libs.window.indexers, pandas._libs.reshape, pandas._libs.tslibs.strptime, pandas._libs.groupby, pandas._libs.testing, pandas._libs.parsers, pandas._libs.json, pyarrow._json (total: 69)
(base) I have no name!@ray-hypha-service-59bcd866c6-74tq5:/app$ pip install --target=/tmp/pip -U https://github.com/bioimage-io/bioengine/archive/refs/heads/main.zip
WARNING: The directory '/home/ray/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Collecting https://github.com/bioimage-io/bioengine/archive/refs/heads/main.zip
  Downloading https://github.com/bioimage-io/bioengine/archive/refs/heads/main.zip
     | 7.4 MB 13.2 MB/s 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting hypha>=0.20.31 (from hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading hypha-0.20.32-py3-none-any.whl.metadata (4.7 kB)
Collecting hypha-rpc (from bioimageio.engine==0.1.1)
  Downloading hypha_rpc-0.20.32-py3-none-any.whl.metadata (649 bytes)
Collecting PyYAML (from bioimageio.engine==0.1.1)
  Downloading PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.1 kB)
Collecting hypha-launcher>=0.1.3 (from bioimageio.engine==0.1.1)
  Downloading hypha_launcher-0.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting pyotritonclient (from bioimageio.engine==0.1.1)
  Downloading pyotritonclient-0.2.6-py3-none-any.whl.metadata (6.4 kB)
Collecting simpervisor (from bioimageio.engine==0.1.1)
  Downloading simpervisor-1.0.0-py3-none-any.whl.metadata (4.3 kB)
Collecting aiofiles (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading aiofiles-24.1.0-py3-none-any.whl.metadata (10 kB)
Collecting fastapi<=0.106.0,>=0.70.0 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading fastapi-0.106.0-py3-none-any.whl.metadata (24 kB)
Collecting msgpack>=1.0.2 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading msgpack-1.0.8-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.1 kB)
Collecting numpy (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading numpy-2.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.9/60.9 kB 211.1 MB/s eta 0:00:00
Collecting pydantic>=2.6.1 (from pydantic[email]>=2.6.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading pydantic-2.8.2-py3-none-any.whl.metadata (125 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 125.2/125.2 kB 158.8 MB/s eta 0:00:00
Collecting typing-extensions>=3.7.4.3 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Collecting jinja2>=3 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
Collecting lxml (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading lxml-5.3.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (3.8 kB)
Collecting python-dotenv>=0.19.0 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)
Collecting python-jose>=3.3.0 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading python_jose-3.3.0-py2.py3-none-any.whl.metadata (5.4 kB)
Collecting python-multipart>=0.0.6 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading python_multipart-0.0.9-py3-none-any.whl.metadata (2.5 kB)
Collecting fakeredis>=2.14.1 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading fakeredis-2.24.1-py3-none-any.whl.metadata (3.8 kB)
Collecting shortuuid>=1.0.1 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading shortuuid-1.0.13-py3-none-any.whl.metadata (5.8 kB)
Collecting uvicorn>=0.23.2 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading uvicorn-0.30.6-py3-none-any.whl.metadata (6.6 kB)
Collecting httpx>=0.21.1 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading httpx-0.27.2-py3-none-any.whl.metadata (7.1 kB)
Collecting friendlywords>=1.1.3 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading friendlywords-1.1.3-py3-none-any.whl.metadata (3.4 kB)
^CERROR: Operation cancelled by user
^CTraceback (most recent call last):
  File "/home/ray/anaconda3/bin/pip", line 11, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/cli/main.py", line 79, in main
    return command.main(cmd_args)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/cli/base_command.py", line 101, in main
    return self._main(args)
           ^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/cli/base_command.py", line 236, in _main
    self.handle_pip_version_check(options)
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/cli/req_command.py", line 188, in handle_pip_version_check
    pip_self_version_check(session, options)
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/self_outdated_check.py", line 227, in pip_self_version_check
    upgrade_prompt = _self_version_check_logic(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/self_outdated_check.py", line 200, in _self_version_check_logic
    pip_installed_by_pip = was_installed_by_pip("pip")
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/self_outdated_check.py", line 149, in was_installed_by_pip
    dist = get_default_environment().get_distribution(pkg)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_envs.py", line 189, in get_distribution
    return next(matches, None)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_envs.py", line 184, in <genexpr>
    matches = (
              ^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/metadata/base.py", line 626, in iter_all_distributions
    for dist in self._iter_distributions():
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_envs.py", line 176, in _iter_distributions
    yield from finder.find(location)
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_envs.py", line 79, in find
    for dist, info_location in self._find_impl(location):
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_envs.py", line 64, in _find_impl
    raw_name = get_dist_name(dist)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/site-packages/pip/_internal/metadata/importlib/_compat.py", line 52, in get_dist_name
    name = cast(Any, dist).name
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/importlib/metadata/__init__.py", line 622, in name
    return self.metadata['Name']
           ^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/importlib/metadata/__init__.py", line 610, in metadata
    self.read_text('METADATA')
  File "/home/ray/anaconda3/lib/python3.11/importlib/metadata/__init__.py", line 939, in read_text
    return self._path.joinpath(filename).read_text(encoding='utf-8')
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/pathlib.py", line 1058, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ray/anaconda3/lib/python3.11/pathlib.py", line 1044, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen codecs>", line 309, in __init__
KeyboardInterrupt

(base) I have no name!@ray-hypha-service-59bcd866c6-74tq5:/app$ pip install --target=/tmp/pip -U https://github.com/bioimage-io/bioengine/archive/refs/heads/main.zip
WARNING: The directory '/home/ray/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Collecting https://github.com/bioimage-io/bioengine/archive/refs/heads/main.zip
  Downloading https://github.com/bioimage-io/bioengine/archive/refs/heads/main.zip
     | 7.4 MB 8.5 MB/s 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting hypha>=0.20.31 (from hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading hypha-0.20.32-py3-none-any.whl.metadata (4.7 kB)
Collecting hypha-rpc (from bioimageio.engine==0.1.1)
  Downloading hypha_rpc-0.20.32-py3-none-any.whl.metadata (649 bytes)
Collecting PyYAML (from bioimageio.engine==0.1.1)
  Downloading PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.1 kB)
Collecting hypha-launcher>=0.1.3 (from bioimageio.engine==0.1.1)
  Downloading hypha_launcher-0.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting pyotritonclient (from bioimageio.engine==0.1.1)
  Downloading pyotritonclient-0.2.6-py3-none-any.whl.metadata (6.4 kB)
Collecting simpervisor (from bioimageio.engine==0.1.1)
  Downloading simpervisor-1.0.0-py3-none-any.whl.metadata (4.3 kB)
Collecting aiofiles (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading aiofiles-24.1.0-py3-none-any.whl.metadata (10 kB)
Collecting fastapi<=0.106.0,>=0.70.0 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading fastapi-0.106.0-py3-none-any.whl.metadata (24 kB)
Collecting msgpack>=1.0.2 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading msgpack-1.0.8-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.1 kB)
Collecting numpy (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading numpy-2.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (60 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.9/60.9 kB 187.8 MB/s eta 0:00:00
Collecting pydantic>=2.6.1 (from pydantic[email]>=2.6.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading pydantic-2.8.2-py3-none-any.whl.metadata (125 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 125.2/125.2 kB 90.2 MB/s eta 0:00:00
Collecting typing-extensions>=3.7.4.3 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Collecting jinja2>=3 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
Collecting lxml (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading lxml-5.3.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (3.8 kB)
Collecting python-dotenv>=0.19.0 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)
Collecting python-jose>=3.3.0 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading python_jose-3.3.0-py2.py3-none-any.whl.metadata (5.4 kB)
Collecting python-multipart>=0.0.6 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading python_multipart-0.0.9-py3-none-any.whl.metadata (2.5 kB)
Collecting fakeredis>=2.14.1 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading fakeredis-2.24.1-py3-none-any.whl.metadata (3.8 kB)
Collecting shortuuid>=1.0.1 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading shortuuid-1.0.13-py3-none-any.whl.metadata (5.8 kB)
Collecting uvicorn>=0.23.2 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading uvicorn-0.30.6-py3-none-any.whl.metadata (6.6 kB)
Collecting httpx>=0.21.1 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading httpx-0.27.2-py3-none-any.whl.metadata (7.1 kB)
Collecting friendlywords>=1.1.3 (from hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading friendlywords-1.1.3-py3-none-any.whl.metadata (3.4 kB)
Collecting aiohttp (from hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading aiohttp-3.10.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.5 kB)
Collecting requests (from hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
Collecting tqdm (from hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading tqdm-4.66.5-py3-none-any.whl.metadata (57 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.6/57.6 kB 198.1 MB/s eta 0:00:00
Collecting fire (from hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading fire-0.6.0.tar.gz (88 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 88.4/88.4 kB 293.8 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Collecting loguru (from hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading loguru-0.7.2-py3-none-any.whl.metadata (23 kB)
Collecting executor-engine (from hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading executor_engine-0.2.5-py3-none-any.whl.metadata (2.0 kB)
Collecting imjoy-rpc (from hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading imjoy_rpc-0.5.59-py3-none-any.whl.metadata (1.1 kB)
Collecting psutil (from hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading psutil-6.0.0-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (21 kB)
Collecting munch (from hypha-rpc->bioimageio.engine==0.1.1)
  Downloading munch-4.0.0-py2.py3-none-any.whl.metadata (5.9 kB)
Collecting websockets (from hypha-rpc->bioimageio.engine==0.1.1)
  Downloading websockets-13.0.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.7 kB)
Collecting aiobotocore>=2.1.0 (from hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading aiobotocore-2.14.0-py3-none-any.whl.metadata (23 kB)
Collecting six (from pyotritonclient->bioimageio.engine==0.1.1)
  Downloading six-1.16.0-py2.py3-none-any.whl.metadata (1.8 kB)
Collecting python-rapidjson>=0.9.1 (from pyotritonclient->bioimageio.engine==0.1.1)
  Downloading python_rapidjson-1.20-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (22 kB)
Collecting botocore<1.35.8,>=1.35.0 (from aiobotocore>=2.1.0->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading botocore-1.35.7-py3-none-any.whl.metadata (5.7 kB)
Collecting wrapt<2.0.0,>=1.10.10 (from aiobotocore>=2.1.0->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading wrapt-1.16.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
Collecting aioitertools<1.0.0,>=0.5.1 (from aiobotocore>=2.1.0->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading aioitertools-0.11.0-py3-none-any.whl.metadata (3.3 kB)
Collecting aiohappyeyeballs>=2.3.0 (from aiohttp->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading aiohappyeyeballs-2.4.0-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.1.2 (from aiohttp->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading aiosignal-1.3.1-py3-none-any.whl.metadata (4.0 kB)
Collecting attrs>=17.3.0 (from aiohttp->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading attrs-24.2.0-py3-none-any.whl.metadata (11 kB)
Collecting frozenlist>=1.1.1 (from aiohttp->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading frozenlist-1.4.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (12 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading multidict-6.0.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.2 kB)
Collecting yarl<2.0,>=1.0 (from aiohttp->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading yarl-1.9.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (38 kB)
Collecting redis>=4 (from fakeredis>=2.14.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading redis-5.0.8-py3-none-any.whl.metadata (9.2 kB)
Collecting sortedcontainers<3,>=2 (from fakeredis>=2.14.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl.metadata (10 kB)
Collecting anyio<4.0.0,>=3.7.1 (from fastapi<=0.106.0,>=0.70.0->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading anyio-3.7.1-py3-none-any.whl.metadata (4.7 kB)
Collecting starlette<0.28.0,>=0.27.0 (from fastapi<=0.106.0,>=0.70.0->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading starlette-0.27.0-py3-none-any.whl.metadata (5.8 kB)
Collecting certifi (from httpx>=0.21.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading certifi-2024.8.30-py3-none-any.whl.metadata (2.2 kB)
Collecting httpcore==1.* (from httpx>=0.21.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading httpcore-1.0.5-py3-none-any.whl.metadata (20 kB)
Collecting idna (from httpx>=0.21.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading idna-3.8-py3-none-any.whl.metadata (9.9 kB)
Collecting sniffio (from httpx>=0.21.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx>=0.21.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)
Collecting MarkupSafe>=2.0 (from jinja2>=3->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading MarkupSafe-2.1.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.0 kB)
Collecting annotated-types>=0.4.0 (from pydantic>=2.6.1->pydantic[email]>=2.6.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.20.1 (from pydantic>=2.6.1->pydantic[email]>=2.6.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading pydantic_core-2.20.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
Collecting email-validator>=2.0.0 (from pydantic[email]>=2.6.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading email_validator-2.2.0-py3-none-any.whl.metadata (25 kB)
Collecting ecdsa!=0.15 (from python-jose>=3.3.0->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading ecdsa-0.19.0-py2.py3-none-any.whl.metadata (29 kB)
Collecting rsa (from python-jose>=3.3.0->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading rsa-4.9-py3-none-any.whl.metadata (4.2 kB)
Collecting pyasn1 (from python-jose>=3.3.0->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading pyasn1-0.6.0-py2.py3-none-any.whl.metadata (8.3 kB)
Collecting click>=7.0 (from uvicorn>=0.23.2->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Collecting cmd2func>=0.1.9 (from executor-engine->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading cmd2func-0.2.1-py3-none-any.whl.metadata (1.4 kB)
Collecting funcdesc>=0.1.2 (from executor-engine->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading funcdesc-0.1.3-py3-none-any.whl.metadata (1.3 kB)
Collecting loky (from executor-engine->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading loky-3.4.1-py3-none-any.whl.metadata (6.4 kB)
Collecting diskcache (from executor-engine->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading diskcache-5.6.3-py3-none-any.whl.metadata (20 kB)
Collecting cloudpickle (from executor-engine->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading cloudpickle-3.0.0-py3-none-any.whl.metadata (7.0 kB)
Collecting termcolor (from fire->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading termcolor-2.4.0-py3-none-any.whl.metadata (6.1 kB)
Collecting charset-normalizer<4,>=2 (from requests->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading charset_normalizer-3.3.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (33 kB)
Collecting urllib3<3,>=1.21.1 (from requests->hypha-launcher>=0.1.3->bioimageio.engine==0.1.1)
  Downloading urllib3-2.2.2-py3-none-any.whl.metadata (6.4 kB)
Collecting jmespath<2.0.0,>=0.7.1 (from botocore<1.35.8,>=1.35.0->aiobotocore>=2.1.0->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading jmespath-1.0.1-py3-none-any.whl.metadata (7.6 kB)
Collecting python-dateutil<3.0.0,>=2.1 (from botocore<1.35.8,>=1.35.0->aiobotocore>=2.1.0->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting dnspython>=2.0.0 (from email-validator>=2.0.0->pydantic[email]>=2.6.1->hypha>=0.20.31->hypha[s3]>=0.20.31->bioimageio.engine==0.1.1)
  Downloading dnspython-2.6.1-py3-none-any.whl.metadata (5.8 kB)
Downloading hypha-0.20.32-py3-none-any.whl (133 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.9/133.9 kB 313.6 MB/s eta 0:00:00
Downloading hypha_launcher-0.1.3-py3-none-any.whl (15 kB)
Downloading hypha_rpc-0.20.32-py3-none-any.whl (40 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.4/40.4 kB 231.6 MB/s eta 0:00:00
Downloading pyotritonclient-0.2.6-py3-none-any.whl (23 kB)
Downloading PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (762 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 763.0/763.0 kB 221.8 MB/s eta 0:00:00
Downloading simpervisor-1.0.0-py3-none-any.whl (8.3 kB)
Downloading aiobotocore-2.14.0-py3-none-any.whl (77 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.3/77.3 kB 233.1 MB/s eta 0:00:00
Downloading aiohttp-3.10.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 361.4 MB/s eta 0:00:00
Downloading fakeredis-2.24.1-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.0/97.0 kB 168.9 MB/s eta 0:00:00
Downloading fastapi-0.106.0-py3-none-any.whl (92 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 92.1/92.1 kB 379.7 MB/s eta 0:00:00
Downloading friendlywords-1.1.3-py3-none-any.whl (21 kB)
Downloading httpx-0.27.2-py3-none-any.whl (76 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 76.4/76.4 kB 339.0 MB/s eta 0:00:00
Downloading httpcore-1.0.5-py3-none-any.whl (77 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.9/77.9 kB 328.6 MB/s eta 0:00:00
Downloading jinja2-3.1.4-py3-none-any.whl (133 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.3/133.3 kB 284.2 MB/s eta 0:00:00
Downloading msgpack-1.0.8-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (409 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 409.3/409.3 kB 291.1 MB/s eta 0:00:00
Downloading pydantic-2.8.2-py3-none-any.whl (423 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 423.9/423.9 kB 347.7 MB/s eta 0:00:00
Downloading pydantic_core-2.20.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 375.4 MB/s eta 0:00:00
Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)
Downloading python_jose-3.3.0-py2.py3-none-any.whl (33 kB)
Downloading python_multipart-0.0.9-py3-none-any.whl (22 kB)
Downloading python_rapidjson-1.20-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 309.8 MB/s eta 0:00:00
Downloading shortuuid-1.0.13-py3-none-any.whl (10 kB)
Downloading typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Downloading uvicorn-0.30.6-py3-none-any.whl (62 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.8/62.8 kB 116.4 MB/s eta 0:00:00
Downloading aiofiles-24.1.0-py3-none-any.whl (15 kB)
Downloading executor_engine-0.2.5-py3-none-any.whl (24 kB)
Downloading imjoy_rpc-0.5.59-py3-none-any.whl (75 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 75.8/75.8 kB 316.6 MB/s eta 0:00:00
Downloading loguru-0.7.2-py3-none-any.whl (62 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.5/62.5 kB 259.6 MB/s eta 0:00:00
Downloading lxml-5.3.0-cp311-cp311-manylinux_2_28_x86_64.whl (5.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 MB 355.3 MB/s eta 0:00:00
Downloading munch-4.0.0-py2.py3-none-any.whl (9.9 kB)
Downloading numpy-2.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.3/16.3 MB 317.7 MB/s eta 0:00:00
Downloading psutil-6.0.0-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (290 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 290.5/290.5 kB 327.5 MB/s eta 0:00:00
Downloading requests-2.32.3-py3-none-any.whl (64 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.9/64.9 kB 281.7 MB/s eta 0:00:00
Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Downloading tqdm-4.66.5-py3-none-any.whl (78 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.4/78.4 kB 104.7 MB/s eta 0:00:00
Downloading websockets-13.0.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (157 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 157.9/157.9 kB 305.5 MB/s eta 0:00:00
Downloading aiohappyeyeballs-2.4.0-py3-none-any.whl (12 kB)
Downloading aioitertools-0.11.0-py3-none-any.whl (23 kB)
Downloading aiosignal-1.3.1-py3-none-any.whl (7.6 kB)
Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Downloading anyio-3.7.1-py3-none-any.whl (80 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80.9/80.9 kB 262.3 MB/s eta 0:00:00
Downloading attrs-24.2.0-py3-none-any.whl (63 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.0/63.0 kB 242.1 MB/s eta 0:00:00
Downloading botocore-1.35.7-py3-none-any.whl (12.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.5/12.5 MB 196.3 MB/s eta 0:00:00
Downloading certifi-2024.8.30-py3-none-any.whl (167 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 167.3/167.3 kB 270.8 MB/s eta 0:00:00
Downloading charset_normalizer-3.3.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (140 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 140.3/140.3 kB 153.7 MB/s eta 0:00:00
Downloading click-8.1.7-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 303.3 MB/s eta 0:00:00
Downloading cmd2func-0.2.1-py3-none-any.whl (7.4 kB)
Downloading ecdsa-0.19.0-py2.py3-none-any.whl (149 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 149.3/149.3 kB 202.8 MB/s eta 0:00:00
Downloading email_validator-2.2.0-py3-none-any.whl (33 kB)
Downloading frozenlist-1.4.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (272 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 272.3/272.3 kB 250.0 MB/s eta 0:00:00
Downloading funcdesc-0.1.3-py3-none-any.whl (10 kB)
Downloading h11-0.14.0-py3-none-any.whl (58 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.3/58.3 kB 214.2 MB/s eta 0:00:00
Downloading idna-3.8-py3-none-any.whl (66 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.9/66.9 kB 247.6 MB/s eta 0:00:00
Downloading MarkupSafe-2.1.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (28 kB)
Downloading multidict-6.0.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (128 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 128.7/128.7 kB 231.8 MB/s eta 0:00:00
Downloading redis-5.0.8-py3-none-any.whl (255 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 255.6/255.6 kB 217.9 MB/s eta 0:00:00
Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)
Downloading starlette-0.27.0-py3-none-any.whl (66 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.0/67.0 kB 163.8 MB/s eta 0:00:00
Downloading urllib3-2.2.2-py3-none-any.whl (121 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.4/121.4 kB 351.2 MB/s eta 0:00:00
Downloading wrapt-1.16.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (80 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80.7/80.7 kB 336.3 MB/s eta 0:00:00
Downloading yarl-1.9.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (331 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 331.8/331.8 kB 288.8 MB/s eta 0:00:00
Downloading cloudpickle-3.0.0-py3-none-any.whl (20 kB)
Downloading diskcache-5.6.3-py3-none-any.whl (45 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.5/45.5 kB 184.9 MB/s eta 0:00:00
Downloading loky-3.4.1-py3-none-any.whl (54 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.6/54.6 kB 248.4 MB/s eta 0:00:00
Downloading pyasn1-0.6.0-py2.py3-none-any.whl (85 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.3/85.3 kB 359.8 MB/s eta 0:00:00
Downloading rsa-4.9-py3-none-any.whl (34 kB)
Downloading termcolor-2.4.0-py3-none-any.whl (7.7 kB)
Downloading dnspython-2.6.1-py3-none-any.whl (307 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 307.7/307.7 kB 313.4 MB/s eta 0:00:00
Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 295.8 MB/s eta 0:00:00
Building wheels for collected packages: bioimageio.engine, fire
  Building wheel for bioimageio.engine (pyproject.toml) ... done
  Created wheel for bioimageio.engine: filename=bioimageio.engine-0.1.1-py3-none-any.whl size=38098 sha256=036a8dbb24fe1b8844dc54d13b6aa8bc19488cfe133b86f03813c403ef49c3d1
  Stored in directory: /tmp/pip-ephem-wheel-cache-s44ws1v3/wheels/f4/ec/ee/0716c9feb9d1dd5d9fe2e4166b024cd23469a697fec8fa5f96
  Building wheel for fire (setup.py) ... done
  Created wheel for fire: filename=fire-0.6.0-py2.py3-none-any.whl size=117033 sha256=068f5898de15f783c59457383e99135c00fcb416769082208fef5f5fc3781f76
  Stored in directory: /tmp/pip-ephem-wheel-cache-s44ws1v3/wheels/6a/f3/0c/fa347dfa663f573462c6533d259c2c859e97e103d1ce21538f
Successfully built bioimageio.engine fire
Installing collected packages: sortedcontainers, wrapt, websockets, urllib3, typing-extensions, tqdm, termcolor, sniffio, six, simpervisor, shortuuid, redis, PyYAML, python-rapidjson, python-multipart, python-dotenv, pyasn1, psutil, numpy, munch, multidict, msgpack, MarkupSafe, lxml, loguru, jmespath, idna, h11, funcdesc, frozenlist, friendlywords, dnspython, diskcache, cloudpickle, click, charset-normalizer, certifi, attrs, annotated-types, aioitertools, aiohappyeyeballs, aiofiles, yarl, uvicorn, rsa, requests, python-dateutil, pydantic-core, loky, jinja2, imjoy-rpc, hypha-rpc, httpcore, fire, fakeredis, email-validator, ecdsa, cmd2func, anyio, aiosignal, starlette, python-jose, pyotritonclient, pydantic, httpx, executor-engine, botocore, aiohttp, fastapi, aiobotocore, hypha, hypha-launcher, bioimageio.engine
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
azure-cli-core 2.40.0 requires psutil~=5.9; sys_platform != "cygwin", but you have psutil 6.0.0 which is incompatible.
boto3 1.26.76 requires botocore<1.30.0,>=1.29.76, but you have botocore 1.35.7 which is incompatible.
conda 24.7.1 requires packaging>=23.0, but you have packaging 21.3 which is incompatible.
pyasn1-modules 0.3.0 requires pyasn1<0.6.0,>=0.4.6, but you have pyasn1 0.6.0 which is incompatible.
pywavelets 1.5.0 requires numpy<2.0,>=1.22.4, but you have numpy 2.1.0 which is incompatible.
scipy 1.11.4 requires numpy<1.28.0,>=1.21.6, but you have numpy 2.1.0 which is incompatible.
Successfully installed MarkupSafe-2.1.5 PyYAML-6.0.2 aiobotocore-2.14.0 aiofiles-24.1.0 aiohappyeyeballs-2.4.0 aiohttp-3.10.5 aioitertools-0.11.0 aiosignal-1.3.1 annotated-types-0.7.0 anyio-3.7.1 attrs-24.2.0 bioimageio.engine-0.1.1 botocore-1.35.7 certifi-2024.8.30 charset-normalizer-3.3.2 click-8.1.7 cloudpickle-3.0.0 cmd2func-0.2.1 diskcache-5.6.3 dnspython-2.6.1 ecdsa-0.19.0 email-validator-2.2.0 executor-engine-0.2.5 fakeredis-2.24.1 fastapi-0.106.0 fire-0.6.0 friendlywords-1.1.3 frozenlist-1.4.1 funcdesc-0.1.3 h11-0.14.0 httpcore-1.0.5 httpx-0.27.2 hypha-0.20.32 hypha-launcher-0.1.3 hypha-rpc-0.20.32 idna-3.8 imjoy-rpc-0.5.59 jinja2-3.1.4 jmespath-1.0.1 loguru-0.7.2 loky-3.4.1 lxml-5.3.0 msgpack-1.0.8 multidict-6.0.5 munch-4.0.0 numpy-2.1.0 psutil-6.0.0 pyasn1-0.6.0 pydantic-2.8.2 pydantic-core-2.20.1 pyotritonclient-0.2.6 python-dateutil-2.9.0.post0 python-dotenv-1.0.1 python-jose-3.3.0 python-multipart-0.0.9 python-rapidjson-1.20 redis-5.0.8 requests-2.32.3 rsa-4.9 shortuuid-1.0.13 simpervisor-1.0.0 six-1.16.0 sniffio-1.3.1 sortedcontainers-2.4.0 starlette-0.27.0 termcolor-2.4.0 tqdm-4.66.5 typing-extensions-4.12.2 urllib3-2.2.2 uvicorn-0.30.6 websockets-13.0.1 wrapt-1.16.0 yarl-1.9.6
(base) I have no name!@ray-hypha-service-59bcd866c6-74tq5:/app$ HYPHA_SERVER_URL=https://hypha.aicell.io HYPHA_WORKSPACE=bioengine-apps HYPHA_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FtdW4uYWkvIiwic3ViIjoiZW1lcmFsZC1zY2FyLTU1NjI0MjcwIiwiYXVkIjoiaHR0cHM6Ly9hbXVuLWFpLmV1LmF1dGgwLmNvbS9hcGkvdjIvIiwiaWF0IjoxNzI0MjExMDQ2LCJleHAiOjE3MjUyMTEwNDYsInNjb3BlIjoid3M6YmlvZW5naW5lLWFwcHMjcncgd2lkOmJpb2VuZ2luZS1hcHBzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwiaHR0cHM6Ly9hbXVuLmFpL3JvbGVzIjpbImFkbWluIl0sImh0dHBzOi8vYW11bi5haS9lbWFpbCI6Im9ld2F5MDA3QGdtYWlsLmNvbSJ9.C1MwD2o99aRHn05RBbtbPFf3TXPfmuxtGVhyfuWX4hY serve run bioimageio.engine.ray_app_manager:app --address=ray://service-ray-cluster:20002
2024-08-31 14:49:11,416 INFO scripts.py:499 -- Running import path: 'bioimageio.engine.ray_app_manager:app'.
INFO:app_launcher:App loaded: Cellpose
INFO:app_launcher:App loaded: microSAM
INFO:app_launcher:App loaded: Translator
Loaded apps: dict_keys(['cellpose', 'micro_sam', 'translator'])
(ProxyActor pid=3093) INFO 2024-08-31 14:49:17,457 proxy 10.42.5.206 proxy.py:1165 - Proxy starting on node 8b3e10a943a3e228db2c17c035091abee3264c1ac381730ab9e13d42 (HTTP port: 8000).
2024-08-31 14:49:18,041 INFO handle.py:126 -- Created DeploymentHandle 'qcfof48d' for Deployment(name='cellpose', app='default').
2024-08-31 14:49:18,042 INFO handle.py:126 -- Created DeploymentHandle 'zb8e5t8i' for Deployment(name='micro_sam', app='default').
2024-08-31 14:49:18,043 INFO handle.py:126 -- Created DeploymentHandle 'c4a685vf' for Deployment(name='translator', app='default').
2024-08-31 14:49:18,044 INFO handle.py:126 -- Created DeploymentHandle 'dopzol9y' for Deployment(name='cellpose', app='default').
2024-08-31 14:49:18,044 INFO handle.py:126 -- Created DeploymentHandle '5bqckge5' for Deployment(name='micro_sam', app='default').
2024-08-31 14:49:18,044 INFO handle.py:126 -- Created DeploymentHandle 'b18jbp0x' for Deployment(name='translator', app='default').
2024-08-31 14:49:18,045 INFO handle.py:126 -- Created DeploymentHandle 'zcq5apjs' for Deployment(name='HyphaRayAppManager', app='default').
2024-08-31 14:49:18,045 INFO handle.py:126 -- Created DeploymentHandle '1i3ba3ds' for Deployment(name='cellpose', app='default').
2024-08-31 14:49:18,046 INFO handle.py:126 -- Created DeploymentHandle '8ap6039s' for Deployment(name='micro_sam', app='default').
2024-08-31 14:49:18,046 INFO handle.py:126 -- Created DeploymentHandle '8rc5z4z2' for Deployment(name='translator', app='default').
2024-08-31 14:49:18,046 INFO handle.py:126 -- Created DeploymentHandle 'gbmawmgq' for Deployment(name='HyphaRayAppManager', app='default').
(ServeController pid=3025) INFO 2024-08-31 14:49:18,150 controller 3025 deployment_state.py:1598 - Deploying new version of Deployment(name='cellpose', app='default') (initial target replicas: 0).
(ServeController pid=3025) INFO 2024-08-31 14:49:18,153 controller 3025 deployment_state.py:1598 - Deploying new version of Deployment(name='micro_sam', app='default') (initial target replicas: 0).
(ServeController pid=3025) INFO 2024-08-31 14:49:18,156 controller 3025 deployment_state.py:1598 - Deploying new version of Deployment(name='translator', app='default') (initial target replicas: 0).
(ServeController pid=3025) INFO 2024-08-31 14:49:18,160 controller 3025 deployment_state.py:1598 - Deploying new version of Deployment(name='HyphaRayAppManager', app='default') (initial target replicas: 1).
(ServeController pid=3025) INFO 2024-08-31 14:49:18,265 controller 3025 deployment_state.py:1844 - Adding 1 replica to Deployment(name='HyphaRayAppManager', app='default').
(ServeReplica:default:HyphaRayAppManager pid=795, ip=10.42.6.166) Registering method predict for app cellpose
(ServeReplica:default:HyphaRayAppManager pid=795, ip=10.42.6.166) Registering method train for app cellpose
(ServeReplica:default:HyphaRayAppManager pid=795, ip=10.42.6.166) Added service cellpose with id bioengine-apps/KbksMK3ofz9YLg7cdy9Z4h:cellpose, use it at https://hypha.aicell.io/bioengine-apps/services/KbksMK3ofz9YLg7cdy9Z4h:cellpose
(ServeReplica:default:HyphaRayAppManager pid=795, ip=10.42.6.166) Registering method compute_embedding for app micro_sam
(ServeReplica:default:HyphaRayAppManager pid=795, ip=10.42.6.166) Registering method reset_embedding for app micro_sam
(ServeReplica:default:HyphaRayAppManager pid=795, ip=10.42.6.166) Registering method segment for app micro_sam
(ServeReplica:default:HyphaRayAppManager pid=795, ip=10.42.6.166) Added service micro_sam with id bioengine-apps/KbksMK3ofz9YLg7cdy9Z4h:micro_sam, use it at https://hypha.aicell.io/bioengine-apps/services/KbksMK3ofz9YLg7cdy9Z4h:micro_sam
(ServeReplica:default:HyphaRayAppManager pid=795, ip=10.42.6.166) Registering method translate for app translator
(ServeReplica:default:HyphaRayAppManager pid=795, ip=10.42.6.166) Added service translator with id bioengine-apps/KbksMK3ofz9YLg7cdy9Z4h:translator, use it at https://hypha.aicell.io/bioengine-apps/services/KbksMK3ofz9YLg7cdy9Z4h:translator
2024-08-31 14:49:27,246 INFO handle.py:126 -- Created DeploymentHandle 'eu10b4t9' for Deployment(name='HyphaRayAppManager', app='default').
2024-08-31 14:49:27,247 INFO api.py:584 -- Deployed app 'default' successfully.
(ProxyActor pid=868, ip=10.42.6.166) INFO 2024-08-31 14:49:28,058 proxy 10.42.6.166 proxy.py:1165 - Proxy starting on node d7fb0036bb0570ba9bd652d8e48b5fe5e960eb22f954610a25f4b02d (HTTP port: 8000).
(ServeController pid=3025) INFO 2024-08-31 14:49:55,723 controller 3025 deployment_state.py:1647 - Upscaling Deployment(name='cellpose', app='default') from 0 to 1 replicas. Current ongoing requests: 1.00, current running replicas: 0.
(ServeController pid=3025) INFO 2024-08-31 14:49:55,725 controller 3025 deployment_state.py:1844 - Adding 1 replica to Deployment(name='cellpose', app='default').
(raylet) [2024-08-31 14:50:16,690 E 253 253] (raylet) node_manager.cc:3034: 1 Workers (tasks / actors) killed due to memory pressure (OOM), 0 Workers crashed due to other reasons at node (ID: 8b3e10a943a3e228db2c17c035091abee3264c1ac381730ab9e13d42, IP: 10.42.5.206) over the last time period. To see more information about the Workers killed on this node, use `ray logs raylet.out -ip 10.42.5.206`
(raylet) 
(raylet) Refer to the documentation on how to address the out of memory issue: https://docs.ray.io/en/latest/ray-core/scheduling/ray-oom-prevention.html. Consider provisioning more memory on this node or reducing task parallelism by requesting more CPUs per task. To adjust the kill threshold, set the environment variable `RAY_memory_usage_threshold` when starting Ray. To disable worker killing, set the environment variable `RAY_memory_monitor_refresh_ms` to zero.
(ServeController pid=3025) WARNING 2024-08-31 14:50:25,829 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:50:55,886 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:51:25,925 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:51:55,948 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:52:25,997 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:52:56,004 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:53:26,061 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:53:56,080 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:54:26,128 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:54:56,230 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:55:26,262 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:55:56,303 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:56:26,321 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:56:56,362 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:57:26,388 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:57:56,417 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:58:26,504 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:58:56,577 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:59:26,667 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
(ServeController pid=3025) WARNING 2024-08-31 14:59:56,756 controller 3025 deployment_state.py:2147 - Deployment 'cellpose' in application 'default' has 1 replicas that have taken more than 30s to be scheduled. This may be due to waiting for the cluster to auto-scale or for a runtime environment to be installed. Resources required for each replica: {"CPU": 1.0}, total resources available: {"CPU": 1.0}. Use `ray status` for more details.
^C2024-08-31 15:00:04,576       WARNING api.py:592 -- Got KeyboardInterrupt, exiting...
2024-08-31 15:00:04,577 INFO scripts.py:585 -- Got KeyboardInterrupt, shutting down...
(ServeController pid=3025) INFO 2024-08-31 15:00:04,683 controller 3025 deployment_state.py:1860 - Removing 1 replica from Deployment(name='cellpose', app='default').
(ServeController pid=3025) INFO 2024-08-31 15:00:04,683 controller 3025 deployment_state.py:1860 - Removing 1 replica from Deployment(name='HyphaRayAppManager', app='default').
^C
Aborted!
(base) I have no name!@ray-hypha-service-59bcd866c6-74tq5:/app$ ^C
(base) I have no name!@ray-hypha-service-59bcd866c6-74tq5:/app$ HYPHA_SERVER_URL=https://hypha.aicell.io HYPHA_WORKSPACE=bioengine-apps HYPHA_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FtdW4uYWkvIiwic3ViIjoiZW1lcmFsZC1zY2FyLTU1NjI0MjcwIiwiYXVkIjoiaHR0cHM6Ly9hbXVuLWFpLmV1LmF1dGgwLmNvbS9hcGkvdjIvIiwiaWF0IjoxNzI0MjExMDQ2LCJleHAiOjE3MjUyMTEwNDYsInNjb3BlIjoid3M6YmlvZW5naW5lLWFwcHMjcncgd2lkOmJpb2VuZ2luZS1hcHBzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwiaHR0cHM6Ly9hbXVuLmFpL3JvbGVzIjpbImFkbWluIl0sImh0dHBzOi8vYW11bi5haS9lbWFpbCI6Im9ld2F5MDA3QGdtYWlsLmNvbSJ9.C1MwD2o99aRHn05RBbtbPFf3TXPfmuxtGVhyfuWX4hY serve run bioimageio.engine.ray_app_manager:app --address=ray://service-ray-cluster:20002