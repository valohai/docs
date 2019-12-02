.. meta::
    :description: How to handle hyperparameters and hyperparameter searching.

Parameters
==========

The wikipedia definition of hyperparameter: "a parameter whose value is set before the learning process begins".

In Valohai, the hyperparameters are a subset of :doc:`parameters </valohai-yaml/step-parameters>`. To define a parameter,
you add it as part of your step configuration in ``valohai.yaml``.

Defining parameters
~~~~~~~~~~~~~~~~~~~

Example of ``valohai.yaml``:

.. code-block:: yaml

    - step:
        name: train
        image: python:3.6
        command:
          - python train.py {parameters}
        parameters:
          - name: max_steps
            pass-as: --max_steps={v}
            type: float
            default: 300
          - name: learning_rate
            pass-as: --learning_rate={v}
            type: float
            default: 0.001
          - name: dropout
            pass-as: --dropout={v}
            type: float
            default: 0.9

The above would generate the following commands by default:

.. code-block:: bash

    python train.py --max_steps=300 --learning_rate=0.001 --dropout=0.9

Selecting values
~~~~~~~~~~~~~~~~

When you create a new Valohai execution using the UI, look for the parameter values subsection at the bottom.

.. thumbnail:: /_images/exec_params.png
   :alt: Execution parameters.

Default values of parameters are defined by the ``valohai.yaml``, but they can be tweaked in the UI. All changes
are version controlled as part of a Valohai execution.

Hyperparameter search
~~~~~~~~~~~~~~~~~~~~~

It can be daunting to try different hyperparameters one-by-one. Valohai offers a mechanism to do
hyperparameter searches using parallel executions and a grid search. These are called :doc:`tasks </core-concepts/tasks>`.

When starting a task, instead of a single value for a single hyperparameter, you get to define multiple values at once.
There are 5 different modes to choose from (Single, Multiple, Linear, Logspace, Random).

Single
~~~~~~

.. thumbnail:: /_images/hyperparam_single.png
   :alt: Hyperparameter (single).

Single means just a single value for a hyperparameter you do not want to search for.

Multiple
~~~~~~~~

.. thumbnail:: /_images/hyperparam_multiple.png
   :alt: Hyperparameter (multiple).

Multiple means a list of all the values to try for a specific hyperparameter. For example, here we are trying out
4 different values (0.81, 0.84, 0.86 and 0.91).

Logspace
~~~~~~~~

.. thumbnail:: /_images/hyperparam_logspace.png
   :alt: Hyperparameter (logspace).

Logspace is a search with values inside a specific range in logarithmic space. For example, here we are trying out
4 different values between 2^2 - 2^8 (base^start - base^end)

Random
~~~~~~~~

.. thumbnail:: /_images/hyperparam_random.png
   :alt: Hyperparameter (random).

Finally, if you want to "gamble", you can search randomly with a specified range and distribution.
For example, here we are trying out 10 different random values between 0.001 and 0.002.

Grid search
~~~~~~~~~~~

.. thumbnail:: /_images/gridsearch.png
   :alt: Grid search.

When we are searching for multiple values for multiple hyperparameters, all permutations are searched. This is also
called grid search.

For example, here we have 6 different values for learning_rate and 6 different values for dropout. In total this is
6*6 = 36 executions. Valohai calculates the number for permutations for you and you can see it in the right bottom corner
of this screenshot.
