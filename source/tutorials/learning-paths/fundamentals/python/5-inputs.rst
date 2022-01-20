.. meta::
    :description: Valohai Fundamentals learning path - Downloading data with Valohai inputs

Download input data
#######################

.. include:: ../_shared/_intro.rst

.. include:: ../_shared/_5-inputs.rst

Let's start by defining an input in our ``valohai.yaml``. Uncomment the sample input and update the name and default address.

.. code-block:: yaml
    :emphasize-lines: 7,8,9
    :linenos:

    ---

    - step:
        name: train-model
        image: tensorflow/tensorflow:2.1.0-py3
        command: python train.py {parameters}
        inputs:
          - name: mnist
            default: s3://onboard-sample/tf-sample/mnist.npz
        parameters:
          - name: epoch
            type: integer
            default: 5

Update ``train.py`` to add inputs:

* Get the path to the Valohai inputs folder from the environment variable ``VH_INPUTS_DIR``
* Update the ``mnist_file_path`` to point to a single file in the Valohai inputs.
* Remove the line ``mnist = tf.keras.datasets.mnist``

You should also remove the ``mnist.npz`` from your local machine.

.. code-block:: python
    :emphasize-lines: 6,15
    :linenos:

    import tensorflow as tf
    import numpy
    import argparse

    VH_OUTPUTS_DIR = os.getenv('VH_OUTPUTS_DIR', '.outputs/')
    VH_INPUTS_DIR = os.getenv('VH_INPUTS_DIR', '.inputs/')

    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--epoch', type=int, default=10)
        return parser.parse_args()

    args = parse_args()

    mnist_file_path = os.path.join(VH_INPUTS_DIR, 'mnist/mnist.npz')

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

.. include:: ../_shared/_5-inputs-end.rst

Next: `Collect and view metrics </tutorials/learning-paths/fundamentals/python/6-metadata/>`_ 
