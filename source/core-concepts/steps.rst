.. meta::
    :description: What are Valohai steps? Building your data science pipeline one step at a time.

Steps
=====

.. seealso::

    For the technical specifications, go to :doc:`valohai.yaml step section </valohai-yaml/step>`.

Each **step** defines a workload type; such as
data anonymization, data generation, feature extraction, training or model evaluation.

To run a step, you create an execution, then that execution can be said to **implement the step**.
Executions are heavily version controlled so re-executing any
past workloads will work as long as the Docker image and inputs still exist.

As machine learning projects are vastly different from one another,
users are allowed to be as flexible as possible in building their own data science pipelines.

Usually separate steps are defined for:

* preprocessing files and upload them to be used by other steps
* integrating with database services to create version controlled snapshot for training data
* executing a Python script or C code e.g. to train a predictive model
* validating if a trained model model could be used for production
* deploying trained model to staging or production
* build application binaries to be used in other steps

:doc:`What is Valohai? page </core-concepts/what-is-valohai>` lists additional possible
"steps" in a machine learning pipeline we have seen over the years.
You can run anything that works inside a Docker container so the possibilities are seemingly endless.

You define project steps in project :doc:`valohai.yaml</valohai-yaml/index>`.

.. tip::

    You can also run steps from command-line or API; web interface is just one approach.
