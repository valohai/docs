
.. meta::
    :description: Valohai Fundamentals learning path - Running your first Valohai execution


Getting started
#####################

.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`learning-paths-fundamentals` series.
..

In this section you will learn how to

- Install Valohai tools
- Create a project in Valohai
- Import Valohai in your Python scripts
- Save Valohai outputs
- Run executions in Valohai


.. admonition:: Prerequirements
    :class: attention

    Before starting make sure you have created and account at `app.valohai.com <https://app.valohai.com>`_ and that you have been added to a Valohai organization. Your organization admin can invite you to join the organization.


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

* Create a new the step called ``train-model``
* Define a default Docker image for this step. The Docker image should contain the packages we need to run our code, like Tensorflow.

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,5

    import tensorflow as tf
    import numpy
    import valohai

    valohai.prepare(step='train-model', image='tensorflow/tensorflow:2.4.1')

..

Run in Valohai
------------------------

Finally, we run the following commands in the the command line, on your own computer:

.. code:: bash

    vh yaml step train.py
    vh exec run train-model --adhoc

..

* ``vh yaml step`` uses the command-line tools to generate a :ref:`yaml` and a ``requirements.txt`` that contains ``valohai-utils`` (which is need to run the Python script).
* ``vh exec run <step-name>`` creates a new Valohai execution with the step that we defined.
* ``--adhoc`` tells Valohai that the code for this execution is coming from our local machine instead of our code repository. Valohai will package the local directory and upload it for an execution.

.. hint:: 

    ``valohai-utils`` is a Python helper library that makes it easier to configure and run Valohai executions.

    **What does valohai-utils do?**
    
    * Generates and updates the :ref:`yaml` based on the source code
    * Agnostic input handling (single file, multiple files, zip, tar)
    * Parse command-line parameters
    * Compress outputs
    * Download inputs for local experiments
    * Straightforward way to print metrics as Valohai metadata
    * Code parity between local vs. cloud

    Read more at https://github.com/valohai/valohai-utils


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
