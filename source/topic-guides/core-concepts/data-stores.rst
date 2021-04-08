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


Mounting a network file system (NFS)
---------------------------------------

.. admonition:: See also
    :class: seealso

    This feature is available for customers who are using their own cloud or on-premises workers.

..

Mounting gives you direct access to the network file system like `AWS EFS <https://aws.amazon.com/efs/>`_ or `GCP Filestore <https://cloud.google.com/filestore>`_, without having to download the files on your machine.

Valohai does not version or keep track of the changes made inside the mounted file system. The files that are created, edited, or deleted will not be versioned as part of a Valohai execution.

.. admonition:: NFS mounts are not version controlled
    :class: warning

    We strongly recommend using the Valohai inputs and outputs system, as they are versioned as a part of the execution.

    You can mount a filesystem to access a large dataset, run preprocessing operations, and output the processed dataset into Valohai Outputs before it's used further in the pipeline. This way the snapshot of the preprocessed data will be versioned.

..

In your ``valohai.yaml`` specify a new mount:

.. tab:: AWS Elastic File System

    .. code-block:: yaml
        :linenos:
        :emphasize-lines: 6,7,8,9

        - step:
            name: mount-sample
            image: python:3.7
            command:
                - ls -la /my-data
            mounts:
                - destination: /my-data
                  source: fs-1234aa62.efs.eu-west-1.amazonaws.com:/
                  type: nfs

    ..

.. tab:: GCP Filestore

    .. code-block:: yaml
        :linenos:
        :emphasize-lines: 6,7,8,9

        - step:
            name: mount-sample
            image: python:3.7
            command:
                - ls -la /my-data
            mounts:
                - destination: /my-data
                  source: <IP>:/mystore
                  type: nfs

    ..

.. tab:: On-premises worker

    .. code-block:: yaml
        :linenos:
        :emphasize-lines: 6,7,8

        - step:
            name: mount-sample
            image: python:3.7
            command:
                - ls -la /my-data
            mounts:
                - destination: /my-data
                  source: /path/to/directory/outside/container

    ..
