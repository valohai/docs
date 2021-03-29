.. meta::
    :description: Running a grid-search executions

.. _task-grid-search:

Running a Grid search
##########################

It can be daunting to try different hyperparameters one-by-one. Valohai offers a mechanism to do hyperparameter searches using parallel executions and a grid search.

When starting a task, instead of a single value for a single hyperparameter, you get to define multiple values at once. There are various modes to choose from e.g. Single, Multiple, Linear, Logspace and Random.

.. admonition:: Prerequirements
    :class: attention

    * A Valohai project that is connected to a Git-repository.
    * At least one :ref:`step` with parameters defined. Follow our :ref:`quickstart-parameters` tutorial to create a step with parameters.

..

Create a Task
---------------

* **Open your project** on `app.valohai.com <https://app.valohai.com>`_ 
* **Open the Task tab**
* Click **Create task** 
* Select the **Step** that contains parameters and you want to use for the Grid-search
* Scroll down to **Parameters**
* **Set the values** for each parameter
    * Choose the type: Single, Multiple, Linear, Logspace or Random
    * Input the values (for multiple input one value per line)
* Click on **Create task**

Valohai will launch a set of execution to run a Grid search. Each execution will have a unique combination of the parameters, within the ranges you provided. 

Valohai manages the queueing of those executions, creating new virtual machines to run the executions and finally scaling the machines back down, when they're not needed anymore.

A Task is a collection of related executions. You'll find all the individual executions on the ``Executions`` tab of your project.

.. video:: /_static/videos/task_create.mp4
    :autoplay:
    :width: 600

.. admonition:: Early stopping
    :class: tip

    You can set the `Early stopping` criteria if you want to stop running the search based on your metadata values.

..

Compare executions
---------------------

You can view metadata metrics and compare the a Task's executions just like with any other execution.

* Click on your Project's **Task** tab
* **Open a Task**
* On the Executions view of a Task, click on the **Show columns** button on the right side, above the table
* **Select ``max_steps`` and ``learning_rate``** to show them in the table.
* **Go to the metadata tab** to view metrics from all executions in that Task.
* Select **step on X-axis** and **accuracy on Y-axis** 

.. video:: /_static/videos/task_compare.mp4
    :autoplay:
    :width: 600