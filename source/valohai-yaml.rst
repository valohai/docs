The ``valohai.yaml`` Configuration File
---------------------------------------

The ``valohai.yaml`` configuration file contains all the instructions
required for the platform to execute your experiments.

The root level of a configuration file contains a list of steps.

Steps
~~~~~

Every ``step`` defines a separate execution. It has five valid properties:

Name
^^^^

The ``name`` of the step simply identifies the step in a human-readable format.

Image
^^^^^

``image`` identifies the Docker image that will be used as the base of
the experiment execution. Your code will be inserted run inside this
image, so it should contain most or all the dependencies your experiment has.

Command(s)
^^^^^^^^^^

``command`` defines a single command or a list of commands that are run.

Inputs
^^^^^^

``inputs`` defines a list of inputs.
Inputs are data that is available during step execution.
Inputs are optional for the step.

An input has three valid properties:

* ``name``: defines a human-readable name for the input.
* ``default``: defines a source where the input will be fetched from.
* ``optional``: if defined marks that this input is optional and a URL is
  not necessary to be defined before execution of the step.

Currently valid sources for inputs are HTTP and HTTPS URLs. For these basic access authentication is supported.

During the step execution, the inputs are available under ``/valohai/inputs/<input name>/<input file>``.

Parameters
^^^^^^^^^^

``parameters`` defines a list of parameters. Parameters can be accessed
from the code and used to modify the execution at runtime.

Parameters are optional for the step.

A parameter has these valid properties:

* ``name`` defines a human-readable name for the parameter.
* ``pass-as`` defines how the parameter is passed to the command(s).
  Optional; if not defined, the parameter is passed as  ``--<name> <value>``.
* ``description``: describes what the parameter value is used for.
* ``type``: defines what type the parameter is. Valid values are *float*, *integer* and *string*.
* ``default``: defines a default value for the parameter.
* ``optional``: if defined, marks that this input is optional
  and a value is not necessary to be defined before execution of the step.

An example configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A configuration file could look like this:

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
            pass-as: --max_steps={v}
            description: Number of steps to run the trainer
            type: integer
            default: 300
          - name: learning_rate
            pass-as: --learning_rate={v}
            description: Initial learning rate
            type: float
            default: 0.001
          - name: dropout
            pass-as: --dropout={v}
            description: Keep probability for training dropout
            type: float
            default: 0.9

This configuration file contains one step called *Train model*. The step
is run in the ``gcr.io/tensorflow/tensorflow:0.12.1-devel-gpu`` Docker
image.

The *Train model* step contains one command, which runs the Python file
``train.py`` passing it the parameters defined below.

The step contains four inputs, which are the images and labels for both
the training and the test set. None of these inputs are optional.

The step contains three parameters: *max\_steps*, *learning\_rate* and
*dropout*. None of these parameters are optional.
