.. meta::
    :description: xxx

Architecture
============

Valohai can be deployed in three flavors:

* **Software-as-a-Service Installation:**
  Users run workloads under Valohai owned AWS, Google Cloud, Azure and other cloud provider accounts.
  Valohai bills organization depending how much resources they use. SaaS flavor works without any setup.
* **Private Workers Installation:**
  Workers nodes that handle the data processing, training and inference are all deployed under customer owned AWS, Google Cloud or Azure account. No input or output data ever leaves the customer account network.
* **Full Private Installation:**
  All components are deployed inside customer owned AWS, Google Cloud, Azure or data center; allowing fully enclosed installation. Required for setups without Internet connection.

Components
~~~~~~~~~~

To get a general idea how the architecture looks, here is a diagram of a common SaaS use-case:

.. figure:: architecture-overview.png
  :alt: Architecture Overview Diagram

* **Valohai Master:**
  Valohai master node that runs the web application and the API. Master is the core component that manages all the other resources such as scheduling executions and scaling individual worker groups across cloud providers.
* **Valohai Database:**
  A relational database that contains user data and saves execution details such as which worker type was used, what commands were run, what Docker image was used, which inputs where used and what was the launch configuration.
* **Git Repositories:**
  External code repositories for the data science projects. Usually a private GitHub repository but can be any Git repository like GitLab or GitHub Enterprise as long as Valohai Master can access it.
* **User Code Archive:**
  We store Git commit snapshot in binary storage (AWS S3, Azure Blob Storage, etc.) to maintain reproducibility. Worker machines load the user code archives from this storage.
* **Worker Binary Storage:**
  Worker machines have an executable that downloads inputs (e.g. training data), starts the configured Docker image, reports real-time logs and uploads outputs (e.g. trained models). Worker release binaries are stored in this binary storage.
* **Log Storage:**
  Real-time logs are moved to a binary storage for long-term storage after the target execution finishes.
* **Queues and Cache:** In-memory database instance that has hosts execution/build queues and caches user code logs so they can be shown on Valohai web app and API in real-time.
* **Workers Groups:** Workers are the servers that execute user code. There is one worker group per instance type (e.g. g2.2xlarge on AWS) per region (e.g. AWS Ireland). Valohai Master manages these auto-scaling groups. Workers can also be non-scaling cluster of on-premises machines. Worker groups can be local, AWS, Azure, GCP or OpenStack.
* **Artifact Stores:** Execution inputs are downloaded from and outputs are uploaded to a file storage. Valohai supports various storage back-ends but an AWS S3 bucket is the most commonly used artifact store.
* **Docker Registries:** Used Docker images are downloaded from a private or public Docker registry. Docker Hub is the most common one but you can also host Docker registry inside your cloud provider account.
* **Inference Builders:** Before hosting your model for inference, we build a Docker image to make deployments fast and reliable. It will prebuild all files required for deployment so endpoint can be easily scaled.
* **Inference Registry:** Used inference Docker images are uploaded to a private Docker registry, usually hosted under the inference provider account like AWS, GCP or Azure.
* **Inference Cluster:** Kubernetes cluster that hosts the inference request/response endpoints. It downloads the used images from private inference registry.
