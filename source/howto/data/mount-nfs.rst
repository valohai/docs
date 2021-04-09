
.. meta::
    :description: How to mount a network file system (NFS) on Valohai workers

.. _howto-mount-nfs:

Mounting a network file system (NFS)
#######################################

.. note::

    This feature is available for customers who are using their own cloud or on-premises workers.

..

Mounting gives you direct access to the network file system like `AWS EFS <https://aws.amazon.com/efs/>`_ or `GCP Filestore <https://cloud.google.com/filestore>`_, without having to download the files on your machine.

Valohai does not version or keep track of the changes made inside the mounted file system. The files that are created, edited, or deleted will not be versioned as part of a Valohai execution.

.. admonition:: NFS mounts are not version controlled
    :class: warning

    We strongly recommend using the Valohai inputs and outputs system, as they are versioned as a part of the execution.

    You can mount a filesystem to access a large dataset, run preprocessing operations, and output the processed dataset into Valohai Outputs before it's used further in the pipeline. This way the snapshot of the preprocessed data will be versioned.

..

Define a mount in YAML
--------------------------------------------

.. note::

    Mounts are defined for each environment seperately. Contact Valohai, if you see an error ``mounts were ignored due to environment configuration.`` in your execution logs.

In your ``valohai.yaml`` specify a new mount:

.. tab:: AWS Elastic File System

    You can either use an existing, or create a new EFS. 

    .. tip:: 

        * Create your EFS in the same VPC where all Valohai resources are in or `setup VPC peering between the two VPCs <https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access-vpc-peering.html>`_ 
        * Make sure the security group of your EFS has an inbound rule to accept traffic from the Valohai workers (``sg-valohai-workers``)
        * Valohai will connect to the EFS over DNS name or IP address. Make sure the VPC has DNS hostnames and DNS resolution enabled, if you're connecting over DNS name.
    
    Example ``valohai.yaml`` configuration:
    
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
