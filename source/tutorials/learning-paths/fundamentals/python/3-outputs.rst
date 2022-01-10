.. meta::
    :description: Valohai Fundamentals learning path -  Uploading data from your Valohai execution
    

Upload output data
####################

.. include:: ../_shared/_intro.rst

.. include:: ../_shared/_3-outputs.rst

Let's get the path to the Valohai outputs folder from the environment variable ``VH_OUTPUTS_DIR``` and update the ``save_path`` to save our model in that folder.

.. note:: 

    If there is no environment varialbe (= you're running locally) the path will be ``.outputs/``

.. code-block:: python
    :emphasize-lines: 4, 38
    :linenos:

    import tensorflow as tf
    import numpy

    VH_OUTPUTS_DIR = os.getenv('VH_OUTPUTS_DIR', '.outputs/')

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

    save_path = os.path.join(VH_OUTPUTS_DIR, 'model.h5')
    model.save(save_path)

..

.. include:: ../_shared/_3-outputs-end.rst

Next: `Use parameters </tutorials/leaning-paths/fundamentals/python/4-parameters/>`_ 
