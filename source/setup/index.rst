.. meta::
    :description: Setup instructions for Valohai
    
******************************************************************
Running Valohai Inside Your Own Cloud or On-premise Environment
******************************************************************

.. seealso::
    .. toctree::
        :maxdepth: 2
        :titlesonly:

        environments
        setup_options
        on-premises/index

..


1. Installing Valohai
#################################

Valohai can be installed on both cloud (Microsoft Azure, AWS, GCP) and on-prem servers, or a combination of them.

There are several ways to install Valohai. The most popular options are:

1) **Valohai Private Workers** - In which Valohai manages a set of worker machines in your subscription. These machines fetch data from your private data stores and run executions (e.g. pre-processing, training, batch inference) on the workers. Therefore data stays inside your subscription environment.
    
    Valohai will host the app.valohai.com web application and will store execution logs, code snapshots and user management data on Valohai servers.
2) **Valohai Full Private** - A fully custom installation of Valohai in your environment, and optionally inside your own private network. All Valohai services are hosted in your environment (AWS, GCP, Azure, on-prem) including the web app, core Valohai services, logs, snapshots etc.

👉 Read more about `setup options </setup/setup_options>`__.

.. container:: alert alert-warning

    **Use your existing cloud benefits** 

    You might have discounted pricing, credits or other deals with your cloud provider. Valohai worker machines run inside your cloud subscription, so their billing will be according to the pricing that you have from cloud provider.

..

2. Environment Checklist
###############################

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
    * Read more about `Selecting compute instances </setup/environments>`__

.. container:: alert alert-warning

    **On-premise and full-private installations**

    We recommend providing ssh access to the Valohai engineering team to ensure a smooth and easy installation in your private environment. This access can be revoked after the installation period or provided on a per-request basis after the installation.

..

3. Successful Valohai Onboarding
##################################

Our Customer Success team will be there to help you to bring your team and projects to Valohai, and start running your experiments. Together you'll start by:

* 👉 **Clear the items from our** `check-list <#environment-checklist>`_.
* 👉 **Set clear goals for the onboarding.** Feel free to use our `Valohai POC kick-off template <https://get.valohai.com/poc-kickoff>`_ as a base for your planning.
* 👉 **Select an existing project for Valohai onboarding.** We can run everything with our `sample-projects </quickstarts/>`_ but it's recomended to onboard your real-life project to get the most out of the onboarding and understand how Valohai fits into your workflow.
* 👉 **Setup a joint communication channel.** Our success team sets up a private Slack/Microsoft Teams channel for all Valohai customers. The channel is a great place to ask questions and share feedback.
* 👉 **Schedule catch up calls.** Monthly catch up calls allow us to dig a bit deeper into your projects, share best practices, and discuss the Valohai roadmap.
* 👉 **Get hands-on with Valohai.** We want to ensure you get value out of Valohai from day one. In our hands-on session we'll give you an overview of Valohai and have you running experiments, pipelines and parameter sweeps like a pro.
    Check out the sample agenda below:

Sample Agenda of a Valohai Onboarding Session
***********************************************

* **Refresh on Valohai platform and capabilities** (10min)
* **Hands-on with Valohai** | Hands-on on your computer (1h 15min)
    * This will be focused on the Valohai command-line tools to give you a better understanding of the platform. We'll create a sample project and run it on Valohai with data inputs, outputting model files, collecting metrics from executions, etc. We'll run these experiments on your cloud/on-prem machines running in the Valohai subscription.
* **Bringing your project to Valohai** (1h 30min)
    * Launching Valohai executions from Notebooks using `Jupyhai </quickstarts/quick-start-jupyter/>`_
    * Connecting a private Git repository to Valohai
    * Using customer Docker image for the project 
    * Running the project in different cloud virtual machines (CPU & GPU)
    * Downloading data from your cloud storage to Valohai execution
    * Upload data to your cloud storage from Valohai executions
    * Collect & visualize key metrics on Valohai
    * Running parameter sweeps and hyperparameter optimization in Valohai
    * Chaining executions with Valohai pipelines
    * Using Valohai APIs to automate steps

.. thumbnail:: onboarding.png
  :width: 500
  :alt: Onboarding process