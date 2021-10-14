.. meta::
    :description: Valohai Jupyter notebook extension

:orphan:

Jupyter Notebooks
##################

In this tutorial, we will use Jupyhai, to run a Valohai execution from your local Jupyter notebook.

.. admonition:: A short recap on Notebooks
   :class: tip

   * Jupyhai is a Jupyter notebook extension developed and maintained by Valohai.
   * Use the **Run remote** button, instead of the Run cell button to run your notebook on Valohai.
   * The Jupyhai addon will generate a :ref:`yaml` file for each execution based on the contents of the Notebook. You don't need to create the YAML file yourself.

.. admonition:: Installing Jupyhai to on your machine
   :class: attention

   .. code:: bash

      pip install --upgrade pip
      pip install notebook
      pip install jupyhai
      jupyhai install

   ..



Start notebook
----------------

Create a new folder ``valohai-notebook`` on your desktop and launch Jupyter in that directory.

.. code-block:: none

   mkdir valohai-notebook
   cd valohai-notebook
   jupyter notebook

..

* Create a new Python 3 notebook
* Open the new Notebook
* Click on **Settings** on the toolbar
* Login with your Valohai credentials
* Update the Docker image to ``valohai/notebook:tensorflow-2.5.0``
* Close the settings tab
* Add ``print('Hello Valohai Notebooks!')`` to the first cell
* Click on ``Run remote`` to run the notebook remotely
* View the logs from the execution by clicking on the gizmo on the right side of the page (e.g. ``#1``)

.. admonition:: Jupyhai Settings
   :class: tip

   Click on **Settings**  on the toolbar to:

   * Connect your Notebook to a Valohai project
   * Choose the environment you want to run on
   * Define the Docker image you'd like to use

.. video:: /_static/videos/jupyter-login-launch.mp4
   :autoplay:
   :width: 600



.. admonition:: Open a Notebook from a previous execution
   :class: tip

   Each of the colored gizmos on the right side of the page signify a single Valohai execution. You can click on any of the completed executions and select ``Notebook`` to inspect the Notebook version that was used to run the execution.

..

MNIST sample
-------------

.. admonition:: Prerequirements
   :class: attention

   `Download the sample MNIST dataset <https://onboard-sample.s3-eu-west-1.amazonaws.com/tf-sample/mnist.npz>`_ and place it in the same folder as the notebook.

Replace your ``print('Hello Valohai Notebooks!')`` with the sample code from below.

This is a simple MNIST sample that loads up the data from a local file, trains a model and saves the trained model on the local machine.

.. code-block:: python
   :linenos:

   import tensorflow as tf
   import numpy

   myinput = 'mnist.npz'

   with numpy.load(myinput, allow_pickle=True) as f:
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

   model.save('model.h5')

..

Add parameters
------------------------

Parameterizing a notebook happens through cell tags. Tags are a standard Jupyter feature.

* Create a new cell and define a new variable ``epoch_val`` in it.
* Show cell tags by going to **View->Cell Toolbar->Tags**.
* Add a new tag ``parameters`` to the first cell.

.. code-block:: python

   epoch_val = 6

..

Then update ``model.fit`` to set the epochs value from the variable.

.. code-block:: python
   :linenos:
   :lineno-start: 28
   :emphasize-lines: 5


   model.compile(optimizer='adam',
               loss=loss_fn,
               metrics=['accuracy'])

   model.fit(x_train, y_train, epochs=epoch_val)

   model.save('model.h5')

..

.. video:: /_static/videos/jupyter-parameters.mp4
    :autoplay:
    :width: 600


Add inputs
----------------------

You can easily download data to your notebook either from a public location (HTTP/HTTPS) or a private cloud storage.

* Create a new cell at the top of your notebook
* Add an ``inputs`` tag to the new cell
* In the new cell define a variable ``mydata`` and paste the address of your dataset

.. code-block:: python

   mydata = 's3://onboard-sample/tf-sample/mnist.npz'

..

.. tip::

   Valohai will download the input data to ``/valohai/inputs/<name>/<file>``.

..

Update the ``myinput`` in your sample code to point to ``/valohai/inputs/mydata/mnist.npz``

.. code-block:: python
   :linenos:
   :emphasize-lines: 4

   import tensorflow as tf
   import numpy

   myinput = '/valohai/inputs/mydata/mnist.npz'

   with numpy.load(myinput, allow_pickle=True) as f:
      x_train, y_train = f['x_train'], f['y_train']
      x_test, y_test = f['x_test'], f['y_test']
..


.. video:: /_static/videos/jupyter-inputs.mp4
    :autoplay:
    :width: 600

Save a trained model
----------------------

Finally you need to save the trained model as a Valohai output.

.. code-block:: python
   :linenos:
   :lineno-start: 34

   model.save('/valohai/outputs/model.h5')

..


View in Valohai
-------------------

* **Open your project** on `app.valohai.com <https://app.valohai.com>`_
* **Open the latest execution**
* The details type contains information about the executions
* The logs tab contains all logs from the execution
* You can click on the blue **Notebooks** button, to view an executed Notebook

.. seealso::

   * Using :ref:`howto-tasks` for hyperparameter tuning

