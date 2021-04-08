.. meta::
    :description: Collecting metrics and comparing executions

.. _quickstart-metadata:


Collect and view metrics
########################################

.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`quickstart` series.
..

Valohai allows you to easily collect key performance metrics from executions, visualize them and compare metrics across multiple executions.

.. admonition:: A short recap on metadata
    :class: tip

    * Valohai metadata is collected as key:value pairs
    * Easily visualized as a time series graph or a scatter plot in the web app
    * Used to compare performance of multiple executions
    * Sort and find executions based on metadata metrics

..

Update **train.py** to add metadata logging:

* Create a new method ``logMetadata`` that will use log metadata
* Create a TensorFlow LambdaCallback to trigger ``logMetadta`` every time an epoch ends
* Pass the new callback to ``model.fit``

.. code-block:: python
    :emphasize-lines: 3,5,6,7,8,9,49,50
    :linenos:

    import tensorflow as tf
    import numpy
    import valohai

    def logMetadata(epoch, logs):
        with valohai.metadata.logger() as logger:
                logger.log("epoch", epoch)
                logger.log("accuracy", logs['accuracy'])
                logger.log("loss", logs['loss'])

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

    metadataCallback = tf.keras.callbacks.LambdaCallback(on_epoch_end=logMetadata)
    model.fit(x_train, y_train, epochs=valohai.parameters('epoch').value, callbacks=[metadataCallback])

    save_path = valohai.outputs().path('model.h5')
    model.save(save_path)

..

Run in Valohai
------------------------

Adding or changing metadata doesn't require any changes to the :ref:`yaml`.

You can immediately launch a new execution and view the collected metadata.

.. code:: bash

    vh exec run train-model --adhoc

..

View metrics
-------------------

* Go to your project's executions
* Click on the **Show columns** button on the right side, above the table
* **Select accuracy and loss** to show them in the table.
* **Open the latest execution**
* **Go to the metadata tab** to view metrics from that executions.
* Select **epoch on X-axis** and **accuracy and loss on Y-axis**

.. admonition:: Latest metada value
    :class: Important

    The metadata value displayed in the table is always the latest printed metadata. In your script you should ensure that the last value you print out for ``accuracy`` is the best value for your use case.

.. video:: /_static/videos/execution_metadata.mp4
    :autoplay:
    :width: 600

.. seealso::

    * :ref:`executions-compare`
    * :ref:`executions-graphs`

..
