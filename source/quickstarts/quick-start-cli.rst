.. meta::
    :description: Everything in Valohai deep learning platform works through an API. Learn how to setup and optimize deep learning experiments with command-line client that supports Python 2.7 or Python 3.4 and higher.

Quick Start - Command-line Client
---------------------------------

In this tutorial, we will use `Valohai command-line client <https://github.com/valohai/valohai-cli>`_ to bootstrap a fresh project.

.. contents::
   :backlinks: none
   :local:

1. Requirements
~~~~~~~~~~~~~~~

``valohai-cli`` supports Python 3.4+ and works on macOS, Windows and Linux.

.. code-block:: bash

   $ pip3 install valohai-cli  # (or pip2)

   # and test that it works, `vh` should print available commands
   $ vh

2. Sign in
~~~~~~~~~~

If you don't already have an account, sign up at `the Valohai platform <https://app.valohai.com/>`_.

After that, you can use ``vh login`` to login with the command-line client. Just follow the instructions.

3. Create new project and configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next we'll use the ``vh init`` wizard to create a new project on Valohai
and bootstrap the ``valohai.yaml`` configuration file.

The configuration will have a single **step** named 'Execute nvidia-smi' that
simply prints the status of the server GPU using the ``nvidia-smi`` tool.

.. code-block:: bash

   $ mkdir test-project
   $ cd test-project
   $ vh init

   # Hello! This wizard will help you start a Valohai compatible project.
   # First, let's make sure /Users/user/test-project is the root directory of your project.
   # Is that correct? [y/N]:
   y

   # Looks like you don't have a Valohai.yaml file. Let's create one!
   # We couldn't find script files in this directory.
   # Please enter the command you'd like to run in the Valohai platform.
   nvidia-smi

   # Is nvidia-smi correct? [y/N]:
   y

   # Success! Got it! Using nvidia-smi as the command.
   # Now let's pick a Docker image to use with your code.
   # Here are some recommended choices, but feel free to type in one of your own.
   # [  1] tensorflow/tensorflow:1.0.1-devel-gpu-py3
   # ...
   # Choose a number or enter a Docker image name.:
   1

   # Is tensorflow/tensorflow:1.0.1-devel-gpu-py3 correct? [y/N]:
   y

   # Success! Great! Using tensorflow/tensorflow:1.0.1-devel-gpu-py3.
   # Here's a preview of the Valohai.yaml file I'm going to create.
   # ...
   # Write this to /Users/user/test-project/valohai.yaml? [y/N]:
   y

   # Success! All done! Wrote /Users/user/test-project/valohai.yaml.
   # Do you want to link this directory to a pre-existing project,
   # or create a new one? [L/C]:
   c

   # Project name:
   test-project

   # Success! Project test-project created.
   # Success! Linked /Users/user/test-project to test-project.
   #
   # **********************************************************************
   # All done! You can now create an ad-hoc execution with
   #   $ vh exec run --adhoc --watch execute
   # to see that everything works as it should.
   # For better repeatability, we recommend that your code
   # is in a Git repository; you can link the repository
   # to the project in the Valohai webapp.
   #
   # Happy (machine) learning!
   # **********************************************************************

4. Create an execution
~~~~~~~~~~~~~~~~~~~~~~

Next we'll create an ad-hoc execution which packages the project directory,
sends the package to the Valohai platform and executes the command on a GPU-enabled machine in the cloud.

.. code-block:: bash

   $ vh execution run --adhoc --watch execute # replace with the name of your step
   # Packaging /Users/user/test-project...
   #   [########################################]  1/1
   # Uploading 0.30 KiB...
   # Success! Uploaded ad-hoc code ~cc9b9fcdb625f9b580
   # Success! Execution #1 created.
   # ...

You can stop watching the execution with ``Ctrl+C``. (This won't stop the execution itself, though.)
The execution should only take a second or two to finish if the used Docker image is already on the compute node.

You can see the status of the execution in the `web application <https://app.valohai.com/>`_
or with the command-line client.

.. code-block:: bash

   $ vh execution list
   # # | Status   | Step               | Duration   | URL
   # ----------------------------------------------------
   # 1 | complete | Execute nvidia-smi |    0:00:01 | https://app.valohai.com/...

   $ vh execution info 1
   # key                  | value
   # ----------------------------
   # command              | nvidia-smi
   # duration             | 1.2570652961731
   # environment name     | AWS eu-west-1 g2.2xlarge
   # image                | tensorflow/tensorflow:1.0.1-devel-gpu-py3
   # interpolated command | nvidia-smi
   # project name         | test-project
   # status               | complete
   # step                 | Execute nvidia-smi

   $ vh execution logs 1
   # 09:00:37.21 Starting job on i-0b79f3d49308ef2a8, Peon 0.8 (f89f4423)
   # 09:00:37.22 downloading repository (code)
   # 09:00:37.28 starting container...
   # 09:00:38.21 started container 04e3b6dbc on i-0b79f3d49308ef2a8
   # ...

   # And if your execution had produced output files, you could list them with:
   $ vh execution outputs 1
   # and download them into, say, the "my_files" directory with
   $ vh execution outputs 1 -d my_files

.. tip::

   All commands can be abbreviated as long as the abbreviation is unique.
   That is, ``vh execution logs 1`` can also be written ``vh exec logs 1`` or even ``vh ex lo 1``.

5. Next steps
~~~~~~~~~~~~~

Ad-hoc executions are convenient when developing your scripts and learning the platform but we strongly recommend
that you have your main machine learning code in a version control repository to allow better collaboration and
repeatability.

Check out :doc:`our quick start TensorFlow tutorial </quickstarts/quick-start-tensorflow>` to learn more about
adding a version control repository to your project.

The wizard created a ``valohai.yaml`` for us during the tutorial; you might want to know
:doc:`more how these configuration files work </valohai-yaml/index>`.
