Here are the most common Docker images currently used on the platform:

.. code-block:: bash

    ufoym/deepo:all-py36                     # good for initial prototyping
    ufoym/deepo:all-py36-cpu                 # good for initial prototyping
    tensorflow/tensorflow:<VERSION>-gpu-py3  # e.g. 1.15.0, for GPU support
    tensorflow/tensorflow:<VERSION>-py3      # e.g. 1.15.0, for CPU only
    pytorch/pytorch:<VERSION>                # e.g. 1.3-cuda10.1-cudnn7-runtime
    continuumio/miniconda:<VERSION>          # e.g. 4.7.10
    python:<VERSION>                         # e.g. 3.8.0
    r-base:<VERSION>                         # e.g. 3.6.1
    julia:<VERSION>                          # e.g. 1.3.0
    bash:<VERSION>                           # e.g. 5.0.11, for light scripting
    busybox:<VERSION>                        # e.g. 1.13.1, for light scripting
