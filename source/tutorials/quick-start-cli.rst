Quick start - command-line client
---------------------------------

In this guide we will use our `command-line client <https://github.com/valohai/valohai-cli>`_
to bootstrap a fresh project.

.. contents::
   :backlinks: none
   :local:

1. Installation
~~~~~~~~~~~~~~~

``valohai-cli`` supports Python 2.7 or Python 3.4 and higher. We recommend Python 3.

.. code-block:: bash

   $ pip3 install valohai-cli  # (or pip2)

   # and test that it works, `vh` should print available commands
   $ vh

2. Sign in
~~~~~~~~~~

If you don't already have an account, sign up at `the Valohai platform <https://app.valohai.com/>`_.

After that, you can use ``vh login`` to login with the command-line client, just follow the instructions.

3. Create new project and configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next we'll use ``vh init`` wizard to create new project on Valohai and bootstrap ``valohai.yaml`` configuration file.

The configuration will have a single **step** named 'Execute nvidia-smi' to see the status of the server GPU.

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
   # [  1] gcr.io/tensorflow/tensorflow:1.0.1-devel-gpu-py3
   # [  2] gcr.io/tensorflow/tensorflow:1.0.1-devel-gpu
   # [  3] gcr.io/tensorflow/tensorflow:0.12.1-devel-gpu-py3
   # [  4] gcr.io/tensorflow/tensorflow:0.12.1-devel-gpu
   # [  5] valohai/keras:2.0.0-tensorflow1.0.1-python3.6-cuda8.0-cudnn5-devel-ubuntu16.04
   # [  6] valohai/keras:2.0.0-theano0.9.0rc4-python3.6-cuda8.0-cudnn5-devel-ubuntu16.04
   # [  7] valohai/keras:2.0.0-theano0.8.2-python3.6-cuda8.0-cudnn5-devel-ubuntu16.04
   # [  8] valohai/darknet:b61bcf5-cuda8.0-cudnn5-devel-ubuntu16.04
   # Choose a number or enter a Docker image name.:
   1

   # Is gcr.io/tensorflow/tensorflow:1.0.1-devel-gpu-py3 correct? [y/N]:
   y

   # Success! Great! Using gcr.io/tensorflow/tensorflow:1.0.1-devel-gpu-py3.
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

Next we'll create an ad-hoc execution which packages the project directory, send the package to a remote server
and executes defined command on that server.

.. code-block:: bash

   $ vh execution run --adhoc --watch execute
   # Packaging /Users/user/test-project...
   #   [########################################]  1/1
   # Uploading 0.30 KiB...
   # Success! Uploaded ad-hoc code ~cc9b9fcdb625f9b580
   # Success! Execution #1 created.
   # ...

You can stop watching the execution with ``Ctrl+C``, but this won't stop the execution.
The execution should take a second or two to finish if the used Docker image is already on the server.

You can see the status of the execution on `Valohai web application <https://app.valohai.com/>`_
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
   # image                | gcr.io/tensorflow/tensorflow:1.0.1-devel-gpu-py3
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

   # And if your execution would've produced output files, you could access them with:
   $ vh execution outputs 1

.. tip::

   All commands can be written using their shortform if there are no conflicts which sub-command you mean
   e.g. ``vh execution logs 1`` can also be written ``vh exec logs 1`` or even ``vh e lo 1``.

5. Next steps
~~~~~~~~~~~~~

Ad-hoc executions are good when developing your scripts and learning the platform but you should have your
main machine learning code version in a version control repository to allow better collaboration.

Check out :doc:`our quick start TensorFlow tutorial </tutorials/quick-start-tensorflow>` to learn more about
adding a version control repository to your project.

Wizard created a ``valohai.yaml`` for us during the tutorial; you might want to know
:doc:`more how these configuration files work </valohai-yaml>`.
