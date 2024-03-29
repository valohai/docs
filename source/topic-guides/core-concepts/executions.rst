.. meta::
    :description: What are Valohai executions? Run any data science code on the cloud.

.. _executions:

Executions
###########

We encapsulate machine learning workloads in entities called **executions**.
An execution is a similar concept as "a job" or "an experiment" in other systems,
emphasis being that an execution is a smaller piece in a much larger data science process,
be it experimental or well defined production computation.

But, simply put, an execution is one or more strictly defined commands ran on a remote server.

Running a step creates an execution;
multiple executions can be said to implement the same step with
varying parameters, input files, hardware or other configuration.

The context in which the commands are run in depends on three main things:

1. **Environment** meaning the machine type and cloud.
   For instance, you might want to run neural net training on a high-end Amazon AWS instance with 8 GPU cards,
   but a feature extraction step might need a memory-heavy instance with no GPUs instead.
2. The **Docker image** containing main tools, libraries and frameworks. You can use images from public or private Docker repositories.
3. The contents of a commit in your linked **repository**, such as training scripts.
   The commit's contents will be available at ``/valohai/repository``, which is also the default
   working directory during executions.


.. seealso::

   * :ref:`workload-management`
   * :ref:`docker-private-registries`
