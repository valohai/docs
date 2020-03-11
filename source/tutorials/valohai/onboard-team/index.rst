.. meta::
    :description: Start using organization features on Valohai to enable collaboration and ensure compliance, tracability, and reproducability.

Onboard your team
==========================

Once your organisation is setup on Valohai, you'll be able to easily share projects within your teams.


☁️ Connect to a cloud storage 
-----------------------------

Configuring a data store will ensure that all your execution outputs will stay centralized inside your cloud subscription.

* Data Stores are defined for each project and each project can have one or multiple data stores.
* Access existing data from your cloud storage (*e.g. training data sets, labels etc.*)
* Upload new data from executions (*e.g. trained model, weights, metrics, graphics etc.*)
* The project's default upload store determines where to save output files


**Follow one of our tutorials below to setup your own data stores:**

* `Connecting to Azure Storage Account </tutorials/cloud-storage/private-azure-storage/index>`_
* `Connecting to Google Cloud Storage </tutorials/cloud-storage/private-gcp-bucket/index>`_
* `Connecting to AWS S3 </tutorials/cloud-storage/private-s3-bucket/index>`_
* `Connecting to OpenStack Swift </tutorials/cloud-storage/private-swift-container/index>`_


.. container:: alert alert-warning

    **Projects without a data store**

    * Valohai will upload execution outputs by default to the Valohai S3 Store, if a data store hasn't been configured for the project.
    * Only users with access to the project will be able to access data in the Valohai owned storage.
..

⚙️ Configure environment settings 
----------------------------------------------

Every time you run an execution or a task Valohai will either launch a new machine or use an already running one to run your execution.

Each machine type has it's own configuration:

* **Minimum Scale:** What's the minimum number of machines (of a certain type) that Valohai should keep running? By default this is set to 0.
    * If you set the minimum number to 1 (or greater) we'll make sure that there is constantly a machine available in your environment. This also means that your cloud provider will also charge you for having the machine running all the time.
* **Maximum Scale:** What's the maximum number of machines (of a certain type) that Valohai can run in parallel? By default this is set to 5.
    * After a maximum number of machines has been launched, new executions will get queued and executed once a machine frees up from a previous execution.
    * The maximum limit is also determined by the quotas/limits for virtual machines you have with your cloud provider.
* **Scale-Down Grace Period:** How many minutes should we wait after executions have completed to shut down the machine? By default 15min.
* **Per-User Quota:** You can limit how many machines (of a certain type) can a user run in parallel? By default this is 0 (no limit)

.. container:: alert alert-warning

    **Available only for Enterprise subscriptions**

    The environment settings are available only to customers who have Enterprise subscription and are using their own workers (cloud or on-prem).
..

🐳 Access Private Docker Repositories 
------------------------------------------------------

You can use custom Docker images from private repositories by providing the credentials in your organizations Registries settings.
Valohai executions support private repositories from Docker Hub and Azure Container Registry.

Create an `Access token on Docker Hub <https://docs.docker.com/docker-hub/access-tokens/>`_ or a `service principal for Azure Container Registry <https://docs.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal>`_ to generate credentials that Valohai can use to access your private repository.

1. Login at `<https://app.valohai.com>`_
2. Navigate to ``Hi, <name> (the top right menu) > Manage <organization>``. 
3. Go to **Registries** under the organization controls
4. Add a new entry
5. Insert the name in the format of *docker.io/myusername/** or *myregistry.azurecr.io/**.
6. Use the previously generated credentials as the username and password (Docker username and access token or Azure Service Principal credentials)

To use a private Docker image in your executions specify the image in the step of your ``valohai.yaml`` using the full name like ``docker.io/myusername/name:tag``.


🔑 Access Private GitHub Repositories 
---------------------------------------------------

You can easily configure Git repositories for each project. 

* For public repositories, you can just paste the HTTPS link to the repository to *Project->Settings->Repository*
* You can easily authenticate to private GitHub repositories using the app at *Project->Settings->Repository*

If you're connecting to a private repository:

* Generate an private SSH key pair on your machine with ``ssh-keygen -t rsa -b 4096 -N '' -f my-project-deploy-key`` will generate two files
* Add the generated public key (``my-project-deploy-key.pub``) to your source control (e.g. GitHub, GitLab, BitBucket)
* Get the *Clone with SSH* link to your repository from your source control
* Go to your project settings' Repository tab.
    * URL: Paste here the *clone with SSH* url
    * SSH Private Key: Copy & paste the generated private key contents (``my-project-deploy-key``)

**Follow our step-by-step guides to connect your private repository:**

* `Connect to GitHub </tutorials/code-repository/private-github-repository/index>`_
* `Connect to GitLab </tutorials/code-repository/private-gitlab-repository/index>`_
* `Connect to BitBucket </tutorials/code-repository/private-bitbucket-repository/index>`_


🗄 Reproducability and lineage 
-------------------------------------------

Valohai automatically keeps track of key information about your executions, making it easier to reproduce your experiments in the future and understand how they work.

Details on all past executions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* What code was ran to get the results of this execution?
    * For all executions that are based on a Git commit, Valohai will provide details of the commit and link back to it for details.
    * If the execution was ran as *--adhoc* or as a Notebook execution, you'll see ``adhoc`` under commit. Clicking the link will take you to details of the ``valohai.yaml`` configuration file, and allow you to download the code.
* Where the execution was ran (cloud or onprem) and what kind of hardware was used to run it?
* Which Docker image was used to run the execution?
* What was used as the input data for this execution? This could be for example training-data, labels etc.
* Commands that were executed (for example if you executed a ``pip install`` to install additional dependencies that are not part of the original Docker image.
* Who, when and how much did it cost?

Trace models and data files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to seeing the outputs of each execution, you can trace files that you've connected to Valohai (inputs/outputs). This allows you to easily see which executions and deployments are relying certain models, datasets or output files.

Tracing a file will create a graph for you, that'll show:

* How was this file generated? Which executions resulted in this file?
* Which executions and deployments are relying on this file?

Go to your project's data tab to see all your files and trace them.

Metadata
^^^^^^^^^^^^^

On top of all the data that Valohai is collecting about your executions, you can also easily create your own metadata from your executions.

* Metadata can be anything: performance metrics, details about the libraries you're using and anything else.
* This data is then visible on the Metadata tab inside each execution.

Use tags to easily identify certain executions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tags are useful when you for example want to highlight an execution that lead to an update in production. Or just wanto make it easier for your team members to find certain executions, so they don't want to scroll through hundreds of experiments you ran in the project.

Set tags at the bottom of each executions Details tab.


💡 Additional organisation settings
----------------------------------------------

There are a variety of other settings that you can manage for your organization:

* **Manage users and teams** inside you organisation
    * You can set project access and visibility to only to members of a certain team, instead the whole organisation.
* **Connect Valohai to Azure AD** and keep access control on Azure, avoiding access control setting duplication.
* **Require two-factor authentication** for all users in your organisation
* **Prevent users from running personal projects** under organisation execution environments



