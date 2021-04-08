.. meta::
    :description: Downloading data to your Valohai execution

.. _quickstart-inputs:


Download input data
####################

.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`quickstart` series.
..

Define inputs to easily download data from a public address or your private cloud storage.

.. admonition:: A short recap on inputs
    :class: tip

    * Valohai inputs can be from a public location (HTTP/HTTPS) or from your private cloud storage (AWS S3, Azure Storage, GCP Cloud Storage, OpenStack Swift)
    * The input values you define in your code are default values. You can replace any defined inputs file(s) when creating an execution from the UI, command-line or API.
    * All inputs are downloaded and available during an execution to ``/valohai/inputs/<input-name>/``
    * An input value can be a single file (e.g. ``myimages.tar.gz``) or you can use a wildcard to download multiple files from a private cloud storage (e.g. ``s3://mybucket/images/*.jpeg``)
    * Valohai inputs are cached on the virtual machine.


..

Update **train.py** to add inputs:

* Create a dictionary ``my_inputs`` to define your inputs and their default values
* Pass the dictionary to ``valohai.prepare``
* Update the ``mnist_file_path`` to point to the Valohai inputs.

You should also remove the ``mnist.npz`` from your local machine.

.. code-block:: python
    :emphasize-lines: 2,9,10,11,13,15
    :linenos:

    import tensorflow as tf
    import valohai
    import numpy

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

Finally run a new Valohai execution.

.. code:: bash

    vh yaml step train.py
    vh exec run train-model --adhoc

..

Rerun an execution with different input data
-------------------------------------------------------

* **Open your project** on `app.valohai.com <https://app.valohai.com>`_
* **Open the latest execution**
* Click **Copy**
* Scroll down to the **Inputs** section and remove the current input.
* You can now either pass in a new URI or select an input from the Data list (for example, if you've uploaded a file)
* Click **Create execution**


.. video:: /_static/videos/execution_inputs.mp4
    :autoplay:
    :width: 600

.. tip::

    You can also run a new execution with different input value from the command line:

    ``vh exec run train-model --adhoc --mnist=https://mmyurl.com/differentfile.npz``


.. seealso::

    * :ref:`howto-data-upload-files`
    * `step.inputs reference </reference-guides/valohai-yaml/step-inputs/>`_

..
