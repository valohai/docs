Example - TensorFlow MNIST
==========================

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
