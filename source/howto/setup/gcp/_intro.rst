The "Compute and Data Layer" of Valohai can be deployed to your GCP project. This enables you to:

* Use your own Virtual Machines instances to run machine learning jobs
* Use your own Google Storage Bucket for storing training artefacts, like trained models, preprocessed datasets, visualizations, etc.
* Access databases and date warehouses directly from the workers, which are inside your network.

Valohai doesn't have direct access to the virtual machine instances that execute the machine learning jobs. Instead it communicates with a static virtual machine in your GCP project that's responsible for storing the job queue, job states, and short-term logs.

.. image:: /_images/valohai_environment.png
    :width: 700
    :alt: Valohai Components
