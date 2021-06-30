.. meta::
    :description: Valohai Fundamentals learning path -  Uploading data from your Valohai execution
    

Upload output data
####################

.. include:: ../_shared/_3-outputs.rst

Let's update the ``save_path`` to a Valohai output path in our sample scipt file.

.. code-block:: python
    :emphasize-lines: 37
    :linenos:

    import tensorflow as tf
    import numpy
    import valohai

    mnist = tf.keras.datasets.mnist

    mnist_file_path = 'mnist.npz'

    with numpy.load(mnist_file_path, allow_pickle=True) as f:
        x_train, y_train = f['x_train'], f['y_train']
        x_test, y_test = f['x_test'], f['y_test']

    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
    ])

    predictions = model(x_train[:1]).numpy()
    predictions

    tf.nn.softmax(predictions).numpy()

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    loss_fn(y_train[:1], predictions).numpy()

    model.compile(optimizer='adam',
                loss=loss_fn,
                metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)

    save_path = valohai.outputs().path('model.h5')
    model.save(save_path)

..

.. include:: ../_shared/_3-outputs-end.rst