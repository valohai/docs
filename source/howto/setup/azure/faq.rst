:hide-toc:

.. meta::
    :description: Frequently asked questions on deploying Valohai to Azure.


Frequently Asked Questions
###########################

.. include:: ../_common-faq.rst

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
     - By default Valohai doesn't attach any service account to the virtual machines that are created for a job. However, you can define a set of service accounts and then configure Valohai environments to use them. For example, you can create a Valohai environment that spins up a ``Stamdard D2s v3`` with access to production CosmosDB in  ``East US``.
   * - Can we limit user access to certain machine types?
     - Yes. Each Valohai environment can be owned by an individual user, a team, or the whole organization. For example, you could limit access to a specific GPU type to a certain team.
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
   * - How do we connect our existing Azure Blob Storage Bucket to Valohai?
     - Valohai Data stores can be configured through the user interface. You can configure either project-specific data stores, or data stores that are shared with the whole organization. See the guide: :ref:`howto-data-azure`
   * - Can we mount large files and storage?
     - Yes. Valohai supports mounting storage over NFS and directly using GCP Filestore. See the guide :ref:`howto-mount-nfs`