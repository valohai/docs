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
