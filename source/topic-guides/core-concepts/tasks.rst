.. meta::
    :description: What are Valohai tasks? Launch hundreds of distributed hyperparameter optimizations on the cloud.

Tasks
=====

**Tasks** are collections of related executions, where you run the same step/code with different parameter and input data values.

The most common task is hyperparameter optimization where you execute a single step with various
parameter configurations to find the most optimal neural network layout, weights and biases.

Tasks can be created with any step that has parameters defined. 

.. seealso::

    * :ref:`parameters`
    * :ref:`bayesian`

..

.. image:: task-execution-table.jpg
   :alt: Tasks are frequently used for hyperparameter sweeps and random search.
