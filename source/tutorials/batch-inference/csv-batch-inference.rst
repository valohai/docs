.. meta::
    :description: How to do Batch Inference with a CSV dataset

Batch Inference with CSV Data
=============================

In this tutorial you will learn how to create and run a Batch Inference execution in Valohai. This execution will use TensorFlow 2.5.0 to run new CSV data through a previously trained model.

.. admonition:: Prerequirements
    :class: attention

    For this tutorial you will need:

    * Python 3
    * Valohai command-line client (Run ``pip install --upgrade valohai-cli``)

    We're also going to need two files:

    * a model trained with TensorFlow 2.5.0
    * some new data in a single CSV file

    To make it easy for you they are available here, no need to download them:

    * Model: `<s3://valohai-public-files/tutorials/batch-inference/csv-batch-inference/model.zip>`_
    * Images: `<s3://valohai-public-files/tutorials/batch-inference/csv-batch-inference/data.csv>`_

    If you want to, you can train the required model by following the Keras example here: `<https://keras.io/examples/structured_data/structured_data_classification_from_scratch/>`_.

Running on Valohai
------------------

To easily run our batch inference on Valohai, we will use it to run our code from the very beginning.

If you don't already have a Valohai account, go to `<https://app.valohai.com/>`_ to create one for yourself.

Create a new folder for our project, then run the following commands in the project folder:

.. code-block:: bash

    vh login
    # fill in your username
    # and your password

    vh init
    # Answer the wizard questions like this:
    # "First, let's..." -> y
    # "Looks like..." -> python batch_inference.py, then y to confirm
    # "Choose a number or..." -> tensorflow/tensorflow:2.5.0, then y to confirm
    # "Write this to..." -> y
    # "Do you want to link..." -> C, then give a name for your project, then select your user

Edit the generated ``valohai.yaml`` so that it looks like this:

.. code-block:: yaml

    ---

    - step:
        name: Batch Inference
        image: tensorflow/tensorflow:2.5.0
        command:
        - pip install pandas valohai-utils
        - python batch_inference.py
        inputs:
        - name: model
          default: s3://valohai-public-files/tutorials/batch-inference/csv-batch-inference/model.zip
        - name: images
          default: s3://valohai-public-files/tutorials/batch-inference/csv-batch-inference/data.csv

What we are doing here is defining a single step for our machine learning pipeline, which is the Batch Inference step. We will run on top of the official ``tensorflow/tensorflow:2.5.0`` Docker image, first install the ``valohai-utils`` Python library and then run our batch inference code.

Let's test that everything is set up correctly by running on Valohai:

.. code-block:: bash

    vh exec run --adhoc "Batch Inference"

If everything went as planned, we should see our Valohai execution end after finding out that ``batch_inference.py`` is missing:

.. image:: batch-inference-tutorial-1.png
   :alt: Error, but success!

Unpacking the Model
--------------------

Today we are unpacking the model ourselves. Let's get started by creating and opening up ``batch_inference.py`` in your favorite editor!

Add these imports to the beginning of the file:

.. code-block:: python

    import json
    from zipfile import ZipFile

    import pandas as pd
    import tensorflow as tf
    import valohai as vh

For unpacking the model, we will only need `zipfile` and `valohai`, but we will use the rest of the imports soon enough.

Next, unpack the model to a folder called model in the current working directory:

.. code-block:: python

    with ZipFile(vh.inputs('model').path(process_archives=False), 'r') as f:
        f.extractall('model')

Done!

Loading and Using Our Model
---------------------------

Begin by loading our model:

.. code-block:: python

    model = tf.keras.models.load_model('model')

Easy, huh? Let's load up the data:

.. code-block:: python

    csv = pd.read_csv('data.csv')
    labels = csv.pop('target')
    data = tf.data.Dataset.from_tensor_slices((dict(csv), labels))
    batch_data = data.batch(batch_size=32)

Aaand we are almost done. Run the model with the loaded up data. While we're at it, let's log and save the results as a JSON file:

.. code-block:: python

    results = model.predict(batch_data)

    values = [str(nums[0]) for nums in results]
    metadata = {k:v for (k, v) in zip(range(1, len(values) + 1), values)}

    for _, value in metadata.items():
        with vh.logger() as logger:
            logger.log("result", value)

    with open(vh.outputs().path('results.json'), 'w') as f:
        json.dump(metadata, f)

Let's run the batch inference on Valohai:

.. code-block:: bash

    vh exec run --adhoc "Batch Inference"

If everything went according to plan, you can now preview the results in the Outputs-tab:

.. image:: csv-batch-inference-tutorial-2.png
   :alt: Results of our batch inference execution

.. seealso ::

    * `Valohai CLI </tutorials/valohai-cli/>`_
    * `Using Docker Images </topic-guides/docker-images/>`_
    * `Attach tags and metadata to your files </howto/data/tag-files/>`_
    * `Valohai APIs </tutorials/apis/>`_
