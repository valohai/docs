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

.. admonition:: Default values
    :class: tip

    When a value is undefined, the parameter will appear with its default value, except for the type ``flag``.
    
    Flags will only ever appear, if they are defined with value set to true.
