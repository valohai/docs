
.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`learning-paths-fundamentals` series.
..

In this section you will learn how to

- Import Valohai in your Python scripts
- Save Valohai outputs
- Run executions in Valohai


A sample training script
------------------------

* Download `this mnist.npz <https://onboard-sample.s3-eu-west-1.amazonaws.com/tf-sample/mnist.npz>`_ file to your working directory
* Create a **new file** ``valohai-quickstart/train.py`` and paste the following example script:


.. code-block:: python
    :linenos:

    import tensorflow as tf
    import numpy

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

    save_path = 'model.h5'
    model.save(save_path)

..
