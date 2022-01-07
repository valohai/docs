.. meta::
    :description: Valohai Fundamentals learning path - Collect and visualize key metrics

Collect and view metrics
########################

.. include:: _shared/_6-metadata.rst

.. raw:: html

    <div style="position: relative; padding-bottom: 52.785923753665685%; height: 0;"><iframe src="https://www.loom.com/embed/3d85b6d6128c40ef9d8b03fe73e48705" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Update **train.py** to add metadata logging:

* Create a new function ``log_metadata`` that will log metadata
* Create a TensorFlow LambdaCallback to trigger the ``log_metadata`` function every time an epoch ends
* Pass the new callback to the ``model.fit`` method

.. code-block:: python
    :emphasize-lines: 5,6,7,8,9,32,33
    :linenos:

    import numpy as np
    import tensorflow as tf
    import valohai

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

..

Collect test metrics
--------------------

* Save the model test accuracy and test loss into variables
* Log the test metrics with the Valohai logger

.. code-block:: python
    :emphasize-lines: 34,35,36,37
    :linenos:

    import numpy as np
    import tensorflow as tf
    import valohai

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

    test_loss, test_accuracy = model.evaluate(x_test,  y_test, verbose=2)
    with valohai.logger() as logger:
        logger.log('test_accuracy', test_accuracy)
        logger.log('test_loss', test_loss)

    output_path = valohai.outputs().path('model.h5')
    model.save(output_path)

..

.. include:: _shared/_6-metadata-end.rst
