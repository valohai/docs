.. meta::
    :description: Valohai Fundamentals learning path - Adding parameters to your executions

Use parameters
##############

.. include:: _shared/_4-parameters.rst

.. raw:: html

    <div style="position: relative; padding-bottom: 52.863436123348016%; height: 0;"><iframe src="https://www.loom.com/embed/1c353621ce6948e3aff93956313b3c94" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Let's start by defining parameters for our ``train-model`` step.

Update the **valohai.yaml** file with two new parameter definitions:

.. code-block:: yaml

    - step:
        name: train-model
        command:
          - pip install -r requirements.txt
          - python train.py {parameters}
        image: tensorflow/tensorflow:2.6.0
        parameters:
          - name: epoch
            type: integer
            default: 5
          - name: learning_rate
            type: float
            default: 0.001


Update **train.py** to use the parameter ``epoch`` in ``model.fit`` and use the ``learning_rate`` parameter value in the optimizer.

* Read the parameter value during an execution with ``valohai.parameters('myparam').value``

.. code-block:: python
    :emphasize-lines: 20,22,26
    :linenos:

    import numpy as np
    import tensorflow as tf
    import valohai
    

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

.. include:: _shared/_4-parameters-end.rst