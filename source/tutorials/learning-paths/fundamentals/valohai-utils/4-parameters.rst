.. meta::
    :description: Valohai Fundamentals learning path - Adding parameters to your executions

Use parameters
##############

.. include:: ../_shared/_4-parameters.rst

Update **train.py** to parameterize ``epochs``.

* Create a dictionary to pass ``valohai.prepare`` your parameters and their default values
* Read the parameter value during an execution with ``valohai.parameters('myparam').value``


.. code-block:: python
    :emphasize-lines: 9,10,11,33
    :linenos:

    import numpy as np
    import tensorflow as tf
    import valohai
    

    valohai.prepare(
        step='train-model',
        image='tensorflow/tensorflow:2.6.0',
        default_parameters={
            'epochs': 5,
        },
    )

    input_path = 'mnist.npz'
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

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(optimizer='adam',
                loss=loss_fn,
                metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=valohai.parameters('epoch').value)

    model.evaluate(x_test,  y_test, verbose=2)

    output_path = valohai.outputs().path('model.h5')
    model.save(output_path)

..

Add another parameter
---------------------

Update **train.py** to parameterize ``learning_rate``.

* Create a dictionary to pass ``valohai.prepare`` the default values of your parameters
* Read the parameter value during an execution with ``valohai.parameters('myparam').value``

.. code-block:: python
    :emphasize-lines: 9,10,11,29,31
    :linenos:

    import numpy as np
    import tensorflow as tf
    import valohai
    

    valohai.prepare(
        step='train-model',
        image='tensorflow/tensorflow:2.6.0',
        default_parameters={
            'learning_rate': 0.001,
            'epochs': 5,
        },
    )

    input_path = 'mnist.npz'
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

Update your :ref:`yaml` with ``vh yaml step``. This will generate a ``parameters`` section in your step.

.. code-block:: bash

    vh yaml step train.py

.. include:: ../_shared/_4-parameters-end.rst