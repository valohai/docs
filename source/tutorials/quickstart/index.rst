.. meta::
    :description: Taking your existing projects to Valohai

.. _quickstart:


Valohai 101 (Python)
============================

Throughout this tutorial, we’ll walk you through creating a new project and running an sample Python script in Valohai.

The tutorial will start with simply getting a Python script to run on Valohai, and then continue with adding parameters, fetching input data and collecting key metrics.

.. admonition:: Prerequirements
    :class: attention

    .. code:: bash

        # Create a new directory for our sample project
        mkdir valohai-quickstart
        cd valohai-quickstart

        # Install Valohai tools
        pip install --upgrade valohai-cli valohai-utils

        # Login with your Valohai username and password
        vh login

        # Create a new project and link the current directory to project
        vh project create

    ..

    * Download `this mnist.npz <https://onboard-sample.s3-eu-west-1.amazonaws.com/tf-sample/mnist.npz>`_ file to the new directory

..

.. toctree::
    :titlesonly:
    :hidden:

    quickstart-parameters
    quickstart-inputs
    quickstart-metadata
    quickstart-deployments
    quickstart-pipeline

..


.. _quickstart-execution:


A sample training script
------------------------


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

Import Valohai
------------------------

Now we'll ``import valohai`` and define a new :ref:`step` in the ``train.py`` file we just created..

* Create a new the step called `train-model`
* Define a default Docker image for this step. The Docker image should contain the packages we need to run our code, like Tensorflow.

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,5

    import tensorflow as tf
    import numpy
    import valohai

    valohai.prepare(step='train-model', image='tensorflow/tensorflow:2.4.1')

..

Save trained model
------------------------

Next, we'll update the ``save_path`` to a Valohai output path in our sample scipt file.

.. code-block:: python
    :linenos:
    :lineno-start: 37
    :emphasize-lines: 3

    model.fit(x_train, y_train, epochs=5)

    save_path = valohai.outputs().path('model.h5')
    model.save(save_path)

..

Run in Valohai
------------------------

Finally, we run the following commands in the the command line:

.. code:: bash

    vh yaml step train.py
    vh exec run train-model --adhoc

..

* ``vh yaml step`` uses the command-line tools to generate a :ref:`yaml` and a ``requirements.txt`` that contains ``valohai-utils`` (which is need to run the Python script).
* ``vh exec run <step-name>`` creates a new Valohai execution with the step that we defined.
* ``--adhoc`` tells Valohai that the code for this execution is coming from our local machine instead of our code repository. Valohai will package the local directory and upload it for an execution.


View in Valohai
-------------------

* **Open your project** on `app.valohai.com <https://app.valohai.com>`_
* **Open the latest execution**
* The details type contains information about the executions
* The logs tab contains all logs from the execution


.. seealso::

    * :doc:`Docker images</topic-guides/docker-images/>`
    * :ref:`yaml`
    * `vh project </reference-guides/valohai-cli/project/>`_
    * `vh execution run </reference-guides/valohai-cli/execution/#vh-execution-run>`_
    * `vh execution watch </reference-guides/valohai-cli/execution/#vh-execution-watch>`_

..
