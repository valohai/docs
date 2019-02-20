.. meta::
    :description: What are Valohai executions? Run any data science code on the cloud.

Executions
==========

Simply put, an **execution** is one or more commands run on a remote server.

Running a step creates an execution; multiple executions can be based on the same step with varying parameters, input files, hardware or other execution configurations.

The context the commands are run in depends on three things:

1. **Environment** meaning the machine type and cloud.
   For instance, you might want to run neural net training on a high-end Amazon AWS instance with 8 GPU cards,
   but a feature extraction step might need a memory-heavy instance with no GPUs instead.
2. The **Docker image** containing main tools, libraries and frameworks.
3. The contents of a commit in your linked **repository**, such as training scripts.
   The commit's contents will be available at ``/valohai/repository``, which is also the default
   working directory during executions.

.. tip::

   * You can use ready available images or provide URL your own.
     More about images in the :ref:`yaml-image` section.
   * You can skip using version control by using :doc:`our command-line client </tutorials/quick-start-cli>`
     but then you miss all the benefits of version control system.

An execution can be in one of six states:

* **created**: The execution is not yet queued, most likely because you don't have enough quota and the system is waiting for one of your past executions to finish.
* **queued**: The execution is enqueued, but there are no free servers which means that either a new server is being launched or you'll have to wait for another execution (either your own or someone else's) to finish.
* **started**: The execution is currently running on an instance. You should see real-time logs and metadata through the web interface.
* **error**: The last of the execution commands failed; check the logs for more information.
* **stopping**: An user manually cancelled the execution through the web interface or command-line client.
* **stopped**: The execution has been successfully stopped by the platform.
* **complete**: The execution was ran successfully and its results are available through the web interface and command-line client.

Everything your commands write to the standard output or standard error streams is logged and visible in real-time
through our command-line client and web app.  That is, you can freely ``print()`` things and view them in the app.

At the end of an execution, anything stored in the ``/valohai/outputs`` directory will be uploaded to storage.
This is the place to store your neural network weights and biases if you want to access them later.
Everything else is thrown away at the end of an execution.
