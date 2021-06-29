.. meta::
    :description: Valohai Fundamentals learning path - Downloading data with Valohai inputs

Download input data
#######################

.. include:: ../_shared/_5-inputs.rst

Update **train.py** to add inputs:

* Create a dictionary ``my_inputs`` to define your inputs and their default values
* Pass the dictionary to ``valohai.prepare``
* Update the ``mnist_file_path`` to point to the Valohai inputs.

You should also remove the ``mnist.npz`` from your local machine.

.. code-block:: python
    :emphasize-lines: 10,11,12,14,16
    :linenos:

    import tensorflow as tf
    import numpy
    import valohai


    my_parameters = {
        'epoch': 5
    }

    my_inputs = {
        'mnist': 's3://onboard-sample/tf-sample/mnist.npz'
    }

    valohai.prepare(step="train-model", image='tensorflow/tensorflow:2.4.1', default_parameters=my_parameters, default_inputs=my_inputs)

    mnist_file_path = valohai.inputs('mnist').path()

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

    model.fit(x_train, y_train, epochs=valohai.parameters('epoch').value)

    save_path = valohai.outputs().path('model.h5')
    model.save(save_path)

..

Run in Valohai
------------------------

Update your :ref:`yaml` with ``vh yaml step``. This will generate a ``inputs`` section in your step.

.. code:: bash

    vh yaml step train.py

.. include:: ../_shared/_5-inputs-end.rst
