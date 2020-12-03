.. meta::
    :description: Valohai Hosted Jupyter Notebooks

Quick Start - Hosted Jupyter Notebooks (MNIST)
=====================================================

In this tutorial, we will use the Valohai Hosted Notebooks to build a machine learning model
using the MNIST dataset.

Create a new Notebook instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Navigate to the Notebooks tab of your project and click on ``Create notebook`` to create a new instance.
* Give the instance a title and choose your commit version. Currently all Valohai Hosted Notebooks are created in Microsoft Azure in West Europe.
* Once the instance is up and running you'll be able to connect to it directly from the browser.

.. container:: alert alert-warning

    **Notebook instances are not permanent**

    Keep in mind that Valohai Hosted Notebooks current shut down after 12 hours of being idle. The changes you've made in your Hosted Notebook instance will not be saved and won't be accessible after the instance has shut down.

    However, Valohai allows you to open a Notebook from a previous execution. On the *Details*-tab of an execution you can click on the *Notebook*-button to start a new Notebook instance with the version that was used to run the selected execution.

    If this doesn't meet your needs, consider using the `Jupyhai extension </quickstarts/quick-start-jupyter/jupyhai>`_.

..

Open a notebook
~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/createnotebook.gif
   :alt: Creating new notebook

Create new notebook in the folder or choose `tf-mnist-valohai.ipynb`.

Configure settings
~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/settings.gif
   :alt: Valohai execution settings

Press the Valohai button in the toolbar and go to settings window.


Select the following:

- **Project**: Valohai project where the executions will be version controlled
- **Environment**: Environment type for the cloud executions (E.g. AWS p2.xlarge)
- **Docker Image**: Docker image that provides the required libraries (E.g. TensorFlow)
   - Use `valohai/pypermill` as the base when building your custom Docker image to be used as a part of Valohai Notebook executions.

These are the same settings you would choose when using Valohai website, CLI or `valohai.yaml`.

Once you are happy with your selections. Press save.

Create an execution & watch the results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/execution_hosted.gif
   :alt: Running Valohai execution

Press the Valohai button in the toolbar and select *Create execution*.

.. include:: ../shared/_notebookCore.rst