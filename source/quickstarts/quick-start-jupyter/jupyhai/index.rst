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

Installation
~~~~~~~~~~~~~~~

Install Valohai's Jupyhai package to run notebooks from your local machine on Valohai.

.. code-block:: bash

  pip install jupyhai


Start the notebook server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to the folder where your notebooks are located and start notebooks.

.. code-block:: none

  jupyter notebook

..

.. container:: alert alert-warning

   **Run your own code and notebooks**

   * This mounts your current working directory into the container.
   * All the files in your current working directory will be available within the container
   * All changes within the mounted folder will persist after shutting down
   * You can run install additional libraries to the environment by adding a new cell at the top of your notebook and running ``!pip install mylibrary``

..

Open a notebook
~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/createnotebook.gif
   :alt: Creating new notebook

Create new notebook folder or choose an existing one.

Sign in
~~~~~~~~~~

.. thumbnail:: ../shared/login.gif
   :alt: Login to Valohai

Press the Valohai button in the toolbar and login using your Valohai credentials.

.. container:: alert alert-warning

   You'll be automatically logged in, if you've already logged in `valohai-cli`.

..


Select the following:

- **Project**: Valohai project where the executions will be version controlled
- **Environment**: Environment type for the cloud executions (E.g. AWS p2.xlarge)
- **Docker Image**: Docker image that provides the required libraries (E.g. TensorFlow)
   - Use `valohai/pypermill` as the base when building your custom Docker image to be used as a part of Valohai Notebook executions.

These are the same settings you would choose when using Valohai website, CLI or `valohai.yaml`.

Once you are happy with your selections. Press save.

Create an execution & watch the results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/execution.gif
   :alt: Running Valohai execution

Press the *Run remote* button on the toolbar

.. include:: ../shared/_notebookCore.rst


FAQ
~~~

**When I try to download my outputs back from a finished execution, I get** ``404: Not Found``

Always use the notebook server through ``http://127.0.0.1:8888`` instead of ``http://localhost:8888``.
