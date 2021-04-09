.. meta::
    :description: What are Valohai data stores? Keep your training data secure and scalable.

Data Stores
#############

Each Valohai project has one or more **data stores**.

A data store is a secure place to keep your files; you download training data from there and upload your trained models to there.

Valohai supports the following data store types:

* AWS S3
* Azure Storage Account
* Google Cloud Storage
* OpenStack Swift

If you don't set a data store to your project, your files will be uploaded to a Amazon S3 bucket under Valohai account. The bucket is not public so your data is safe with us but we do recommend setting up your own private data store.

In addition to downloading files from data stores, you can also download from any public HTTP(S) address. For private installations, we also provide mount-based data ingestion options.

.. thumbnail:: data-stores.jpg
   :alt: You configure data stores per project-basis on Valohai.

.. seealso::

    * :doc:`/howto/data/cloud-storage/private-s3-bucket/index`
    * :doc:`/howto/data/cloud-storage/private-azure-storage/index`
    * :doc:`/howto/data/cloud-storage/private-gcp-bucket/index`
    * :doc:`/howto/data/cloud-storage/private-swift-container/index`

Data Version Control in Valohai
----------------------------------

Files managed by Valohai are fully version controlled.

If an execution uploads a new processed dataset, a model or any other file, it will never overwrite any previous files and will be stored indefinitely if not manually removed e.g. with our “purge” actions.

This feature is automatic if you use Data Stores we support: AWS S3, Azure Blob Storage, Google Cloud Storage or OpenStack Swift.

Changed input data files
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When data comes outside of the control of Valohai, we do our best to record and communicate if the input data has changed. Whenever you use a file in an execution, we note down and report what is the hash of the file (md5, sha1 and sha256).

For example:

.. code-block::

    16:05:40 /valohai/inputs/dataset/train-labels.gz: downloaded, 28.9 kB
    16:05:40 /valohai/inputs/dataset/train-labels.gz: md5 sum: f76a0d20f478ea899cb9ff102548d868
    16:05:40 /valohai/inputs/dataset/train-labels.gz: sha1 sum: aa3f7a65453085265b68d2b61c87e43a22667f76
    16:05:40 /valohai/inputs/dataset/train-labels.gz: sha256 sum:
    0994457350f18004649c30d884e5ff678cffc2fdb14966e4702cad5db409f78e

..

.. code-block::

    16:05:42 /valohai/inputs/dataset/train-images.gz: downloaded, 57.6 GB
    16:05:42 /valohai/inputs/dataset/train-images.gz: md5 sum: 2ea0f900d5bb5d6b5062f78dc93f1591
    16:05:42 /valohai/inputs/dataset/train-images.gz: sha1 sum: a0553c3d5cf68409da90344c4fe3b677d71b946b
    16:05:42 /valohai/inputs/dataset/train-images.gz: sha256 sum:
    079f59a474736c567ba3069ed22050fe7c07047e2b2dcaff3bc1e67ec8d13053

..

As changing of this hash doesn’t necessarily mean it’s undesired, Valohai only give you warnings in the user interface if an input file has changed since the last time you’ve used it as an input.

The execution will have an descriptive warning message associated with it in both the execution listing and execution details page.

.. seealso::

    * :ref:`howto-mount-nfs`