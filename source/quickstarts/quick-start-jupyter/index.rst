.. meta::
    :description: Valohai Jupyter notebook extension

Quick Start - Jupyter Notebooks (MNIST)
=======================================

In this tutorial, we will use the Valohai Jupyter Notebook Extension to build a machine learning model
using the MNIST dataset.

.. contents::
   :backlinks: none
   :local:

1. Requirements
~~~~~~~~~~~~~~~

To use jupyter notebook extension, you will need:

* Docker (https://docs.docker.com/install)

2. Installation
~~~~~~~~~~~~~~~

Pull the ``valohai/mnist_notebook`` docker image from the Docker Hub.

.. code-block:: bash

  docker pull valohai/mnist_notebook

.. note::

    If you want to use an image without examples in it, use ``valohai/jupyhai`` instead.

3. Start the notebook server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the notebook server on local port 8888.

.. code-block:: none

  docker run -p 8888:8888 valohai/mnist_notebook

Open in browser: http://127.0.0.1:8888

.. container:: alert alert-warning

   **Run your own code and notebooks**

   * Run ``docker pull valohai/jupyhai`` instead.
   * Navigate to the folder where your files are
   * Run ``docker run -p 8888:8888 -v "$PWD":/home/jovyan/work valohai/jupyhai``.
      * This mounts your current working directory into the container.
      * All the files in your current working directory will be available within the container
      * All changes within the mounted folder will persist after shutting down
   * You can run install additional libraries to the environment by adding a new cell at the top of your notebook and running ``!pip install mylibrary``

4. Open a notebook
~~~~~~~~~~~~~~~~~~

.. thumbnail:: createnotebook.gif
   :alt: Creating new notebook

Create new notebook in the `/work` folder or choose `tf-mnist-valohai.ipynb`.

5. Sign in
~~~~~~~~~~

.. thumbnail:: login.gif
   :alt: Login to Valohai

Press the Valohai button in the toolbar and login using your Valohai credentials.

6. Configure settings
~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: settings.gif
   :alt: Valohai execution settings

Press the Valohai button in the toolbar and go to settings window.

Select the following:

- **Project**: Valohai project where the executions will be version controlled
- **Environment**: Environment type for the cloud executions (E.g. AWS p2.xlarge)
- **Docker Image**: Docker image that provides the required libraries (E.g. TensorFlow)

These are the same settings you would choose when using Valohai website, CLI or `valohai.yaml`.

Once you are happy with your selections. Press save.

7. Create an execution
~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: execution.gif
   :alt: Running Valohai execution

Press the Valohai button in the toolbar and select *Create execution*.

The gizmo for the new execution will appear to the right.

.. container:: alert alert-warning

   **Open a Notebook from a previous execution**

   Each of the colored gizmos on the right side of the page signify a single Valohai execution. You can click on any of the completed executions and select ``Notebook`` to launch the Notebook version that was used to run the execution.

..

8. Watch the results
~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: download.gif
   :alt: Get results back from Valohai

You can click the `#1 > Notebook` button to download the finished notebook back to your local machine.

9. Parameterize the notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: parameterize.gif
   :alt: Adding hyperparameter

Parameterizing a notebook happens through cell tags. Tags are a standard Jupyter feature.

Here we mark the first cell with a ``parameters`` tag, which means all variables are considered to be
Valohai parameters, just like you would define in the `valohai.yaml`.

10. Download the inputs
~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: inputs.png
   :alt: Adding parameterized input

Here we marked the first cell with ``inputs`` tag and ran it in Valohai.

All the variables in this cell will be considered as Valohai input URIs for the execution, just like in the `valohai.yaml`.

11. Reusing the parameterized notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: parameter2.gif
   :alt: Adding hyperparameter

Now you can run notebook based experiments without a notebook!

Because the ``learning_rate`` is parameterized, you can change it via Valohai web interface and run
additional experiments without even opening the notebook.


FAQ
~~~

**When I try to download my outputs back from a finished execution, I get** ``404: Not Found``

Always use the notebook server through ``http://127.0.0.1:8888`` instead of ``http://localhost:8888``.
