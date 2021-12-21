.. meta::
    :description: Valohai Jupyter notebook extension

.. _jupyter:

Jupyter Notebooks
##################

In this tutorial, we will use Jupyhai, to run a Valohai execution from your local Jupyter notebook.

.. admonition:: A short recap on Notebooks
   :class: tip

   * Jupyhai is a Jupyter notebook extension developed and maintained by Valohai. It allows you to easily run your notebooks on a remote (cloud) machine.
   * The plugin adds a **Run remote** button to the user interface. Clicking it will execute the notebook in Valohai.
     
     * Valohai always executes the whole notebook, from the first to the last cell to ensure anyone can easily rerun the notebook as is.

   * The Jupyhai addon will generate a :ref:`yaml` file for each execution based on the contents of the Notebook. You don't need to create the YAML file yourself.
   * Notebook executions use a custom Docker image called ``valohai/pypermill``. Make sure to use it as a base for your custom Docker images.
   * Each executed Notebook is versioned and stored in Valohai.


Setting up
-----------

In this tutorial you'll learn how to:

* Run an existing Notebook on a remote virtual machine through Valohai
* Read data from your private cloud storage
* Save trained models and graphics in Valohai
* Collect customer metrics from your executions
* Create timeseries graphs and confusion matrices

In this tutorial we'll use the churn-analysis example notebook from `Donne Martin's Data Science iPython Notebooks repository <https://github.com/donnemartin/data-science-ipython-notebooks>`_.

You can `download the example notebook from here <https://nbviewer.org/github/donnemartin/data-science-ipython-notebooks/blob/master/analyses/churn.ipynb>`_ and the `example dataset (churn.csv) <https://github.com/donnemartin/data-science-ipython-notebooks/blob/master/data/churn.csv>`_ file. (Right click on the links and click "Save Link as")


Install the tools
^^^^^^^^^^^^^^^^^^^

We'll start by installing JupyterLab and Valohai's addon called ``jupyhai``.

.. code:: bash

   pip install --upgrade pip
   pip install jupyterlab
   pip install --upgrade jupyhai
   jupyhai install

..

Create a new directory on your machine and place in there the two files that you downloaded above. Then open JupyterLab from that directory by running ``jupyter-lab`` on your command line.

Finally, go to the Valohai web app and create a new project.

Run your notebook on Valohai
------------------------------

Let's start by running your existing notebook in Valohai.

You should have your Jupyter environment open with only two files, the notebook and the ``churn.csv`` file.

1. Update the notebook's second cell to read the csv file from the correct path:

   .. code-block:: python
      :linenos:
      :emphasize-lines: 1

      churn_df = pd.read_csv('churn.csv')
      col_names = churn_df.columns.tolist()

      print "Column names:"
      print col_names

      to_show = col_names[:6] + col_names[-6:]

      print "\nSample data:"
      churn_df[to_show].head(6)

2. Click on the **Run Remote** button and start by logging in with your Valohai username/password or API Token (if you have MFA setup).
3. Choose your project from the dropdown menu and optionally choose a different execution environment.
4. Change the default Docker image to ``valohai/notebook:sklearn-1.0``. This is a custom Valohai hosted image that contains sklearn, matplotlib, pandas, and numpy.