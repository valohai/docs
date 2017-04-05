Core concepts
=============

.. contents::
   :backlinks: none
   :local:

Projects
~~~~~~~~

You work and collaborate on **projects**; a project is a digital space for tackling a specific machine learning problem.
If you have used GitHub, project is a lot like a repository.

Project is linked to one or more remote git repositories (not just GitHub).

These linked repositories define what kind of "experiments" will be executed in the context of that project
using :doc:`valoha.yaml configuration file </valohai-yaml>`.

Here are some more in depth example repositories:

* https://github.com/valohai/tensorflow-example
* https://github.com/valohai/keras-example
* https://github.com/valohai/darknet-example
* https://github.com/valohai/ladder

We also have `quick start tutorials </tutorials>`_ to get started right away.

Fire-and-forget style experimentation is also supported using
`our command line client <https://github.com/valohai/valohai-cli>`_.

Steps
~~~~~

Every **step** defines a separate type of execution such as feature extraction or training.

You execute a step that creates an execution. Steps are version controlled so executing any
past steps will work if the Docker image and inputs are still available.

:doc:`valoha.yaml documentation </valohai-yaml>` has more details how to define steps.

Executions
~~~~~~~~~~

Simply put, **execution** is one or more Linux commands ran on a remote server.

Running a step creates an execution and multiple executions can be based on the same step with various
parameter, input file or command differences.

I what kind of a context are the commands ran depends on three things:

1. *Environment* meaning the machine type; e.g. Amazon instance with 8 GPU cards
2. *Docker image* containing command line tools, libraries and frameworks
3. Your linked *repository* contents such as training scripts will be available at ``/valohai/repository``

.. container:: tips

   Tips:

   * You can use readily available images or provide URL your own.
     More about images in :ref:`yaml-image` section.
   * You can skip using version control by using `our command line client <https://github.com/valohai/valohai-cli>`_
     but then you miss all benefits of version control system.

An execution can be in one of six states:

* **created**: execution is not yet queued, most likely because you don't have enough quota and the system will
  wait one of your past executions to finish
* **queued**: execution is good to go but there are no free servers which means that either a new server is being
  launched or you'll have to wait for another execution to finish
* **started**: execution is currently running on an instance, you should see logs and metadata through web interface
* **error**: one of the execution commands failed, you should check the logs
* **stopped**: an user manually cancelled the execution through web interface or command line client
* **complete**: execution was ran successfully and results are visible through web interface and command line client

Everything your commands write to standard output e.g. ``print()`` or stderr is logged and visible in real-time
through our command line client and web app.

At the end of an execution, anything stored at ``/valohai/outputs`` directory will be uploaded.
This is the place to store your neural network weights and biases if you want to access them later.

Metadata
~~~~~~~~

You define **metadata** by writing JSON to standard output by e.g. ``print()`` in Python.

.. code-block:: json

   {"step": 190, "accuracy": 0.9247000813484192}
   {"step": 200, "accuracy": 0.9262000918388367}
   {"model_layout": "ReLU8x-3xELUx32-softmax8"}

Each metadata point also has automatically generated value ``_time`` which tells when was the metadata defined
in UTC string format e.g. ``2017-04-04T15:03:39.321000``.

You can generate real-time charts based on metadata which helps monitoring long trainings so you can stop them if
training doesn't converge well.

You can sort executions by metadata value at the web interface which is useful for e.g. finding training
execution with the highest prediction accuracy. Value of the latest instance of each key such as ``accuracy`` is used
for the sorting.

Tasks
~~~~~

**Task** is a collection of related executions.

The most common task is hyperparameter optimization where you execute a single step with various
parameter configurations to find the most optimal neural network layout, weights and biases.
