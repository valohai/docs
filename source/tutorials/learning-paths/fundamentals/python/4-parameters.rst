.. meta::
    :description: Valohai Fundamentals learning path - Adding parameters to your executions

Use parameters
###############

.. include:: ../_shared/_4-parameters.rst

Update **train.py** to parameterize ``epoch``.

* Define a parameter in your ``valohai.yaml``
* Import argparse
* Create a method to parse the command line arguments
* Use the parsed argument


Start by commenting out the example parameter in your ``valohai.yaml`` and updating the command to include parameters. The ``{parameters}`` will be replaced with all the parameters and their values during runtime.


.. code-block:: yaml
    :emphasize-lines: 6,10,11,12,13
    :linenos:

    ---

    - step:
        name: train-model
        image: tensorflow/tensorflow:2.1.0-py3
        command: python train.py {parameters}
        #inputs:
        #  - name: example-input
        #    default: https://example.com/
        parameters:
          - name: epoch
            type: integer
            default: 5

.. important::

    The linter (``vh lint``) will flag any errors you might have in your YAML file. The most common errors are around identation, so make sure you pay special attention to indentation when writing YAML.

Next update your ``train.py`` to parse the command line arguments and use the argument in ``model.fit``. 

.. code-block:: python
    :emphasize-lines: 3,7,8,9,10,11,12,44
    :linenos:

    import tensorflow as tf
    import numpy
    import argparse

    VH_OUTPUTS_DIR = os.getenv('VH_OUTPUTS_DIR', '.outputs/')

    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--epoch', type=int, default=10)
        return parser.parse_args()

    args = parse_args()

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

    model.fit(x_train, y_train, epochs=args.epoch)

    save_path = os.path.join(VH_OUTPUTS_DIR, 'model.h5')
    model.save(save_path)

..

Run in Valohai
------------------------

Update your :ref:`yaml` with ``vh yaml step``. This will generate a ``parameters`` section in your step.

.. include:: ../_shared/_4-parameters-end.rst