.. meta::
    :description: Frequently asked questions about the Valohai machine learning platform. Contact us if you can’t find an answer to your question.
    :orphan:


Frequently Asked Questions
==========================


General
----------------------

* **Where do the Valohai executions run?**
    Valohai can be setup on your own cloud subscription, on-premises hardware or a combination, so you can leverage your existing resources. This way all the data and executions stay in your environment and your control.

* **My data can't be in the cloud. Can Valohai run on our on-premises hardware?**
    It definitely can! We can even setup a hybrid solution, giving you access to both your on-premises hardware and the scalability of the cloud. Reach out to our sales team to get started.

* **How do I install Valohai?**
    You can register for free on app.valohai.com to start using Valohai. Or reach out to our fantastic sales team to get Valohai installed in your environment.

* **How much does Valohai cost?** 
    Get started for free with model training and batch predictions. Check our Pro and Enterprise pricing for more features: https://valohai.com/pricing/

* **How do I get my existing project to Valohai?**
    You can easily take add your existing project to Valohai. You'll just need to add a ``valohai.yaml`` configuration file, describing what you want to run and your dependencies.

* **Does Valohai support GPU machines?**
    Yes. You can run executions either CPU or GPU machines on Valohai. The exact type will depend on your organization settings and cloud provider availability (AWS, Azure, GCP)

Executions
----------------------

* **What is the max number of trainings I can do at the same time?**
    This is a configurable setting per-instance-type with the default of 5 parallel executions on most environments. If you launch more executions than you have quota for, we will properly queue everything so executions do get ran when the previous ones finish.

* **Why do some of my executions get queued?**
    Each machine type on Valohai has a maximum scale setting that determines how many parallel executions can be ran on each machine type. The setting can be configured from your organization's environment settings, if you're running Valohai workers in your own cloud environment or on-premises hardware. If you're running on the Valohai environment, the default maximum setting is 5. Contact us at info@valohai.com if you require more.

* **Why does it sometimes take so long to start a execution machine?**
    When you launch an execution Valohai will check if there are any available machines running. If there are available machines it will use one of them, otherwise it will request a new machine. The machine will be available as soon as it's ready at the cloud provider.
    
    Sometimes your execution might be queued because all the available machines are being used and you'll have to wait for a machine to free up. You can adjust the min/max settings and the per user quota for each machine type, under your organization settings. If you set the minimum ammount of a machine type to 1 or above, we'll make sure there is always some machines running.

* **How do I install additional libraries, tools and other dependencies to my execution?**
    You can define multiple commands under the ``step.command`` section in your valohai.yaml configuration. For example:
    
        .. code:: yaml

            - step:
                name: train model
                image: python:3.6
                command:
                    - pip install mypackage1
                    - python train.py

        ..

* **My executions keep using an old version of the data. How can I clear the cache?**
    You can tell Valohai to clear the data cache by setting an environment-variable called ``VH_CLEAN`` in your ``valohai.yaml``, or in the web UI when creating an execution.

* **How do I change the default machine type for the executions in my project?**
    Each project has a setting for "Default environment" that you can set in the web UI, valohai.yaml config as ``environment:`` or with the ``-e`` flag  when running CLI.

* **How to define that my execution failed?**
    The individual command is considered to be successful if it returns error code 0. This is the standard convention for most programs and operating systems. Valohai will mark an execution as a failure if *the last* commands returns any other code than 0.
    
    The best approach to communicate what went wrong is to use ``STDERR`` which is visible on the execution **Logs** tab.

Development
----------------------
* **Do I need to commit and push after each code change?**
    Nope, you can use ``--adhoc`` runs to create one-off executions from local files. These ad-hoc executions allow quick iteration with the platform when you are still developing your whole pipeline. ``vh exec run --adhoc --watch name-of-your-step``

* **Which languages and libraries are supported?**
    Valohai is completely technology agnostic. You can develop in notebooks, scripts or shared git projects in any language or framework of your choice. 

* **How do I use my own Docker image?**
    Once you've published your Docker image, you can point your steps and deployments to it in your ``valohai.yaml``. If you've published the image in a private container registry remember to add your credentials under your organization settings

* **How can I access files from my Git repository?**
    The contents of your repository's commit are available at ``/valohai/repository``, which is also the default working directory during executions.

* **How do I ignore certain files when doing --adhoc executions from the command line? I don't want Valohai to upload venv/, datasets/ and other files every time I run an --adhoc execution?**
    Our command-line client ignores everything that git ignores so just add those to your ``.gitignore`` and you are good to go.

* **How can I do so that there are multiple ``valohai.yaml`` for different folders in a repo so that I don't have to split my different models in different repos?**
    For the time being, the easiest way to do this would be defining them all in the same ``valohai.yaml`` and just create more steps in there. We have currently no plans to change this behavior as it can get messy fast. We feel it is nicer to have all the Valohai specific configuration in one place.


Metadata
----------------------

* **How can I compare my experiments and models?**
    Valohai will collect and save all metadata that you print to the logs as JSON. You can then easily compare your executions by selecting multiple executions in your Executions view and selecting compare from the menu. Check our metadata guide for instructions on how to output metadata.

* **How can I collect metadata from my executions?**
    Valohai collects metadata from your executions by collecting JSON from the logs. For example in Python you can write ``json.dumps({"metadata1": str(value1, "metadata2": str(value2)})``.

Data
----------------------

* **How can I upload my data sets to Valohai?**
    You can easily upload files to your cloud storage from the Data-tab in your projects. The files get uploaded to your own cloud storage (AWS S3, Azure Blob Storage, GCP Buckets) or if you haven't configured one, they'll be uploaded to a Valohai owned data store from where only you will be able to access them.

* **Where do my execution outputs get stored?**
    Each project has a default upload store defined in the project's settings. This contains both the Valohai S3 bucket and your own configured data stores.

* **How do I access data sets and other files from my cloud storage?**
    Once you've define the Data Stores under your execution settings, you can easily access the files by defining them as inputs in your valohai.yaml configuration file as HTTP, HTTPS or cloud provider specific data stores (s3://, gs:// etc.)

* **How do I change where my output files are saved?**
    In your projects settings you can define the 'Default upload store'. The options are The Valohai owned S3 storage and all the Data Stores you've configured for your project.

Deployments
----------------------

* **How can I deploy my models for inference?**
    Depending on your case, you might use Valohai executions or Valohai deployments for running your predictions.
    
    * **Executions** are useful when you need to do batch predictions, don't need to have it serving results all the time and don't need to do the predictions on the spot. Maybe you run the predictions daily, weekly or monthly.
    * **Deployments** are great when you need a online prediction service that is constantly receiving requests from users and needs to do the prediction immediately.
        * You can easily deploy for online inference through Valohai. By default the deployments go on a Valohai owned Kubernetes cluster, but it can be configured to your own cluster as well. Follow our guide for detailed instructions.
        * Essentially add an ``endpoint`` to your ``valohai.yaml`` configuration, and write your serving code either as ``wsgi`` or run any custom command with ``server-command``.

* **How do I install additional libraries to deployments?**
    You can place a ``requirements.txt`` in the root of your folder, and Valohai will run ``pip install`` on it to install any missing Python dependencies.

* **What if I don't want to run a WSGI server?**
    Valohai endpoints can be served as a WSGI server but we also support a more generic ``server-command`` with which you can run any HTTP server. Just make sure you either use a Docker image with the all the required dependencies installed on it, or install them by placing a ``requirements.txt`` in the root of your folder. 

* **What if I want to authenticate users before?**
    Valohai doesn't provide built-in authentication functionality for deployments. If you want to expose your endpoint only to authenticated users consider writing the authentication logic inside your app, using an HTTP server that can do that for you or placing the cluster in a location where only authenticated users can access it.