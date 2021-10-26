:hide-toc:

.. meta::
    :description: Frequently asked questions on deploying Valohai to GCP.


Frequently Asked Questions
###########################

General
-----------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :stub-columns: 1

   * - Question
     - Answer
   * - Can we use our on-premises machines with Valohai?
     - Yes. Most of our on-premise workers are running Ubuntu 18.04 or higher, but we support other Linux distributions also. The machine will need Python 3.6 or higher, Docker, and the Valohai agent ("Peon") installed, so it knows how to read jobs from Valohai and handle commands.
      
       Valohai doesn't need direct access to the on-premises machine but the on-premises machine needs outbound access to your job queue virtual machine.
   * - What are Valohai workers?
     - Valohai workers are virtual machines used to run machine learning jobs (e.g., data preprocessing, training, evaluation) that a user launches from Valohai. These machines are created and terminated according to the scaling users your organization defines in the Valohai web app (e.g., min scale, max scale, shutdown grace period)
   * - What's the purpose of the static (job queue) virtual machine?
     - The Valohai queue machine keeps track of your jobs. Valohai will write a record about incoming jobs, and the workers will fetch their jobs that have been scheduled for their queue. Each worker will then write execution logs back to the queue machine, from where app.valohai.com will read them and show them in the user interface.
   * - Can we use private Docker images?
     - Yes. Valohai supports standard docker login (username/password) and the main cloud providers. See the guide: :ref:`docker-private-registries`
   * - Does Valohai support SSO login?
     - Yes. Valohai supports Okta, SSO, SAML, and AzureAD authentication.

Network and security
-----------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :stub-columns: 1

   * - Question
     - Answer
   * - Can we deploy to an existing VPC?
     - Yes. You can either create a dedicated VPC for Valohai, or use an existing one. Valohai will just need to know which VPC and subnet(s) it's allowed to use.

       We highly recommend creating a dedicated environment for running a Valohai trial, as it's usually the fastest way to evaluate the platform. 
   * - Can we access our existing databases and data warehouses?
     - Yes. Valohai will spin all workers inside your VPC in the defined subnets. You'll be able to access your data sources, as long as they are accessible from the workers.
   * - We have a self-hosted Git-repository. How can we access it from Valohai?
     - app.valohai.com will need to be able to access your self-hosted Git-repository. You should whitelist the IP ``34.248.245.191``

       If whitelisting is not possible, we suggest looking into the self-hosted option of Valohai.
   * - What ports do we need to open for Valohai?
     - app.valohai.com (``34.248.245.191``) will need to access your:
     
       * Data Stores (443)
       * Your job queue machine (63790 with Redis over SSL)
       * Git repository (443, 22)
   * - What permissions do the Valohai managed virtual machines have?
     - By default Valohai doesn't attach any service account to the virtual machines that are created for a job. However, you can define a set of service accounts and then configure Valohai environments to use them. For example, you can create a Valohai environment that spins up a ``e2-standard-8`` with access to production BigQuery in  ``us-east1-b``
   * - Can we limit user access to certain machine types?
     - Yes. Each Valohai environment can be owned by an individual user, a team, or the whole organization. For example, you could limit access to a specific GPU type to a certain team, or limit machines and an data stores in a specific GCP project to a specific set of users.
   * - Why does Valohai need the service account key of ``ValohaiMaster``?
     - The key is used by the Valohai scaling service to create and delete virtual machines for Valohai jobs. The key is also used by the core Valohai service to provide presigned temporary keys to the workers, so they can download data from the Google Cloud Storage.
   * - How can we securely share credentials and keys with Valohai?
     - You share credentials securely to Valohai through our self-hosted `Vault <https://www.vaultproject.io/>`_.
     
       You'll get your credentials from your Valohai contact.


Data
-----

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :stub-columns: 1

   * - Question
     - Answer
   * - How do we connect our existing Google Storage Bucket to Valohai?
     - Valohai Data stores can be configured through the user interface. You can configure either project-specific data stores, or data stores that are shared with the whole organization. See the guide: :ref:`howto-data-gcp`
   * - Can we access BigQuery data from Valohai? 
     - Yes. See the guide: :ref:`howto-data-bigquery`
   * - Can we mount large files and storage?
     - Yes. Valohai supports mounting storage over NFS and directly using GCP Filestore. See the guide :ref:`howto-mount-nfs`