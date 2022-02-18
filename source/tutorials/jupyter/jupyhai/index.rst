.. meta::
    :description: Valohai Jupyter notebook extension

.. _jupyter:

Jupyter Notebooks
##################

.. raw:: html  

   <div style="position: relative; padding-bottom: 51.873198847262245%; height: 0;"><iframe src="https://www.loom.com/embed/7c7177d4699a45af8e4b0655091a02b0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

In this tutorial, you will learn how to use the Jupyhai extension to run a Valohai execution from your local Jupyter notebook.

.. admonition:: A short recap on Notebooks
   :class: tip

   * Jupyhai is a Jupyter notebook extension developed and maintained by Valohai.
   * Use the **Run remote** button, instead of the Run cell button to run your notebook on Valohai.
   * The Jupyhai addon will generate a :ref:`yaml` file for each execution based on the contents of the Notebook. You don't need to create the YAML file yourself.
   * Make sure you're always using the latest version of ``jupyhai``

   .. code:: bash

      pip install jupyhai --upgrade

   ..

.. admonition:: Installing Jupyhai to on your machine
   :class: attention

   Instead of installing the following packages globally, you should consider using a virtual environment. 

   .. code:: bash

      pip install --upgrade pip
      pip install notebook
      pip install valohai-cli jupyhai
      jupyhai install

   ..


Start a notebook
-----------------

After installing ``jupyhai``, create a new folder ``valohai-notebook`` on your desktop and launch Jupyter in that directory.

The directory from where you launch Jupyter will be considered as the root of your project. 
Make sure it contains only the files necessary for your notebook run.

.. code-block:: bash

   mkdir valohai-notebook
   cd valohai-notebook

   # Login to your Valohai account with your username and password
   vh login
   
   # Create a new Valohai project
   vh project create
   
   jupyter notebook

..

.. note:: 

   If your organization is on a self-hosted version of Valohai, you'll need to specify the login address with ``vh login --host https://myvalohai.com``

.. note:: 

   Depending on your organization settings, you might be asked to choose the owner for the project. We suggest choosing the organization as the owner of the project.


* Create a new Python 3 notebook
* Open the new notebook
* Click on **Settings** on the toolbar
* Login with your Valohai credentials, if you did not already do so from the CLI
* Update the Docker image to ``valohai/notebook:tensorflow-2.5.0``
* Close the **Settings** tab
* Add ``print('Hello Valohai Notebooks!')`` to the first cell
* Click on ``Run remote`` to run the notebook remotely
* View the logs from the execution by clicking on the gizmo on the right side of the page (e.g. ``#1``)

.. tip::

   Check out our prebuilt set of `Docker images for the most popular Notebook executions on Valohai </howto/docker/popular-notebook-images/>`_.
   You can of course also build your own images for Notebook executions. A good starting point is for example a ``python:3.9`` image.

   

.. video:: /_static/videos/jupyter-login-launch.mp4
   :autoplay:
   :width: 600



.. admonition:: Open a Notebook from a previous execution
   :class: tip

   Each of the colored gizmos on the right side of the page signify a single Valohai execution. You can click on any of the completed executions and select ``Notebook`` to inspect the Notebook version that was used to run the execution.

..

Valohai 101 tutorial
----------------------

Follow our `Valohai Fundamentals learning path </tutorials/learning-paths/fundamentals/>`_ to learn how to interact with Valohai inputs, outputs, metadata, and parameters. 


.. note:: 

   We recommend strongly to use the ``valohai-utils`` Python helper library with jupyter notebooks. 
   This will be useful when working with inputs, outputs, and parameters. 

   ``valohai-utils`` will be installed automatically with the latest versions of ``jupyhai``.
   You can of course either add it in your Docker image or add ``!pip install valohai-utils`` in the first cell of your notebook. 


Note that you will need to add the ``valohai.prepare()`` command at the beginning of your notebook to be able to handle Valohai inputs and parameters.
You can check below how the complete sample script with inputs, outputs, parameters, and metadata logging from the Fundamentals learning path would look like in Jupyter notebook.
Please make sure to go through the tutorial to better understand how to use the ``valohai-utils`` helper tool. 

Finally, even though you will need to defined the ``step`` name in the ``valohai.prepare()`` command, the actual step name in the automatically generated ``valohai.yaml`` will be ``jupyter_execution``.

.. code-block:: python
    :emphasize-lines: 5,6,7,8,9,10,11,12,13,14
    :linenos:

    import numpy as np
    import tensorflow as tf
    import valohai

    valohai.prepare(
         step='mystep',
         default_inputs={
            'dataset': 'https://valohaidemo.blob.core.windows.net/mnist/mnist.npz'
         },
         default_parameters={
            'learning_rate': 0.001,
            'epoch': 10,
        },
    )

    def log_metadata(epoch, logs):
        with valohai.logger() as logger:
            logger.log('epoch', epoch)
            logger.log('accuracy', logs['accuracy'])
            logger.log('loss', logs['loss'])

    input_path = valohai.inputs('dataset').path()
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

    callback = tf.keras.callbacks.LambdaCallback(on_epoch_end=log_metadata)
    model.fit(x_train, y_train, epochs=valohai.parameters('epoch').value, callbacks=[callback])

    model.evaluate(x_test,  y_test, verbose=2)

    output_path = valohai.outputs().path('model.h5')
    model.save(output_path)


Notebook previews and visualizations
-------------------------------------

The notebooks you run in Valohai will be automatically versioned and saved as outputs. 
You can preview them under the Data tab of your project or under the Outputs tab for individual executions.

When it comes to visualization such as plots, it might make more sense to save them as separate outputs. This allows you to access them quickly without having to scroll through the notebook.

- To do this you can follow the instructions in the section on `saving graphs from executions </howto/executions/complex-visualizations/>`_. This way the graphs will be also versioned. 

- If you mark the images read-only when saving them, you can view them under the outputs tab even before the execution has finished.  ``valohai-utils`` can also they care of the direct uploading for you: ``valohai.outputs().live_upload("myimage.png")``


  