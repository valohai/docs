:hide-toc:

.. meta::
    :description: Valohai deep learning management platform architecture diagram and installation flavors.

.. _setup:

Deploy Valohai in your environment
##################################

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    aws/index
    gcp/index
    azure/index
    onpremises/index
    self-hosted/index


Valohai can be deployed in your environment, either in the cloud or on-premise. The platform can also be deployed in multi-cloud setups and in hybrid setups with both cloud and on-premise resources.

When using Valohai:

* Your data stays in your environments (object storages, databases, and data warehouses).
* The machine learning jobs are performed on your own virtual machines.
* Models are deployed to your own object stores and registries.

.. list-table::
   :widths: 20 25 55
   :header-rows: 1
   :stub-columns: 1

   * - Cloud
     - Architecture
     - Installation
   * - AWS
     - Architecture
     - `CloudFormation <https://github.com/valohai/aws-hybrid-workers-cloudformation>`_ / `AWS Terraform <https://github.com/valohai/aws-hybrid-workers-terraform>`_ / :ref:`aws-hybrid-manual`
   * - GCP
     - Architecture
     - `GCP Terraform <https://github.com/valohai/gcp-hybrid-workers-terraform>`_ / :ref:`gcp-hybrid-manual`
   * - Azure
     - Architecture
     - :ref:`azure-hybrid-manual`

.. admonition:: What is Valohai?
    :class: hint

    In short, Valohai allows you to spend less time on infrastructure management and manual experiment tracking and let your data scientists concentrate on building custom models.
    
    `Read more about Valohai <https://valohai.com/product/>`_

Valohai components
-------------------

.. thumbnail:: /_images/valohai_environment.png
    :width: 700
    :alt: Valohai Components

Valohai comprises of two layers, the Application Layer and the Compute & Data Layer.

The Valohai application doesn't directly access your workers but instead writes requests and updates to the job queue machine, from where your own workers find jobs that are scheduled for them.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Application layer
     - Compute & Data Layer
   * - Hosted by Valohai
     - Hosted in your cloud/on-premises
   * - 
       * The **web application**
       * A **PostgreSQL database** for storing user and execution metadata information (who ran what, and when)
       * A **scaling service** responsible for managing virtual machine instances
       * A **deployment image builder** for building and publishing images for online-inference
       * The **API services** that enable you to:
          * Launch, view, and manage jobs, pipelines, and deployments
          * Access execution results, files, and metrics
          * Launch batch processing jobs
          * …more :ref:`api`
     - 
       * A **virtual machine** that manages the machine learning job queue
       * **Object storage(s)** to store job logs, snapshots, and generated files (e.g. models, dataset snapshots)
       * **Autoscaled virtual machines** to run machine learning jobs
       * Other optional services, like:
          * Your existing **Kubernetes cluster**, to enable teams to deploy models for real-time inference
          * **Private Docker Registry**
          * Other **data sources** (databases, data warehouses, etc.)
          * A **Spark cluster**

.. seealso::

    Need to run Valohai completely inside your own network? See the guide `Deploy a self-hosted Valohai </howto/setup/self-hosted/>`_ 


Permissions and access
----------------------

Valohai will need a set of permissions in your cloud environment to autoscale your virtual machines and store logs, snapshots and generated files in an object storage.

First you provision the core Valohai services in your cloud and register your organization in Valohai. Then you can set up your projects and connect them with your Git repositories, object storages, and private Docker registries.

.. seealso::

    See the installation pages for AWS, GCP, and Azure for detailed guides and installation templates.

.. list-table::
   :widths: 20 40 40
   :header-rows: 1
   :stub-columns: 1

   * - Service
     - Access
     - Configuration
   * - Core Services
     - Access to manage virtual machines and read/write to one object storage.
     - 
       * :ref:`aws-hybrid`
       * :ref:`gcp-hybrid`
       * :ref:`azure-hybrid-manual`
   * - Object Storage
     - Read or Read/Write access to existing object storages (AWS S3, GCP Cloud Storage, Azure Blob Storage).
     - Configured in-app: :ref:`cloud-storage`
   * - Git repository
     - SSH or Deploy key with read-only acccess to select repositories.
     - Configured in-app: :ref:`repository`
   * - Docker Registry
     - Permissions to pull from your Docker repository.
     - Configured in-app:  :ref:`docker-private-registries`
   * - Kubernetes Cluster
     - A Kubernetes service account that can manage pods and other resources in a defined namespace. Permissions to read/write to your private Docker registry.
     - `Configuration guide </howto/setup/deployment/existing-cluster/>`_ 
