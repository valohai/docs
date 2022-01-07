.. meta::
    :description: Valohai Fundamentals learning path -  Uploading data from your Valohai execution
    

Upload output data
##################

.. include:: _shared/_3-outputs.rst

.. raw:: html

    <div style="position: relative; padding-bottom: 53.01914580265096%; height: 0;"><iframe src="https://www.loom.com/embed/c9b94a923ce045729d1d33bd28f42fe3" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Let's update the ``output_path`` to a Valohai output path in our sample script file.
We'll use valohai-utils to define the output directory, so make sure you've imported valohai to your project.

.. code-block:: python
    :emphasize-lines: 3, 34
    :linenos:

    import numpy as np
    import tensorflow as tf
    import valohai


    valohai.prepare(
        step='train-model',
        image='tensorflow/tensorflow:2.6.0',
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
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(optimizer='adam',
                loss=loss_fn,
                metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)

    model.evaluate(x_test,  y_test, verbose=2)

    output_path = valohai.outputs().path('model.h5')
    model.save(output_path)

..

Now create a new file ``requirements.txt`` and add there valohai-utils.

Finally, update your ``valohai.yaml`` to first install the requirements and then run your Python script.

.. code-block:: yaml

    - step:
      name: train-model
      command:
        - pip install -r requirements.txt
        - python train.py
      image: tensorflow/tensorflow:2.6.0


.. include:: _shared/_3-outputs-end.rst