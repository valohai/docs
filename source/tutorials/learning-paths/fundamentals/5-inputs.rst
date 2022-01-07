.. meta::
    :description: Valohai Fundamentals learning path - Downloading data with Valohai inputs

Download input data
###################

.. include:: _shared/_5-inputs.rst

Update **train.py** to add inputs:

* Create a dictionary to pass ``valohai.prepare`` your inputs and their default values
* Update the ``mnist_file_path`` to point to the Valohai inputs.

You should also remove the ``mnist.npz`` from your local machine.

.. code-block:: python
    :emphasize-lines: 9,10,11,17
    :linenos:

    import numpy as np
    import tensorflow as tf
    import valohai


    valohai.prepare(
        step='train-model',
        image='tensorflow/tensorflow:2.6.0',
        default_inputs={
            'dataset': 'https://valohaidemo.blob.core.windows.net/mnist/mnist.npz'
        },
        default_parameters={
            'learning_rate': 0.001,
            'epochs': 5,
        },
    )

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

Update your :ref:`yaml` with ``vh yaml step``. This will generate a ``inputs`` section in your step.

.. code:: bash

    vh yaml step train.py

.. include:: _shared/_5-inputs-end.rst
