``valohai.yaml``
================

The ``valohai.yaml`` configuration file defines how the platform runs your experiments.

The ``valohai.yaml`` must be placed at the root of your project version control repository.

.. contents::
   :backlinks: none
   :local:

``step`` defines the type of execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every ``step`` defines a separate type of execution such as feature extraction or training.

Here is an overview of the five valid ``step`` properties:

* ``name``: a human-readable name of the step such as "Feature extraction" or "Run training"
* ``image``: the Docker image that will be used as the base of the execution
* ``command``: one or more commands that are ran during execution
* ``inputs``: (optional) files available during execution
* ``parameters``: (optional) valid parameters that can be passed to the ``command``

.. _yaml-image:

``image`` and dependency installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your code will be run inside the defined Docker ``image``.

The Docker image should preferably contain all dependencies you need, to ensure your runs can get to work
as quickly as possible.

.. tip::

   You can run dependency installation commands as part of your ``command`` but it will result in slower
   computation time as then each execution starts by dependency setup, which is sub-optimal but nevertheless allowed.

You can find premade Docker images for the most popular machine learning libraries on
`Docker Hub <https://hub.docker.com/>`_.

For instance:

* https://hub.docker.com/r/tensorflow
* https://hub.docker.com/r/valohai
* https://hub.docker.com/r/kaixhin

You can also create and host your own images on `Docker Hub <https://hub.docker.com/>`_ or any other public Docker
repository.

Here are the most common Docker images currently used on the platform:

* gcr.io/tensorflow/tensorflow:1.5.0-devel-gpu-py3
* gcr.io/tensorflow/tensorflow:1.5.0-devel-gpu *(the Python 2 version)*
* gcr.io/tensorflow/tensorflow:1.4.1-devel-gpu-py3
* gcr.io/tensorflow/tensorflow:1.4.1-devel-gpu *(the Python 2 version)*
* gcr.io/tensorflow/tensorflow:1.3.0-devel-gpu-py3
* gcr.io/tensorflow/tensorflow:1.3.0-devel-gpu *(the Python 2 version)*
* gcr.io/tensorflow/tensorflow:1.0.1-devel-gpu-py3
* gcr.io/tensorflow/tensorflow:1.0.1-devel-gpu *(the Python 2 version)*
* gcr.io/tensorflow/tensorflow:0.12.1-devel-gpu-py3
* gcr.io/tensorflow/tensorflow:0.12.1-devel-gpu *(the Python 2 version)*
* valohai/keras:2.1.3-tensorflow1.4.0-python3.5-cuda8.0-cudnn6-devel-ubuntu14.04
* valohai/keras:2.0.0-tensorflow1.0.1-python3.6-cuda8.0-cudnn5-devel-ubuntu16.04
* valohai/keras:2.0.0-theano0.9.0rc4-python3.6-cuda8.0-cudnn5-devel-ubuntu16.04
* valohai/keras:2.0.0-theano0.8.2-python3.6-cuda8.0-cudnn5-devel-ubuntu16.04
* valohai/darknet:62b781a-cuda8.0-cudnn5-devel-ubuntu16.04
* valohai/darknet:b61bcf5-cuda8.0-cudnn5-devel-ubuntu16.04
* r-base:3.4.2

.. tip:: Using these images will result in faster executions since they're pre-seeded onto our workers.


``command`` defines what is run
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``command`` section defines one or more commands that are run during execution.

For example, the following configuration file defines two steps:

* **Hardware check**: executes ``nvidia-smi`` to check the status of server GPU using ``gcr.io/tensorflow/tensorflow:0.12.1-devel-gpu`` Docker image
* **Environment check**: executes ``printenv`` followed by ``python --version`` to check how the runtime environment looks like inside ``busybox`` Docker image

.. code-block:: yaml

    ---

    - step:
        name: Hardware check
        image: gcr.io/tensorflow/tensorflow:0.12.1-devel-gpu
        command: nvidia-smi

    - step:
        name: Environment check
        image: busybox
        command:
          - printenv
          - python --version

.. tip::

   The ``command`` is considered to be successful if it returns error code 0. This is the default convention
   for most programs and scripting languages.

   The platform will mark execution as crashed if any of the commands returns any other error code.

``inputs`` and downloading files before execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``inputs`` are the data files that are available during step execution.

An input in ``inputs`` has three potential properties:

* ``name``: A human-readable name for the input
* ``default``: (optional) The default source where the input will be fetched from.
  If not defined, the user has to define the source at the start of the execution.
* ``optional``: (optional) Marks that this input is optional and an URL definition is not necessary before execution of the step

Currently valid sources for inputs are HTTP and HTTPS URLs. For these basic access authentication is supported.

During the step execution, inputs are available under ``/valohai/inputs/<input name>/<input file>``.
To see this in action, try running ``ls -la /valohai/inputs/*`` as the main command of execution which has inputs.

.. tip::

   You can download any files you want during the execution with e.g. Python libraries or command-line tools
   but then your executions become slower as it circumvents our input file caching system.

``parameters`` and customizing executions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameters are injected into the command by replacing the ``{parameters}`` placeholder.
Good examples of parameters would be "learning rate" number or "network layout" string.

A parameter in ``parameters`` has six potential properties:

* ``name``: a human-readable name for the parameter
* ``type``: the parameter type, valid values are **float**, **integer** and **string**
* ``pass-as``: (optional) how the parameter is passed to the command e.g. ``-t {v}`` where ``{v}`` becomes the actual value.
  If not defined, the parameter is passed as  ``--{name}={value}``
* ``description``: (optional) more detailed human-readable description of the parameter
* ``default``: (optional) the default value of the parameter
* ``optional``: (optional) marks that this input is optional and the value can be left undefined

Example ``valohai.yaml`` files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TensorFlow MNIST training
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    ---

    - step:
        name: Train model
        image: gcr.io/tensorflow/tensorflow:0.12.1-devel-gpu
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

This configuration file contains one step called **Train model**.

The step is run inside the ``gcr.io/tensorflow/tensorflow:0.12.1-devel-gpu`` Docker image.

The step contains one command, which runs a Python file named ``train.py`` passing it the parameters defined further below.

The step requires four inputs: **training-set-images**, **training-set-labels**, **test-set-images**, **test-set-labels**.
These are the images and labels for both the training and test sets.
None of these inputs are optional but all of them have a default source.

The step contains three parameters: **max\_steps**, **learning\_rate** and **dropout**.
None of these parameters are optional but all of them have a default value.
