.. meta::
    :description: Valohai Fundamentals learning path -  Uploading data from your Valohai execution
    

Upload output data
####################

.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`learning-paths-fundamentals` series.
..

During execution the outputs are stored in ``/valohai/outputs`` directory. After the execution is finished, they will be automatically uploaded to the user configured data store. This will happen regardless the execution was terminated as intended or stopped or crashed.

In this section you will learn:

- What is a datum identifier
- Where do you find datums
- How to set aliases for datums

.. admonition:: A short introduction to outputs
    :class: tip

    * At the end of each execution, outputs are stored in the default data store that is defined in your project settings
    * Valohai will handle authenticating with your cloud data store and uploading the data. You just have to save the file locally to ``/valohai/outputs/``
    * Uploading data never overwrites existing files. It is possible to upload multiple files with the same name. 
    * Each uploaded file will get a unique identifier called datum.
    * For easily accessing specific output files, it is possible to set aliases to datums. 

..

Let's update the ``save_path`` to a Valohai output path in our sample scipt file.

.. code-block:: python
    :emphasize-lines: 45
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

Datums
--------

Datums are unique identifiers that can be used to point to specific output files. You can use them as inputs in your executions in order to reuse the output data. You can view and copy datums from the web UI. 

- **Open your project** on `app.valohai.com <https://app.valohai.com>`_
- **Go to the Data tab under your project**
- Click the three dots at the end of the row for the execution you
- Click **Copy datum:// URL**

.. note:: 

    You'll also have the option to copy your cloud data store's URL (e.g. ``s3://``, ``gs://``, or ``azure://``. You can use either the datum URL or the cloud provider URL for your Valohai executions.


    The advantage of using ``datum://`` is that it allows Valohai keep track of that exact file and version. This allows you to later on trace back files and understand where different files are used, or for example know which pipeline was ran to generate a trained model file.

Setting datum aliases
--------------------------------

In some cases you might want to set an alias that for example always points to the latest execution and its datum. 

- **Open your project** on `app.valohai.com <https://app.valohai.com>`_
- **Go to the Project Data view** (Data tab under your project)
- **Choose Aliases tab**
- Click **Create new datum alias**
- Write **Name** for the alias and choose **datum** from the list.
- Click **Save**
- You can edit saved aliases by choosing **Edit** from the **Actions dropdown menu**. The change history of aliases is tracked.

.. seealso::

  * :ref:`outputs`
  * :ref:`live-outputs`
  * :ref:`cloud-storage`
  * :ref:`howto-datum-alias`
  * `step.inputs reference </reference-guides/valohai-yaml/step-inputs/>`_

..