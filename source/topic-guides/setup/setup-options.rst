.. meta::
    :description: Comparison between a Private Worker and Full Private installation


Choosing the right installation setup
########################################

Valohai can be configured to run on both cloud (e.g. Microsoft Azure, Amazon Web Services, Google Cloud Platform) and on-premise servers, or a combination of these. In addition to the SaaS version available at app.valohai.com

This page describes the different resources that will be set up and the access control permissions that need to be configured in order for the Valohai team to complete the setup.

.. warning::

    This applies only to private Valohai installations. You can use app.valohai.com without additional configuration or setup.

..

🔐 Private Worker Installation
---------------------------------

This installation allows you to run your own cloud or on-premise machines to run executions on Valohai (`architecture </_static/Valohai_Architecture_PrivateWorker.pdf>`__).

* All machines that access data and run executions (e.g. preprocessing, training, etc.) are located inside your environment (Azure, AWS, GCP, on-premises).
* All data (e.g. training data) is stored in your own data storage (e.g. AWS S3, GCP Bucket, Azure Blob Storage, on-premises).
* Valohai hosts the web app (app.valohai.com) and Valohai servers store information on:
    * User accounts (for login, authentication and authorization)
    * Execution details (who ran which training, when and with what parameters)
    * Logs from the executions (status & error messages, and messages that you've printed in `stdout </topic-guides/executions/logs/>`_)
    * Git commit snapshots to ensure reproducability in the platform (Valohai allows you to go back in time and easily reproduce executions as it's tracking this history)


🔐🔐 Self-Hosted Installation
---------------------------------

Setup a fully private Valohai installation that can be inside your private network and access your private resources (`architecture </_static/Valohai_Architecture_FullPrivate.pdf>`__).

* A custom installation of Valohai that contains all Valohai services (inc. web app, core Valohai servers, logging, and user management).
* Access Valohai from your custom location (e.g. https://valohai.your-company.com)
* Allows you to place Valohai inside your own private network.
* Easily configured to access internal resources (e.g. Git repositories, on-premise machines).
* No requirements to have any traffic leave your network
