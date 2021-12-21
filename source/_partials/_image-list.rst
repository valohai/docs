Here are the most common Docker images currently used on the platform:

.. code-block:: bash

    tensorflow/tensorflow:<VERSION>-gpu                                  # e.g. 2.6.1-gpu, for GPU support
    tensorflow/tensorflow:<VERSION>                                      # e.g. 2.6.1, for CPU only
    pytorchlightning/pytorch_lightning:latest-py<version>-torch<version> # e.g. py3.6-torch1.6
    pytorch/pytorch:<VERSION>                                            # e.g. 1.3-cuda10.1-cudnn7-runtime
    python:<VERSION>                                                     # e.g. 3.8.0
    r-base:<VERSION>                                                     # e.g. 3.6.1
    julia:<VERSION>                                                      # e.g. 1.3.0
    valohai/fbprophet                                                    # Valohai hosted image with Prophet
    valohai/sklearn:1.0                                                  # Valohai hosted image with sklean
    valohai/xgboost:1.4.2                                                 # Valohai hosted image with xgboost