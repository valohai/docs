.. meta::
    :description: Setup instructions for Valohai

.. _setup:

Running Valohai Inside Your Own Cloud or On-premise Environment
##################################################################

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :hidden:

    environments
    setup-options
    on-premises/index

Installing Valohai
--------------------------

Valohai can be installed on AWS, Microsoft Azure, GCP, OpenStack or on-prem servers, or a combination of these.

There are several ways to install Valohai. The most popular options are:

1) **Valohai Private Workers** - In which Valohai manages a set of worker machines in your subscription. These machines fetch data from your private data stores and run executions (e.g. pre-processing, training, batch inference) on the workers. Therefore data stays inside your subscription environment.
    Valohai will host the app.valohai.com web application and will store execution logs, code snapshots and user management data on Valohai servers.
2) **Self-Hosted Valohai** - A fully custom installation of Valohai in your environment, and optionally inside your own private network. All Valohai services are hosted in your environment (AWS, GCP, Azure, OpenStack, on-prem) including the web app, core Valohai services, logs, snapshots etc.

👉 Read more about `choosing the right Valohai environment </topic-guides/setup/setup-options.html>`__.

.. admonition:: Use your existing cloud benefits
    :class: tip

    You might have discounted pricing, credits or other deals with your cloud provider. Valohai worker machines run inside your cloud subscription, so their billing will be according to the pricing that you have from cloud provider.

..

Environment Checklist
-----------------------------

There are a couple of things to check in your environment, before you start with the Valohai installation. The Valohai team will provide additional details on the topics below and help you configure everything.

**1) Check access to your Git-repository** *(applies only to Private Worker installations)*
    * If your Git-repository is behind a firewall, you'll need to create a new firewall rule to whitelist the IP of app.valohai.com.
        * **Note:** You'll still use your own Git credentials to authenticate to the repositories. The firewall rule just allows Valohai to reach the server.
**2) Check access to your Docker-repository** *(applies only to Private Worker installations)*
    * If your Docker registry is behind a firewall, you'll need to create a new firewall rule to whitelist the IP of app.valohai.com.
        * **Note:** Valohai supports standard username/password authentication, used for it example to authenticate to DockerHub. In addition you can use the Container Registry from AWS, Azure or GCP.
**3) Check your cloud quota**
    * Ensure that you have enough CPU/GPU quota from your cloud service in your region.
    * `AWS EC2 Service Quotas <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html>`_ / `GCP Instance Quotas <https://cloud.google.com/compute/quotas#understanding_quotas>`_ / `Azure Service Quotas <https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits>`_
**4) Select the region for your services**
    * Consider using the same region where your data is located to reduce data transfer times.
    * When selecting your region, note that regions have different collections of available GPU types. We suggest the regions mentioned below, as they have the widest range of GPU machines available at the moment of writing.
        * **AWS:** *US West 2 (Oregon)* or *EU West 1 (Ireland)*
        * **Azure:** *East US* or *West US 2*
        * **GCP:**
            * US: *us-central1 (Iowa)* if you need to use TPUs or *us-west1 (Oregon)* if you want to use K80 and V100 GPUs.
            * Europe: *europe-west4 (Netherlands)* if need to use TPUs and V100 GPUs, or *europe-west1 (Belgium)* if you need to use K80 and P100 GPUs.
**5) Choose your machine instance types**
    * Depending on your scenario, you will need virtual machines with different CPU, memory, and GPU configurations for your work. Please choose the instance types you'd like to have available for your organization inside Valohai.
    * The list of available environments can be updated at any time to your subscription by our support team.
    * Read more about `Selecting compute instances </topic-guides/setup/environments>`__

.. admonition:: On-premise and self-hosted installations
    :class: tip

    We recommend providing ssh access to the Valohai engineering team to ensure a smooth and easy installation in your private environment.

    This access can be revoked after the installation period or provided on a per-request basis after the installation.

..
