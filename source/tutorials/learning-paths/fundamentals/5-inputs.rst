.. meta::
    :description: Valohai Fundamentals learning path - Downloading data with Valohai inputs

Download input data
###################

.. include:: _shared/_intro.rst

.. raw:: html

    <div style="position: relative; padding-bottom: 52.7086383601757%; height: 0;"><iframe src="https://www.loom.com/embed/7fe4a2d1709841b9bc5e7d9a8a348f13" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


.. include:: _shared/_5-inputs.rst


Let's start by defining the inputs for our ``train-model`` step.

Update **valohai.yaml** to define new inputs:

.. code-block:: yaml

    - step:
        name: train-model
        command:
          - pip install -r requirements.txt
          - python train.py {parameters}
        image: tensorflow/tensorflow:2.6.0
        parameters:
          - name: epoch
            type: integer
            default: 5
          - name: learning_rate
            type: float
            default: 0.001
        inputs:
          - name: dataset
            default: https://valohaidemo.blob.core.windows.net/mnist/mnist.npz

Update **train.py** to point the ``mnist_file_path`` to the Valohai inputs.

You should also remove the ``mnist.npz`` from your local machine.

.. code-block:: python
    :emphasize-lines: 5
    :linenos:

    import numpy as np
    import tensorflow as tf
    import valohai

    input_path = valohai.inputs('dataset').path()
    with np.load(input_path, allow_pickle=True) as f:
        x_train, y_train = f['x_train'], f['y_train']
        x_test, y_test = f['x_test'], f['y_test']

    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
    ])

    optimizer = tf.keras.optimizers.Adam(learning_rate=valohai.parameters('learning_rate').value)
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(optimizer=optimizer,
                loss=loss_fn,
                metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=valohai.parameters('epoch').value)

    model.evaluate(x_test,  y_test, verbose=2)

    output_path = valohai.outputs().path('model.h5')
    model.save(output_path)

..

Run in Valohai
--------------


.. include:: _shared/_5-inputs-end.rst
