.. meta::
    :description: The valohai.yaml configuration file defines how the platform runs your experiments. It must be placed at the root of your project version control repository. Read how to create a YAML file for managing steps in a machine learning pipeline.

Valohai YAML
============

The ``valohai.yaml`` configuration file defines steps of your machine learning pipeline.

The configuration file is optional but we recommend adding it so everything stays reproducible between
different Valohai projects using the same git repository.
The configuration file must be placed at the root of your project repository.

Here is a very simple ``valohai.yaml`` to print "hello" on a worker machine with Python 3.6.

.. code-block:: yaml

    - step:
        name: greet-me
        image: python:3.6
        command: echo hello

.. contents::
   :backlinks: none
   :local:

``step``
~~~~~~~~

Every ``step`` defines a separate type of execution such as feature extraction, training or evaluation.

Here is an overview of the five valid ``step`` properties:

* ``name``: the name of the step such as "feature-extraction" or "model-training"
* ``image``: the Docker image that will be used as the base of the execution
* ``command``: one or more commands that are ran during execution
* ``inputs``: (optional) files available during execution
* ``parameters``: (optional) valid parameters that can be passed to the ``command``

.. _yaml-image:

``image``
~~~~~~~~~

Your code will be run inside a Docker container based on the defined Docker ``image``.

The Docker image should preferably contain all dependencies you need, to ensure your runs can get to work
as quickly as possible.

.. tip::

   You can run dependency installation commands as part of your ``command`` but it will result in slower
   computation time as then each execution starts by dependency setup, which is sub-optimal but nevertheless allowed.

You can find Docker images for the most popular machine learning libraries on
`Docker Hub <https://hub.docker.com/>`_.

You can also create and host your images on `Docker Hub <https://hub.docker.com/>`_ or any other Docker repository.

.. include:: _image-list.rst

``command``
~~~~~~~~~~~

The ``command`` section defines one or more commands that are run during execution.

For example, the following configuration file defines two steps:

* **hardware-check**: executes ``nvidia-smi`` to check the status of server GPU using ``tensorflow/tensorflow:0.12.1-devel-gpu`` Docker image
* **environment-check**: executes ``printenv`` followed by ``python --version`` to check how the runtime environment looks like inside ``busybox`` Docker image

.. code-block:: yaml

    - step:
        name: hardware-check
        image: tensorflow/tensorflow:0.12.1-devel-gpu
        command: nvidia-smi

    - step:
        name: environment-check
        image: python:3.6
        command:
          - printenv
          - python --version

.. tip::

   The platform will mark execution as crashed if *the last* command returns an error code other than 0.

``inputs``
~~~~~~~~~~

``inputs`` are the data files that are available during step execution.

An input in ``inputs`` has three potential properties:

* ``name``: The input name; this is shown on the user interface and names the directory where the input files
  will be placed during execution like ``/valohai/inputs/my-input-name``.
* ``default``: (optional) The default source where the input will be fetched from.
  If not defined, the user has to define the source at the start of the execution.
* ``optional``: (optional) Marks that this input is optional and an URL definition is not
  necessary before execution of the step.

Currently valid sources for inputs are HTTP, HTTPS and various cloud provider specific data
stores such as AWS S3 (``s3://...``) and Azure Storage (``azure://...``).

For these HTTP/S endpoints basic access authentication is supported, but for the cloud provider stores,
the access credentials must be configured under project settings.

During the step execution, inputs are available under ``/valohai/inputs/<input name>/<input file>``.
To see this in action, try running ``ls -la /valohai/inputs/`` as the main command of execution which has inputs.

.. tip::

   You can download any files you want during the execution with e.g. Python libraries or command-line tools
   but then your executions become slower as it circumvents our input file caching system.

``parameters``
~~~~~~~~~~~~~~

Parameters are injected into the command by replacing the ``{parameters}`` placeholder.
Good examples of parameters would be "learning rate" number or "network layout" string.

A parameter in ``parameters`` has six potential properties:

* ``name``: the parameter name, shown on the user interface and used as the default name when passed to commands
* ``type``: the parameter type, valid values are **float**, **integer**, **string** and **flag**
* ``pass-as``: (optional) how the parameter is passed to the command e.g. ``-t {v}`` where ``{v}`` becomes the actual value.
  If not defined, the parameter is passed as  ``--{name}={value}``. Note: Type 'flag' defaults to '--{name}'.
* ``description``: (optional) more detailed human-readable description of the parameter
* ``default``: (optional) the default value of the parameter
* ``optional``: (optional) marks that this input is optional and the value can be left undefined. Note: has no effect for the type 'flag'.

Note: When a value is undefined, the parameter will appear with it's default value, except for the type 'flag'. Flags will only
ever appear, if they are defined with value set to true.

Example YAML Files
~~~~~~~~~~~~~~~~~~

TensorFlow MNIST Training
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    - step:
        name: train-model
        image: tensorflow/tensorflow:0.12.1-devel-gpu
        command: python train.py {parameters}
        inputs:
          - name: training-set-images
            default: https://valohai-mnist.s3.amazonaws.com/train-images-idx3-ubyte.gz
          - name: training-set-labels
            default: https://valohai-mnist.s3.amazonaws.com/train-labels-idx1-ubyte.gz
          - name: test-set-images
            default: https://valohai-mnist.s3.amazonaws.com/t10k-images-idx3-ubyte.gz
          - name: test-set-labels
            default: https://valohai-mnist.s3.amazonaws.com/t10k-labels-idx1-ubyte.gz
        parameters:
          - name: max_steps
            type: integer
            pass-as: --max_steps={v}
            description: Number of steps to run the trainer
            default: 300
          - name: learning_rate
            type: float
            pass-as: --learning_rate={v}
            description: Initial learning rate
            default: 0.001
          - name: dropout
            type: float
            pass-as: --dropout={v}
            description: Keep probability for training dropout
            default: 0.9

This configuration file contains one step called **train-model**.

The step is run inside the ``tensorflow/tensorflow:0.12.1-devel-gpu`` Docker image.

The step contains one command, which runs a Python file named ``train.py`` passing it the parameters defined further below.

The step requires four inputs: **training-set-images**, **training-set-labels**, **test-set-images**, **test-set-labels**.
These are the images and labels for both the training and test sets.
None of these inputs are optional but all of them have a default source.

The step contains three parameters: **max\_steps**, **learning\_rate** and **dropout**.
None of these parameters are optional but all of them have a default value.
