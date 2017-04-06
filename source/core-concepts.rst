Core concepts
=============

.. contents::
   :backlinks: none
   :local:

Projects
~~~~~~~~

You work and collaborate on **projects**; a project is a space for tackling a specific machine learning problem or domain.
If you have used GitHub, projects in Valohai are a lot like code repositories.

Projects are linked to one or more remote Git repositories. You can use any Git hosting service, not just GitHub.

These linked repositories define what kind of "runs" can be executed in the context of that project
using the :doc:`valohai.yaml configuration file </valohai-yaml>`.

Here are some in-depth example repositories:

* https://github.com/valohai/tensorflow-example
* https://github.com/valohai/keras-example
* https://github.com/valohai/darknet-example
* https://github.com/valohai/ladder

We also have `quick start tutorials </tutorials>`_ to get you started right away.

Fire-and-forget style experimentation is also supported using
`our command line client <https://github.com/valohai/valohai-cli>`_,
try out :doc:`our quick start command-line client tutorial </tutorials/quick-start-cli>` to get a taste how it works.

Configuration File
~~~~~~~~~~~~~~~~~~

Each Valohai-enabled Git repository should have ``valohai.yaml`` **configuration file** that defines
what kind of runs can be executed. We'll cover these execution types or "steps", as we call them, in the next section.

A single configuration file can be used by multiple projects by various users, as long as the user
has access to the Git repository.

:doc:`More about valohai.yaml configuration file. </valohai-yaml>`

Steps
~~~~~

Every **step** defines a separate type of execution such as feature extraction or training.

You execute a step that creates an execution. Steps are version controlled so re-executing any
past steps will work as long as the Docker image and inputs are still available.

:doc:`valohai.yaml documentation </valohai-yaml>` has more details how to define steps.

Executions
~~~~~~~~~~

Simply put, an **execution** is one or more commands run on a remote server.

Running a step creates an execution; multiple executions can be based on the same step with various
parameter, input file or command configurations.

The context the commands are run in depends on three things:

1. *Environment* meaning the machine type and cloud.
   For instance, you might want to run neural net training on a high-end Amazon AWS instance with 8 GPU cards,
   but a feature extraction step might need a memory-heavy instance with no GPUs instead.
2. The *Docker image* containing tools, libraries and frameworks.
3. The contents of a commit in your linked *repository*, such as training scripts.
   The commit's contents will be available at ``/valohai/repository``.

.. tip::

   * You can use ready available images or provide URL your own.
     More about images in the :ref:`yaml-image` section.
   * You can skip using version control by using `our command line client <https://github.com/valohai/valohai-cli>`_
     but then you miss all the benefits of version control system.

An execution can be in one of six states:

* **created**: The execution is not yet queued, most likely because you don't have enough quota and the system is
  waiting for one of your past executions to finish
* **queued**: The execution is enqueued, but there are no free servers which means that either a new server is being
  launched or you'll have to wait for another execution (either your own or someone else's) to finish
* **started**: The execution is currently running on an instance. You should see real-time logs and metadata
  through the web interface.
* **error**: One of the execution commands failed; check the logs for more information.
* **stopped**: An user manually cancelled the execution through the web interface or command line client
* **complete**: The execution was ran successfully and its results are available
  through the web interface and command line client.

Everything your commands write to the standard output or standard error streams is logged and visible in real-time
through our command line client and web app.  That is, you can freely ``print()`` things and view them in the app.

At the end of an execution, anything stored in the ``/valohai/outputs`` directory will be uploaded to storage.
This is the place to store your neural network weights and biases if you want to access them later.
Everything else is thrown away at the end of an execution.

Metadata
~~~~~~~~

Execution **metadata** is output by writing lines of JSON to the standard output stream.

For instance, in Python,

.. code-block:: python

   import json

   print(json.dumps({"step": 190, "accuracy": 0.9247000813484192}))
   print(json.dumps({"step": 200, "accuracy": 0.9262000918388367}))
   print(json.dumps(({"model_layout": "ReLU8x-3xELUx32-softmax8"}))

.. code-block:: json

   {"step": 190, "accuracy": 0.9247000813484192}
   {"step": 200, "accuracy": 0.9262000918388367}
   {"model_layout": "ReLU8x-3xELUx32-softmax8"}

Each metadata point also has an implicit value ``_time`` which tells the metadata line was output.
The ``_time`` value is in UTC, formatted as an ISO-8601 datetime (e.g. ``2017-04-04T15:03:39.321000``).

You can generate real-time charts based on metadata which helps with
monitoring long runs so you can stop them if training doesn't converge well.

You can sort executions by metadata values in the web interface which is useful for e.g. finding training
executions with the highest prediction accuracy.

The latest or last value of each key such as ``accuracy`` is used for the sorting.

Tasks
~~~~~

**Tasks** are collections of related executions.

The most common task is hyperparameter optimization where you execute a single step with various
parameter configurations to find the most optimal neural network layout, weights and biases.
