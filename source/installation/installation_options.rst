.. meta::
    :description: Comparison between a Private Worker and Full Private installation
    
******************************************
Choosing the right installation method
******************************************

Valohai can be installed on both cloud (e.g. Microsoft Azure, Amazon Web Services, Google Cloud Platform) and on-prem servers, or a combination of these.

This page describes the different resources that will be set up and the access control permissions that need to be configured in order for the Valohai team to complete the setup.

🔐 Private Worker Installation
###############################

This installation allows you to run your own cloud or on-prem machines to run executions on Valohai (`architecture </_static/Valohai_Architecture_PrivateWorker.pdf>`__).

    * All machines that access data and run executions (e.g. preprocessing, training, etc.) are located inside your environment (Azure, AWS, GCP, on-premises).
    * All data (e.g. training data) is stored in your own data storage (e.g. AWS S3, GCP Bucket, Azure Blob Storage, on-premises).
    * Valohai hosts the web app (app.valohai.com) and Valohai servers store information on:
        * User accounts (for login, authentication and authorization)
        * Execution details (who ran which training, when and with what parameters)
        * Logs from the executions (status & error messages, and messages that you've printed in `stdout </executions/logs/>`_)
        * Git commit snapshots to ensure reproducability in the platform (Valohai allows you to go back in time and easily reproduce executions as it's tracking this history)

⬇️ Download our Private Worker Installation Guide for a detailed list of permissions that Valohai will need in your cloud environment:
    * `Amazon Web Services - Private Worker Installation <https://get.valohai.com/aws-worker-installation>`_
    * `Microsoft Azure - Private Worker Installation <https://get.valohai.com/azure-worker-installation>`_
    * `Google Cloud Platform - Private Worker Installation <https://get.valohai.com/gcp-worker-installation>`_

What will Valohai install in my subscription?
************************************************

* **valohai-i-queue** a low-cost machine (2 vCPUs, 4GB RAM) that keep track of the queue of your organizations executions. This machine will also have a static IP address assigned to it.
* **valohai-vpc** and subnets per each availability zone you want to use. All Valohai machines will be placed within this VPC. It's also possible to use existing VPCs.
* **valohai-scalie** (not applicable in AWS) a low-cost machine that will managing the scaling of compute instances.
* **security groups / firewall rules**
    * Allow Valohai resources to access the machines, and the workers to communicate with the queue.
    * (optional) Allow ssh access to the machines for further updates and maintenance.

🔐🔐Full Private Installation
###############################

Setup a fully private Valohai installation that can be inside your private network and access your private resources (`architecture </_static/Valohai_Architecture_FullPrivate.pdf>`__).

* A custom installation of Valohai that contains all Valohai services (inc. web app, core Valohai servers, logging, and user management).
* Access Valohai from your custom location (e.g. https://valohai.your-company.com)
* Allows you to place Valohai inside your own private network.
* Easily configured to access internal resources (e.g. Git repositories, on-prem machines).

⬇️ Download our Full Private Installation Guide for a detailed list of permissions that our engineering team to install Valohai in your environment.

* `Amazon Web Services - Full Private Installation <https://get.valohai.com/aws-private-installation>`_

What will Valohai install in my subscription?
************************************************

* **A virtual machine** (4 vCPUs, 16GB RAM) for the Valohai API and web UI.
* **A PostgreSQL database**, for general metadata
    * If needed, this can also be installed on a virtual machine instead of a managed service.
* **Redis database**, for workload queue. One of these databases is set up per each AWS region you want to use
    * If needed, this can also be installed on a virtual machine instead of a managed service.
* **A storage account** dedicated for Valohai (e.g. AWS S3, GCP Bucket, Azure Blob Storage)
* **VPC and subnets** per each availability zone you want to use. It's also possible to use existing VPCs.

.. container:: alert alert-warning

    **Enterprise users**
    
    For enterprise users we recommend the Full Private Installation which can be installed inside your private network and configured to securely access local resources that are behind a VPN/firewall (local machines, data, repositories etc.)

..