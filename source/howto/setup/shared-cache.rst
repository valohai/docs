.. meta::
    :description: Setting up a shared network cache for your Valohai workers 

.. _setup-shared-cache:

Setting up a shared cache for Valohai workers
##############################################

Most of your Valohai machine learning jobs have a set of input files that are downloaded from a cloud object storage like AWS S3, Azure Blob Storage, or GCP Cloud Storage. This data is downloaded on each of the virtual machines that are running your jobs.

* By default each Valohai worker (virtual machine) will have its own cache where the downloaded data is stored.
* When the machine is no longer used (after a configurable grace period) it gets scaled down, and with it the local cache gets removed.
* The next time a machine gets scaled up it will download the input files to its own cache.

Valohai has the option to setup a shared network cache between several worker machines.

In this case the input data is stored on an NFS or SMB network mount from where the workers can fetch the data, instead of always redownloading the data from cloud storage.

This is for example useful when:

* You have large datasets (50GB+) that you access often from different workers.
* You're running Valohai Tasks where you have multiple parallel (GPU) instances that download the same dataset from a cloud object storage.
* You have TBs of data that takes a long time to download from your object storage.

.. image:: /_images/shared_cache.png
    :alt: Shared NFS cache with workers
    :width: 350

.. admonition:: Input URLs
    :class: tip

    Users will still provide Valohai inputs by providing the URL to the file in your cloud storage as they would with a standard on-worker cache. Valohai will take care authenticating with your object storage, downloading the dataset on the shared cache, and versioning that input file with the execution in the same way as in standard executions.


Setup a shared cache
---------------------

You'll need to configure your network mount (NFS or SMB) either in your cloud or on-premises. 

The main thing to verify is that the workers can access the network mount.

After completing your network mount configuration you'll need to send your Valohai contact the address of the network drive, so it can be configured with the relevant Valohai workers.

Configure a network file system
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab:: AWS Elastic File System

    You can either use an existing one or create a new EFS. 

    .. tip:: 

        * Create your EFS in the same VPC where all Valohai resources are in or `setup VPC peering between the two VPCs <https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access-vpc-peering.html>`_ 
        * Select a region where your workers are stored

.. tab:: GCP Fileshare

    You can either use an existing one or create a new GCP Fileshare. 

    .. tip:: 

        * Create your Filestore in the same VPC where all Valohai resources are in.
        * Make sure grant access to all clients on the VPC network



Send details to Valohai
^^^^^^^^^^^^^^^^^^^^^^^^

To update your worker configuration you'll need to send the following information to your Valohai contact:

* The address of the NFS drive and the name:
* 
  * AWS Example: ``fs-1234aa12.efs.eu-west-1.amazonaws.com:/``
  * GCP Example: ``10.123.12.123:/my_valohai_cache``

* List of environment you want to configure to use the shared NFS cache

  * You can either choose specific environment, or configure all of your environments to use the shared cache
  * Optional: Each environment can be configured to copy data from the NFS on the virtual machine before starting a job. By default it will not copy the data to a local directory but directly access it from NFS.
