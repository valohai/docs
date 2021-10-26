:hide-toc:


.. meta::
    :description: How to manually deploy Valohai resources in your GCP project

.. _gcp-hybrid-manual:


Deploy to GCP manually
######################

.. include:: _intro.rst

.. warning::

    Before running the template you'll need the following information from Valohai:

    * ``queue_address`` that will be used for your queue
    * ``valohai_email`` of the account Valohai will use to assume the generated service account in your GCP.


Configure the IAM Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start by creating a new role in your GCP Project `IAM & Admin -> Roles <https://console.cloud.google.com/iam-admin/roles>`_

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Property
     - Value
   * - Title
     - ``ValohaiMaster``
   * - Description
     - A role used by app.valohai.com to manage Valohai related resources
   * - ID
     - ``ValohaiMaster``
   * - Role launch stage
     - General Availability
   * - Permissions
     - 
       * ``compute.disks.create``
       * ``compute.disks.delete``
       * ``compute.disks.setLabels``
       * ``compute.instances.create``
       * ``compute.instances.delete``
       * ``compute.instances.list``
       * ``compute.instances.setLabels``
       * ``compute.instances.setMetadata``
       * ``compute.instances.setServiceAccount``
       * ``compute.instances.setTags``
       * ``compute.subnetworks.use``
       * ``compute.subnetworks.useExternalIp``
       * ``compute.zones.list``


Next create two new `Service Accounts <https://console.cloud.google.com/iam-admin/serviceaccounts>`_

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Property
     - Value
   * - Name
     - ``valohai-sa-master``
   * - Description
     - Used to manage Valohai related VM resources in the project
   * - Roles
     - 
       * ``Compute Viewer``
       * ``Service Account User``
       * ``Secret Manager Secret Accessor``

         * **Title:** Only Valohai secrets
         * **Condition Editor:** 
         
           .. code-block::
             
            resource.name.extract('/secrets/{name}/versions/') == "valohai_redis_password" ||
            resource.name.extract('/secrets/{name}/versions/') == "valohai_master_sa_key"

           ..
       * ``ValohaiMaster``

         * **Title:** Only Valohai managed VMs
         * **Condition Editor:** 
         
           .. code-block::
             
            resource.name.extract("instances/{name}").startsWith("valohai") ||
            resource.name.extract("disks/{name}").startsWith("valohai") || 
            resource.name.extract("subnetworks/{name}").startsWith("valohai")

           ..
   * - Grant access
     - Add the ``valohai_email`` you received a ``Service account user``

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - Name
     - ``valohai-sa-queue``
   * - Description
     - Service account used by the Valohai queue virtual machine
   * - Roles
     - 
       * ``Service Account User``
       * ``Secret Manager Secret Accessor``

         * **Title:** Only the Valohai redis password
         * **Condition Editor:** 
         
           .. code-block::
             
            resource.name.extract('/secrets/{name}/versions/') == "valohai_redis_password"

           ..

Deploying resources
^^^^^^^^^^^^^^^^^^^^

Secret Manager
---------------

You'll need to upload two secrets for Valohai:

* ``valohai_redis_password`` as the password that will be set on the job queue machine. Your workers and app.valohai.com will need this to be able to access the job queue.
* ``valohai_master_sa_key`` will be used by the Valohai autoscaler to create and delete virtual machine resources for your Valohai machine learning jobs.

Start by going to the  `IAM -> Service Accounts <https://console.cloud.google.com/iam-admin/serviceaccounts>`_ page and opening ``valohai-sa-master``. 

Go to the ``KEYS`` tab and create a new JSON key. The key will be downloaded to your workstation.

Next go to the `Security -> Secret Manager <https://console.cloud.google.com/security/secret-manager/>`_ and create the two secrets:

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Name
     - Secret value
   * - valohai_redis_password
     - ``Generate a random password, that includes lowercase and capital letters and numbers.``
   * - valohai_master_sa_key
     - ``Paste the JSON contents of the key file you just downloaded``

VPC
---

Start by creating a new VPC in your GCP Project `VPC -> VPC networks <https://console.cloud.google.com/networking/networks/>`_

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Property
     - Value
   * - Name
     - ``valohai-vpc``
   * - Subnet creation mode
     - Automatic

Firewall Rules
---------------

Next open the `VPC -> Firewall <https://console.cloud.google.com/networking/firewall/>`_ and create two firewall rules

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Property
     - Value
   * - Rule name
     - ``valohai-fr-queue-redis``
   * - Description
     - Allows connection to the queue from Valohai services and valohai workers from this project.
   * - Network
     - ``valohai-vpc``
   * - Direction
     - Ingress
   * - Action on match
     - Allow
   * - Target tags
     - ``valohai-queue``
   * - Source IP Ranges
     - 
       * ``34.248.245.191/32``
       * ``63.34.156.112/32``
   * - Second soruce filter / Source tags
     - ``valohai-worker``
   * - Specified protocols and ports
     - TCP on port ``63790``

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Property
     - Value
   * - Rule name
     - ``valohai-fr-queue-http``
   * - Description
     - Allows connections on port 80 for the Let's Encrypt HTTP challenge
   * - Network
     - ``valohai-vpc``
   * - Direction
     - Ingress
   * - Action on match
     - Allow
   * - Target tags
     - ``valohai-queue``
   * - Source IP Ranges
     - ``0.0.0.0/0``
   * - Specified protocols and ports
     - TCP on port ``80``

Virtual Machine
---------------

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Property
     - Value
   * - Name
     - ``valohai-queue``
   * - Region
     - Choose your region and zone
   * - Type
     - ``e2-medium``
   * - Boot disk
     -        
       * **Operating system:** Ubuntu
       * **Version:** Ubuntu 20.04 LTS
       * **Boot disk type:** SSD persistent disk
       * **Size (GB):** 16
   * - Identity and API access
     - **Service Account:** ``valohai-sa-queue``
   * - Networking
     - 

       * **Network tags:** ``valohai-queue``
       * **Network interface:** ``valohai-vpc``
       * **External IP:** Create IP Address ``valohai-ip-queue``
   * - Management 
     - Startup script:
     
       **IMPORTANT:** Replace the ``<queue_address>`` with value you got from Valohai.
     
       .. code-block:: bash

           export QUEUE=<queue_address>
           export PASSWORD=`gcloud secrets versions access 1 --secret="valohai_redis_password"`
           curl https://raw.githubusercontent.com/valohai/worker-queue/main/host/setup.sh | sudo QUEUE_ADDRESS=$QUEUE REDIS_PASSWORD=$PASSWORD bash
           unset PASSWORD

Next steps
-----------

You'll need to share the following details with your Valohai contact, so they can finish the setup on app.valohai.com and enable your organization's environments on the platform:

* ``External IP`` of the ``valohai-queue`` virtual machine
* ``Project ID``

