:orphan:

.. meta::
    :description: How to prepare your GCP environment for a Valohai Private Workers installation


Preparing your GCP for Valohai Worker Setup
#################################################

This document prepares your GCP account for Valohai worker installation.


Select the correct region
--------------------------

Select the appropriate region for the resources:

* Consider using the same region where your data is located to reduce data transfer times.
* Consider using the regions where you've already acquired GPU quota from GCP.
* When selecting your region, note that regions have different collections of available GPU types.

You can see the available regions at `GCP Regions <https://cloud.google.com/compute/docs/regions-zones/>`_.

.. admonition:: Setting a dedicated GCP Project
    :class: tip

    You can create a dedicated GCP Project for all the Valohai resources. This way all the Valohai resources will be seperated from all the other GCP services you might be using.


Creating IAM Entities
------------------------------------

Valohai requires a service account that has permissions to manage the compute resources in your subscription.

These are credentials are used by the Valohai services at https://app.valohai.com/ to: 

1. Be able to see how many Valohai-related instances are running, and 
2. Allow scaling worker clusters up and down.

Create a new service account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Go to `IAM & admin > Service accounts > Create service account`

* **Name:** valohai-sa-master
* **Description:** Service account for starting and stopping Valohai workers.
* **Role:** "Compute Admin"
* Create a key in JSON format

Take note of the JSON and send it back to the Valohai engineers over https://aarrearkku.valohai.com. You'll receive the credentials from your Valohai contact.


.. admonition:: Assigning a Service Account to an VM Instance
    :class: tip

    By default, Valohai doesn't assign a service account to the instances that it spins up. 
    
    You'll need to give an aditional role :code:`Service Account User` to :code:`valohai-sa-master`, if you'd like Valohai to assign a service account to workers that are created.
    
    You'll be able to define different service accounts for different Valohai environments.

.. 

.. admonition:: Using TPU instances
    :class: note

    You can use TPUs with your Valohai instances.
    
    For this we suggest to create a seperate service account that has the roles to request a TPU (:code:`TPU Admin`) and access the Google Cloud Storage you're looking to use (or :code:`Storage Object Admin` permissions).
    
    You don't need to share the key of this service account with Valohai as it will be assigned on the worker that will request a TPU.

..

Setting up Valohai resources
------------------------------

Below is a list of the GCP resources that are required for the Valohai Private Worker installation.

You can either create these resources yourself, or give the Valohai team temporary elevated permissions for the setup.

Option 1) Give Valohai permission to provision the resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Valohai engineers require access to your GCP Project for the setup of the VPC Network and compute instances needed to run Valohai workers in your project.

This access can be restricted after the initial installation.

**Create a role (ValohaiAdmin)**

This role is needed for:
  - Setup the private cloud and subnets for the VM resources.
  - Setup one job queue and logging Redis server.
  - Reserve one external IP for that Redis server.
  - And the related key pairs for SSH access.

Create a new role under IAM & Admin -> Roles

* **Name:** ValohaiAdmin
* **Assign the following permissions:**
    * :code:`compute.addresses.create`
    * :code:`compute.firewalls.create`
    * :code:`compute.networks.create`
    * :code:`compute.networks.updatePolicy`
    * :code:`compute.subnetworks.create`

**Add new members**

Go to IAM & Admin -> IAM and add a new member

* New members: valohai.com
* Add the following roles:
    * :code:`Project Viewer`
    * :code:`Compute Instance Admin (v1)`
    * :code:`ValohaiAdmin`

Option 2) Provision the resources yourself
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

VPC and subnets
^^^^^^^^^^^^^^^^

Create a VPC and subnets. For example:

**VPC**

* **Name:** valohai-vpc
* **CIDR:** 10.0.0.0/16
* **Dynamic Routing Mode:** Regional

**Subnet**

* **Name:** valohai-subnet-us-central1
* **Region:** us-central1
* **CIDR:** 10.0.0.0/20

Firewall rules
^^^^^^^^^^^^^^^^

.. list-table::
    :header-rows: 1
    :widths: 25 30 10 5 5 10 10 5

    * - Name
      - Description
      - Network
      - Direction
      - Action
      - Targets
      - Source
      - TCP
    * - valohai-fr-queue-external
      - Redis over SSL from Valohai
      - valohai-vpc
      - Ingress
      - Allow
      - valohai-queue (target networking tag)
      - 34.248.245.191/32, 63.34.156.112/32 (IP range)
      - 63790
    * - valohai-fr-queue-ssh
      - for SSH management from Valohai
      - valohai-vpc
      - Ingress
      - Allow
      - valohai-queue (target networking tag)
      - 3.251.38.215/32 (IP range)
      - 22
    * - valohai-fr-queue-acme
      - for acme tooling and cert renewal
      - valohai-vpc
      - Ingress
      - Allow
      - valohai-queue (target networking tag)
      - 0.0.0.0/0
      - 80, 443
    * - valohai-fr-queue-internal
      - for plain Redis from workers
      - valohai-vpc
      - Ingress
      - Allow
      - valohai-queue (target networking tag)
      - 10.0.0.0/20 (IP ranges of subnets used for workers)
      - 63790

VM Instance for queue machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Provision an External IP and a Virtual Machine instance for storing the job quue and short term logs.

Create an External IP:

* **Name:** valohai-ip-queue-us-central1
* **Network Service Tier:** Premium
* **IP Version:** IPv4
* **Type:** Regional
* **Region:** us-central1

Create an VM Instance:

* **Name:** valohai-i-queue-us-central1
* **Region:** us-central1
* **Zone:** us-central1-c
* **Machine Type:** n1-standard-1
* **OS:** Ubuntu 20.04 LTS
* **Disk:** Standard persistent disk 16GB
* **Service Account:** No service account
* **Advanced settings > Networking:**
    * Network tags: valohai-queue
    * Network interfaces:
        * VPC_NAME, valohai-subnet-us-central1
        * Primary internal IP: Ephemeral (Custom): 10.0.10.10
        * External IP: valohai-ip-queue-us-central1

Conclusion
-------------

You should now have the following details:

* GCP Project ID and Name
* Region
* JSON Key for the service account valohai-sa-master
* A ValohaiAdmin role and access to valohai.com users (if you'd like Valohai to setup the resources for you)

If you created the above mentioned resources yourself, you should also send the following information:

* Name of VPC
* Name(s) of subnet(s) that can be used for Valohai workers
* External IP of the queue instance
* Internal IP of the queue instance
* (optional) Service Account you'd like to attach to the Valohai workers

Share this information with your Valohai contact using the Vault credentials provided to you.


.. seealso:: 

    Each Valohai project has one or more data stores. A data store is a secure place to keep your files; you download training data from there and upload files from your executions there (e.g. models, weights, images).

    It's good practice to setup one Google Cloud storage Bucket to work as the default bucket for all projects in your organization. Each project owner can then change the bucket if needed, but this way you can ensure that all data ends up in your bucket, instead of the shared Valohai storage.

    `Add Google Cloud Storage to Valohai </tutorials/cloud-storage/private-gcp-bucket/>`_
