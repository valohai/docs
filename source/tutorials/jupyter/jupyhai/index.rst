.. meta::
    :description: Valohai Jupyter notebook extension

.. _jupyter:

Jupyter Notebooks
##################

In this tutorial, we will use Jupyhai, to run a Valohai execution from your local Jupyter notebook.

.. admonition:: A short recap on Notebooks
   :class: tip

   * Jupyhai is a Jupyter notebook extension developed and maintained by Valohai.
   * Use the **Run remote** button, instead of the Run cell button to run your notebook on Valohai.
   * The Jupyhai addon will generate a :ref:`yaml` file for each execution based on the contents of the Notebook. You don't need to create the YAML file yourself.
   * Notebook executions use a custom Docker image called ``valohai/pypermill``. Make sure to use it as a base for your custom Docker images.

.. admonition:: Installing Jupyhai to on your machine
   :class: attention

   .. code:: bash

      pip install --upgrade pip
      pip install notebook
      pip install valohai-cli jupyhai
      jupyhai install

   ..


Start notebook
----------------

Create a new folder ``valohai-notebook`` on your desktop and launch Jupyter in that directory.

.. code-block:: bash

   mkdir valohai-notebook
   cd valohai-notebook

   .. code-block:: bash

   vh login
   # ... login with your username and password

   vh project create
   # give the project a name

   jupyter notebook

..

.. note:: 

   Depending on your organization settings, you might be asked to choose the owner for the project. We suggest choosing the organization as the owner of the project.

.. note:: 

   If your organization is on a self-hosted version of Valohai, you'll need to specify the login address with ``vh login --host https://myvalohai.com``


* Create a new Python 3 notebook
* Open the new Notebook
* Click on **Settings** on the toolbar
* Login with your Valohai credentials
* Update the Docker image to ``valohai/notebook:tensorflow-2.5.0``
* Close the **Settings** tab
* Add ``print('Hello Valohai Notebooks!')`` to the first cell
* Click on ``Run remote`` to run the notebook remotely
* View the logs from the execution by clicking on the gizmo on the right side of the page (e.g. ``#1``)

.. tip::

   All Valohai notebook executions have to be based on a custom Valohai Docker image ``valohai/pypermill``. You can build your own images for Notebook executions, as long as they're based on ``valohai/pypermill``

   Check out our prebuilt set of `Docker images for the most popular Notebook executions on Valohai </howto/docker/popular-notebook-images/>`_



.. video:: /_static/videos/jupyter-login-launch.mp4
   :autoplay:
   :width: 600



.. admonition:: Open a Notebook from a previous execution
   :class: tip

   Each of the colored gizmos on the right side of the page signify a single Valohai execution. You can click on any of the completed executions and select ``Notebook`` to inspect the Notebook version that was used to run the execution.

..

Valohai 101 tutorial
----------------------

Follow our Fundamentals tutorial with valohai-utils to learn how to interact with Valohai inputs, outputs, metadata, and parameters. 

`Valohai Fundamentals with valohai-utils </tutorials/learning-paths/fundamentals/valohai-utils/>`_ 


.. hint::

   Are you looking for the old Notebook tutorial that uses ``tags`` to define inputs and parameters? Find it `here </tutorials/jupyter/jupyhai/jupyhai-with-tags/>`_.
