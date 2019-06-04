``step.parameters``
===================

Parameters are injected into the command by replacing any **Valohai parameter placeholders** defined further below.
Good examples of parameters would be "learning rate" number or "network layout" string.

A parameter in ``parameters`` has 2 required and 4 optional properties:

* ``name``: the parameter name, shown on the user interface
* ``type``: the parameter type, valid values are ``float``, ``integer``, ``string`` and ``flag``
* ``pass-as``: **(optional)** how the parameter is passed to the command
* ``description``: **(optional)** more detailed human-readable description of the parameter
* ``default``: **(optional)** the default value of the parameter
* ``optional``: **(optional)** marks that this input is optional and the value can be left undefined

.. note::

    ``optional`` has no effect for the ``flag`` type.

If ``pass-as`` is not defined, the parameter is passed as ``--<PARAMETER_NAME>={v}``, you can customize this by specifying ``{v}`` in the ``pass-as`` e.g. ``-t {v}`` where ``{v}`` becomes the actual value.

.. note::

    ``flag`` type defaults to just ``--<PARAMETER_NAME>`` when set to true.

``{parameters}`` placeholder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``{parameters}`` injects all parameters to its position in the commands.

For example:

.. code-block:: yaml

    - step:
        name: train-model
        image: python:3.6
        command:
          - python train.py {parameters}
        parameters:
          - name: max-steps
            type: integer
            description: Number of steps to run the trainer
            default: 300
          - name: learning-rate
            type: float
            pass-as: --lr={v}
            description: Initial learning rate
            default: 0.001
          - name: architecture
            type: string
            pass-as: arc {v}
            default: 10xRELU-SoftMax
            optional: true

The above would generate the following command by default:

.. code-block:: bash

    python train.py --max-steps=300 --lr=0.001 arc 10xRELU-SoftMax

.. note::

    When a value is undefined, the parameter will appear with its default value, except for the type ``flag``.
    Flags will only ever appear, if they are defined with value set to true.

``{parameter:<NAME>}`` placeholder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also use singular parameters using the ``{parameter:<NAME>}`` syntax.

For example:

.. code-block:: yaml

    - step:
        name: preprocess-and-train
        image: python:3.6
        command:
          - python preprocess.py {parameter:train-split}
          - python train.py {parameter:learning-rate}
        parameters:
          - name: train-split
            type: integer
            default: 80
          - name: learning-rate
            pass-as: --lr={v}
            type: float
            default: 0.001

The above would generate the following commands by default:

.. code-block:: bash

    python preprocess.py --train-split=80
    python train.py --lr=0.001

``{parameter-value:<NAME>}`` placeholder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wish to ignore ``pass-as`` definition, you can use ``{parameter-value:<NAME>}`` to pass only the parameter value.
This is essentially the same as defining ``pass-as: "{v}"``.

For example:

.. code-block:: yaml

    - step:
        name: preprocess
        image: python:3.6
        command:
          - python preprocess.py {parameter-value:train-split} {parameter-value:style}
        parameters:
          - name: train-split
            type: integer
            default: 80
          - name: style
            pass-as: -s={v}
            type: string
            default: nested

The above would generate the following command by default:

.. code-block:: bash

    python preprocess.py 80 nested

.. tip::

    There are no limits how many ``{parameters}``, ``{parameter:<NAME>}`` and ``{parameter-value:<NAME>}`` definitions
    you can have in a set of commands so use them to your heart's content!