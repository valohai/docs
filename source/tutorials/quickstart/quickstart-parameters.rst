.. meta::
    :description: Add parameters to your Valohai executions

.. _quickstart-parameters:

Use parameters
###############

.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`quickstart` series.
..

Defining Valohai parameters will allow you to easily rerun your executions and experiment with a different set of parameters.

.. admonition:: A short recap on parameters
    :class: tip
    
    * A Valohai parameter can be a type of a string, int, float or a flag (=bool).
    * The parameter values you define in your code are default values. These can be changed when creating an execution from the UI, command-line or API.
    * Parameters get passed to each Valohai execution as command-line arguments (e.g. ``train.py --epoch=5``)
  
..

Update **train.py** to parameterize ``epoch``.

* Create a dictionary to store your parameters, and their default values
* Pass the dictionary to ``valohai.prepare``
* Read the parameter value during an execution with ``valohai.parameters('myparam').value``


.. code-block:: python
    :emphasize-lines: 3,4,5,6,7,8,9,41
    :linenos:

    import tensorflow as tf
    import numpy
    import valohai

    my_parameters = {
        'epoch': 5
    }

    valohai.prepare(step="train-model", image='tensorflow/tensorflow:2.4.1', default_parameters=my_parameters)

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

    model.fit(x_train, y_train, epochs=valohai.parameters('epoch').value)

    save_path = valohai.outputs().path('model.h5')
    model.save(save_path)

..

Run in Valohai
------------------------

Update your :ref:`yaml` with ``vh yaml step``. This will generate a ``parameters`` section in your step.

Finally run a new Valohai execution.

.. code:: bash

    vh yaml step train.py
    vh exec run train-model --adhoc

..

Rerun an execution with different parameter values
-------------------------------------------------------

* **Open your project** on `app.valohai.com <https://app.valohai.com>`_ 
* **Open the latest execution**
* Click **Copy** 
* Scroll down to the **Parameters** section
* Change the value of **epoch**
* Click **Create execution** 


.. video:: /_static/videos/execution_parameters.mp4
    :autoplay:
    :width: 600

.. tip:: 

    You can also run a new execution with different parameter values from the command line:

    ``vh exec run train-model --adhoc --epoch=10``

.. seealso::

    * Core concept: :ref:`parameters`
    * Core conept: `Hyperparameter search </topic-guides/core-concepts/parameters/#hyperparameter-search>`_
    * Tutorial: :ref:`task-grid-search`
..