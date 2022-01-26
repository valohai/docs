.. meta::
    :description: Valohai Pipelines learning path - Creating your first pipeline in Valohai

Getting started
#################

.. include:: _intro-pl.rst

.. raw:: html
    
    <div style="position: relative; padding-bottom: 36.45083932853717%; margin-bottom: 20%; height: 0;"><iframe src="https://www.loom.com/embed/2aff28bfe38a43389fc820b328ee2c4c" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 150%;"></iframe></div>  


In this section you will learn:

- What is a pipeline?
- What are pipeline nodes?
- What are pipeline edges?

The sample scripts used in this tutorial can also be found here. 


What is a pipeline?
--------------------

Pipelines automate your machine learning operations on Valohai ecosystem. They are series of executions, Tasks and deployments.

Examples of pipelines could be:

* A pipeline that runs every Monday at 09:00 to fetch data from a database, and if there are over 1000 new records it will retrain the model, evaluate its performance, and update the ``latest-model`` `alias </howto/data/datum-alias>`_ to the newly trained model.
* A pipeline that trains 300 models in parallel and compares if any of those models is better than the existing model.
* A pipeline that trains a new model and deploys a new version of your REST API with the new model.
* A pipeline that extracts data from a database, executes a transformation process on the data, and finally loads the data to a data store.

Valohai pipelines consist of ``nodes`` and ``edges``. 

.. list-table::
   :widths: 10 90
   :stub-columns: 1

   * - ``nodes``
     - A node can be type of a execution, Task or a deployment. It's a "single step" in the pipeline.
   * - ``edges``
     - Edges define how data flows from one node to another. For example: move the file called ``preprocessed_mnist.npz`` from ``preprocess`` node's outputs to ``train`` node as the input called ``dataset``

How to define nodes and edges in ``valohai.yaml`` will be covered in more detail in this tutorial. You can read more about pipelines `here </topic-guides/core-concepts/pipelines>`_. 

Sample scripts
---------------

In this tutorial, we will use sample scripts ``preprocess_dataset.py`` and ``train_model.py`` from our `MNIST TensorFlow example on GitHub <https://github.com/valohai/tensorflow-example>`_. 
Start by creating these files in your current repository.

**preprocess_dataset.py**

.. code-block:: python
    :linenos:

    import numpy as np
    import valohai

    valohai.prepare(
        step='preprocess-dataset',
        image='python:3.9',
        default_inputs={
            'dataset': 'https://valohaidemo.blob.core.windows.net/mnist/mnist.npz',
        },
    )

    print('Loading data')
    with np.load(valohai.inputs('dataset').path(), allow_pickle=True) as file:
        x_train, y_train = file['x_train'], file['y_train']
        x_test, y_test = file['x_test'], file['y_test']

    print('Preprocessing data')
    x_train, x_test = x_train / 255.0, x_test / 255.0

    print('Saving preprocessed data')
    path = valohai.outputs().path('preprocessed_mnist.npz')
    np.savez_compressed(path, x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)
    
..


**train_model.py**

.. code-block:: python
    :linenos:

    import uuid
    import numpy as np
    import tensorflow as tf
    import valohai


    def log_metadata(epoch, logs):
        """Helper function to log training metrics"""
        with valohai.logger() as logger:
            logger.log('epoch', epoch)
            logger.log('accuracy', logs['accuracy'])
            logger.log('loss', logs['loss'])


    valohai.prepare(
        step='train-model',
        image='tensorflow/tensorflow:2.6.0',
        default_inputs={
            'dataset': 'https://valohaidemo.blob.core.windows.net/mnist/preprocessed_mnist.npz',
        },
        default_parameters={
            'learning_rate': 0.001,
            'epochs': 5,
        },
    )

    input_path = valohai.inputs('dataset').path()
    with np.load(input_path, allow_pickle=True) as f:
        x_train, y_train = f['x_train'], f['y_train']
        x_test, y_test = f['x_test'], f['y_test']

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10),
    ])

    optimizer = tf.keras.optimizers.Adam(learning_rate=valohai.parameters('learning_rate').value)
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(optimizer=optimizer,
                    loss=loss_fn,
                    metrics=['accuracy'])

    callback = tf.keras.callbacks.LambdaCallback(on_epoch_end=log_metadata)
    model.fit(x_train, y_train, epochs=valohai.parameters('epochs').value, callbacks=[callback])

    test_loss, test_accuracy = model.evaluate(x_test,  y_test, verbose=2)

    with valohai.logger() as logger:
        logger.log('test_accuracy', test_accuracy)
        logger.log('test_loss', test_loss)


    suffix = uuid.uuid4()
    output_path = valohai.outputs().path(f'model-{suffix}.h5')
    model.save(output_path)
..

Remember to make sure that all the libraries are installed by adding them into the ``requirements.txt`` or by having the respective ``pip install`` commands in the ``valohai.yaml``. 


Add two steps steps, ``preprocess-dataset`` and ``train-model``, to your ``valohai.yaml`` manually or by by using ``valohai-utils``. 

.. code-block:: bash

    vh login
    vh project status

    # Link to and existing project
    vh project link

    # Or create a new project
    vh project create

    # Add the steps to valohai.yaml
    vh yaml step preprocess_dataset.py
    vh yaml step train_model.py

