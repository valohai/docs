.. meta::
    :description: Valohai Fundamentals learning path - Generate and update YAML configuration with valohai-utils

Define your steps in Python
###########################

.. raw:: html

    <div style="position: relative; padding-bottom: 52.7086383601757%; height: 0;"><iframe src="https://www.loom.com/embed/65d18d5a4b5f42f49bff61f54d497ffa" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


So far been manually writing the ``valohai.yaml`` file to define our steps. Alternatively you can use the :ref:`valohai-utils` to create and update your ``valohai.yaml`` configuration file.

Update **train.py** to call ``valohai.prepare`` and specify your step's details.

.. code-block:: python
    :emphasize-lines: 5,6,7,8,9,10,11,12,13,14,15
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
            'epoch': 10,
        },
    )

    def log_metadata(epoch, logs):
        with valohai.logger() as logger:
            logger.log('epoch', epoch)
            logger.log('accuracy', logs['accuracy'])
            logger.log('loss', logs['loss'])

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

    callback = tf.keras.callbacks.LambdaCallback(on_epoch_end=log_metadata)
    model.fit(x_train, y_train, epochs=valohai.parameters('epoch').value, callbacks=[callback])

    model.evaluate(x_test,  y_test, verbose=2)

    output_path = valohai.outputs().path('model.h5')
    model.save(output_path)


Update valohai.yaml
--------------------

You'll need to update the ``valohai.yaml`` file before running your job.

On your own computer run ``vh yaml step <filename>`` to update the file.

.. code-block:: bash

    vh yaml step train.py

Now you can run a new execution:

.. code-block:: bash

    vh exec run train-model --adhoc