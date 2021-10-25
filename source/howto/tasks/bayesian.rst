
.. meta::
    :description: Using interactive hyperparameter optimisation can make hyperparameter tuning faster and more efficient than for example using a random search or an exhaustive grid search.

.. _bayesian:

Using the Bayesian optimizer
################################

.. admonition:: Prerequirements
  :class: attention

  * A Valohai project that is connected to a Git-repository.
  * At least one :ref:`step` with parameters defined. Follow our :ref:`migrate-parameters` tutorial to create a step with parameters.

..

Create a Valohai Task
----------------------

* Go to your Project and open the Task page
* Click on **Create task**
* Choose the step where you defined your parameters
* Scroll down to the **Parameters section**
* Select **Bayesian optimization** as the Task type

Now set your prefered settings:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Setting
     - Description
   * - Early stopping
     - Allows you to set early stopping criteria based on the Tasks :ref:`migrate-metadata`. When one of the executions from the Task meets this criteria, the whole Task will be stopped.
   * - Optimization engine
     - By default Valohai will use `Optuna <https://optuna.org/>`_ but you can also choose to use `HyperOpt <https://github.com/hyperopt/hyperopt>`_ as the engine.
   * - Maximum execution count
     - Defines how many executions can Valohai launch in total for this Task. We recommend the execution count is over 30.
   * - Execution batch size
     - Valohai will run the executions in batches. This defines how many executions will be ran in a single batch.
   * - Optimization target metric
     - Defines which :ref:`metadata` metric you're looking to optimize.
   * - Optimization target value
     - Target value for your :ref:`metadata` metric


* Click **Create Task** to start your Task.

.. image:: /_images/bayesian_ui.gif
   :alt: Bayesian optimization.


.. admonition:: Use Bayesian optimization only when the execution count is over 30
    :class: warning

    We recommend to use Bayesian optimization when creating more than 30 executions to ensure the optimiser has enough base values to use TPE effectively.

    Valohai follows the Hyperopt recomendation and executes the first 20 runs with Random Search before using the TPE to ensure best results. If you have less than 20 runs, the executions will be based on Random Search instead of TPE optimisation.

..
