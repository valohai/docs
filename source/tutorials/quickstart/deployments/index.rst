.. meta::
    :description: Learn the basics of Valohai

.. _valohai101-deployments:


Deployments
===========

Valohai you to easily manage model versions, deployments, and collect custom metrics from your inference.

There are two ways to run inference on Valohai. You should choose the case that suits your use case better.

* **Valohai Deployments** push new deployment versions to your Kubernetes cluster. You're responsible for writing up your own RESTful APIs (for example with FastAPI, Flask, etc.) and configuring the Kubernetes cluster's node-groups and scaling rules.
* **Valohai executions for inference** allow you to specify an inference job using a standard Valohai execution. You can use the Valohai APIs to launch a new inference job with the specificed data and model file(s).

.. raw:: html

    <div style="position: relative; padding-bottom: 52.785923753665685%; height: 0;"><iframe src="https://www.loom.com/embed/488d391bb146463f91109743ad429ca6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

See the tutorials below to learn how to build your deployments:

.. toctree::
    :titlesonly:

    quickstart-deployments
    batch-inference/csv-batch-inference
    batch-inference/image-batch-inference


Comparing Valohai deploymet options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :widths: 15 42 43

   * - Requirement
     - Real-time inference & Custom APIs
     - Valohai executions for inference
   * - Latency & Inference time
     - I need low latency and prediction results in (sub)seconds.
     - I don't have strict latency requirements and my predictions can take minutes.
   * - API
     - Write your your own RESTful APIs and routing (FastAPI, Flask, etc.) 
     - Use Valohai's own RESTful APIs to launch a prediction with your data & model(s).
   * - Versioning
     - Yes. Valohai keeps track of the different versions of your code and model file(s) through deployment versions.
     - Yes. Valohai keeps track of the different versions of your code and model file(s) through execution versioning.
   * - Metrics
     - Yes. Collect custom logs from your endpoints by dumping JSON that can be then visualized with Valohai. See `Monitor your deployment endpoints </howto/deployments/deployment-monitoring/#monitoring-your-deployment-endpoints>`_ for details.
     - Yes. Collect custom logs from your endpoints by dumping JSON that can be then visualized with Valohai. See `Collect metadata </howto/new-user-guide/code/metadata/>`_ for details.
   * - Aliases
     - Yes. You can use `deployment aliases </topic-guides/core-concepts/deployments/#deployment-aliases>`_ to give friendly names to your endpoints. For example and alias ``production`` could point to the deployment version that is currently set to production. You can then easily change which version does ``production`` point to without having to change the API URL that you call.
     - Yes. Each of your model files is versioned automatically by Valohai. You can also create `Datum Aliases </howto/data/datum-alias/>`_ to easily keep track of the exact model version(s) that are currently in production, QA, or somewhere else.
   * - Configuration & Management
     - You are responsible for creating and managing the Kubernetes cluster. This means that you'll be responsible for setting up node groups, access control, and different Kubernetes scaling rules.
     - Valohai managed the Virtual Machine that will be used for the inference. This machine can either be scaled up/down or you could keep a set of machines hot all the time.
   * - What do you need to provide?
     - 
       * Inference code
       * Write your your own RESTful APIs (FastAPI, Flask, etc.) 
       * A base docker image
       * Model file(s)
       * Resource requirements (CPU, Memory)

     - 
       * Inference code
       * Inference code
       * A base docker image
       * Model file(s)
       * Virtual Machine type (CPU/GPU, Memory)

