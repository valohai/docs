.. meta::
    :description: How to deploy Valohai in your self-hosted environment

.. _selfhosted:

Deploy a self-hosted Valohai
############################

Valohai can be fully self-hosted, with all components of the service running inside your environment. This enables you to:

* Use your own virtual machines to run machine learning jobs.
* Use your own object storage (AWS S3, GCP Cloud Storage, Azure Blob Storage) for storing training artefacts, like trained models, preprocessed datasets, visualizations, etc.
* Access databases and date warehouses directly from the workers, which are inside your network.
* Host your own Valohai web application, scaling and deployment services, and databases.
* If needed, run everything in a fully isolated network.

The update schedule is of self-hosted installations is separate from the updates on app.valohai.com. You can view the latest `Valohai patch notes here <https://valohai.com/patch-notes/>`_.

.. image:: /_images/valohai_selfhosted_environment.png
    :width: 700
    :alt: Valohai Self-Hosted Components

Application Layer
-----------------

.. list-table::
   :widths: 15 45 40
   :header-rows: 1
   :stub-columns: 1

   * - Resource
     - Details
     - Requirements
   * - Virtual Machine
     - Running core Valohai services like the web application, autoscaling, and API services. The end-users will access the web application running on this instance (port 8000).
     - 

       * **OS:** Ubuntu 20.04 LTS
       * **vCPU:** 4, **Memory:** 16GiB
       * **Storage:** 80GB
   * - Object Storage
     - Valohai stores Git commit snapshots and execution logs in an object store to maintain reproducibility.
     - Storage size will depend on your datasets and commit sizes. Valohai is compatible with S3, GCP Cloud Storage, and Azure Blob Storage.
   * - Database
     - A relational database that contains user data and saves execution details such as which worker type was used, what commands were run, what Docker image was used, which inputs where used and what was the launch configuration.
     - 

       * **Database:** PostgreSQL 11.3
       * **vCPU:** 2, **Memory:** 8GiB
       * **Storage:** 80GB
   * - Redis
     - Stores information about the job queue and short-term execution logs so they can be shown on the web app and API in real-time. Each job is connected to a queue. The workers fetch a job from the Redis job queue based on their queue name.
     - 

       * **Database:** PostgreSQL 11.3
       * **vCPU:** 2, **Memory:** 8GiB
       * **Storage:** 80GB
   * - Load Balancer
     - The Valohai web application is served at port 8000 on the virtual machine.
     - HTTP/2 Enabled
   * - DNS Name
     - Provide DNS name to point at the load balancer (used for the web application e.g. valohai.yourcompany.net).
     - 

You'll also need to create the resources defined in the cloud specific guide of the cloud(s) you are using:

* :ref:`aws-hybrid`
* :ref:`gcp-hybrid`
* :ref:`azure-hybrid-manual`

Frequently Asked Questions
--------------------------

General
^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :stub-columns: 1

   * - Question
     - Answer
   * - Can Valohai run fully in our network?
     - Yes. All Valohai components including the web application and core services, can be self-hosted.
   * - Can we use our on-premises machines with Valohai?
     - Yes. Most of our on-premise workers are running Ubuntu 18.04 or higher, but we support other Linux distributions also. The machine will need Python 3.6 or higher, Docker, and the Valohai agent ("Peon") installed, so it knows how to read jobs from Valohai and handle commands.
   * - What are Valohai workers?
     - Valohai workers are virtual machines used to run machine learning jobs (e.g., data preprocessing, training, evaluation) that a user launches from Valohai. These machines are created and terminated according to the scaling users your organization defines in the Valohai web app (e.g., min scale, max scale, shutdown grace period)
   * - What's the purpose of the static (job queue) virtual machine?
     - The Valohai queue machine keeps track of your jobs. Valohai will write a record about incoming jobs, and the workers will fetch their jobs that have been scheduled for their queue. Each worker will then write execution logs back to the queue machine, from where app.valohai.com will read them and show them in the user interface.
   * - Can we use private Docker images?
     - Yes. Valohai supports standard docker login (username/password) and the main cloud providers. See the guide: :ref:`docker-private-registries`
   * - Does Valohai support SSO login?
     - Yes. Valohai supports Okta, SSO, SAML, and AzureAD authentication.
   * - How are Valohai updates delivered?
     - Each Valohai service (including the web app) runs inside a Docker container. To update your local version, you'll need to pull the latest Docker image.


Network and security
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :stub-columns: 1

   * - Question
     - Answer
   * - Can we deploy to an existing VPC?
     - Yes. You can either create a dedicated VPC for Valohai, or use an existing one. Valohai will just need to know which VPC and subnet(s) it's allowed to use.
   * - Can we access our existing databases and data warehouses?
     - Yes. Valohai will spin all workers inside your VPC in the defined subnets. You'll be able to access your data sources, as long as they are accessible from the workers.
   * - How do users access an existing Git-repository?
     - Users can either use the GitHub app, or authenticate using a read-only deploy key. Read details on how to guide: :ref:`repository`
   * - What permissions do the Valohai managed virtual machines have?
     - By default Valohai doesn't attach any service account to the virtual machines that are created for a job. However, you can define a set of service accounts and then configure Valohai environments to use them. For example, you can create a Valohai environment that spins up a ``Stamdard D2s v3`` with access to production CosmosDB in  ``East US``
   * - Can we limit user access to certain machine types?
     - Yes. Each Valohai environment can be owned by an individual user, a team, or the whole organization. For example, you could limit access to a specific GPU type to a certain team.
   * - What kind of data does Valohai collect?
     - Valohai collects anonymous usage data that is sent back to Valohai. Optionally a Sentry service can be configure to detect and help with platform issues.
   * - How can we securely share credentials and keys with Valohai?
     - You share credentials securely to Valohai through our self-hosted `Vault <https://www.vaultproject.io/>`_.
     
       You'll get your credentials from your Valohai contact.


Data
^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :stub-columns: 1

   * - Question
     - Answer
   * - How do we connect our existing Azure Blob Storage Bucket to Valohai?
     - Valohai Data stores can be configured through the user interface. You can configure either project-specific data stores, or data stores that are shared with the whole organization. See the guide: :ref:`howto-data-azure`
   * - Can we mount large files and storage?
     - Yes. Valohai supports mounting storage over NFS and directly using GCP Filestore. See the guide :ref:`howto-mount-nfs`
