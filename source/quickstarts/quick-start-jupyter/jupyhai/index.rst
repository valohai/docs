.. meta::
    :description: Valohai Jupyter notebook extension

Quick Start - Jupyter Notebooks (MNIST)
=======================================

In this tutorial, we will use the Valohai Jupyter Notebook Extension to build a machine learning model
using the MNIST dataset.

You can also 

.. contents::
   :backlinks: none
   :local:

Requirements
~~~~~~~~~~~~~~~

To use jupyter notebook extension, you will need:

* Docker (https://docs.docker.com/install)

Installation
~~~~~~~~~~~~~~~

Pull the ``valohai/mnist_notebook`` docker image from the Docker Hub.

.. code-block:: bash

  docker pull valohai/mnist_notebook

.. note::

    If you want to use an image without examples in it, use ``valohai/jupyhai`` instead.

Start the notebook server
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

Open a notebook
~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/createnotebook.gif
   :alt: Creating new notebook

Create new notebook in the `/work` folder or choose `tf-mnist-valohai.ipynb`.

Sign in
~~~~~~~~~~

.. thumbnail:: ../shared/login.gif
   :alt: Login to Valohai

Press the Valohai button in the toolbar and login using your Valohai credentials.

.. include:: ../shared/_notebookCore.rst


FAQ
~~~

**When I try to download my outputs back from a finished execution, I get** ``404: Not Found``

Always use the notebook server through ``http://127.0.0.1:8888`` instead of ``http://localhost:8888``.
