.. meta::
    :description: What are Valohai steps? Building your data science pipeline one step at a time.

Steps
=====

Each **step** defines a separate type of an execution; such as data anonymization, data generation, feature extraction, training or model evaluation.

You execute a step that creates an execution. Step executions are heavily version controlled so re-executing any past workloads will work as long as the Docker image and inputs still exist.

As machine learning projects are very different from one another, we feel like users should be allowed to be as flexible as possible in building their own data science pipeline steps.

Usually separate steps are defined for:

* preprocessing files and upload them to be used by other steps
* integrating with database services to create version controlled snapshot for training data
* executing a Python script or C code e.g. to train a predictive model
* validating if a trained model model could be used for production
* deploying trained model to staging or production
* build application binaries to be used in other steps

You can run anything that works inside a Docker container so the possibilities are endless.

You define project steps in :doc:`valohai.yaml</valohai-yaml/index>`.

.. figure:: execution-form.jpg
   :alt: Step form to create an execution.

.. tip::
    You can also create step executions with Valohai command-line client or API; web interface is just one approach.