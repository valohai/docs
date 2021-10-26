The Compute and Data Layer of Valohai can be deployed to your AWS Account. This enables you to:

* Use your own EC2 instances to run machine learning jobs.
* Use your own S3 Buckets for storing training artefacts such as trained models, preprocessed datasets, visualizations, etc.
* Access databases and data warehouses directly from the workers, which are inside your network.

Valohai doesn't have direct access to the EC2 instances that execute the machine learning jobs. Instead it communicates with a static EC2 instance in your AWS subscription that's responsible for storing the job queue, job states, and short-term logs.

.. image:: /_images/valohai_environment.png
    :width: 700
    :alt: Valohai Components
