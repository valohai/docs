.. meta::
    :description: How to handle hyperparameters and hyperparameter searching.

.. _parameters:

Parameters
############

.. seealso::

    For the technical specifications, go to :doc:`valohai.yaml step.parameters section </reference-guides/valohai-yaml/step-parameters>`.

The Wikipedia definition of **a hyperparameter** is: "a parameter whose value is set before the learning process begins."
This definition exists to differentiate these values that control how the machine learning is conducted from
parameters such as neural network weights that are actively changed during training.
Thus, hyperparameters are a subset of parameters.

In the context of Valohai, all parameters to be recorded are defined before launching an execution. If you wish to
record something that is defined or changes during runtime, use :doc:`Valohai metadata </topic-guides/executions/metadata/index>`.

.. note::

    Valohai supports numerous workloads in addition to normal machine learning training such as data generation
    and feature extraction. Check out :doc:`What is Valohai? page </topic-guides/core-concepts/index>` to learn
    what else could be achieved.

    This is the reason why we don't always use the training-centric *hyperparameter* term.


Defining parameters
~~~~~~~~~~~~~~~~~~~

To keep track of parameters in Valohai, you add them as part of your :doc:`YAML step.parameters </reference-guides/valohai-yaml/step-parameters>`.

Example of a ``valohai.yaml`` with a step defining 3 parameters:

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

The above would generate the following command by default:

.. code-block:: bash

    python train.py --max_steps=300 --learning_rate=0.001 --dropout=0.9

You can then parse the command-line arguments in your script.

.. code-block:: python

   import argparse

   def parse_args():
      parser = argparse.ArgumentParser()
      parser.add_argument('--max_steps', type=int, default=300)
      parser.add_argument('--learning_rate', type=float, default=0.001)
      parser.add_argument('--dropout', type=float, default=0.9)
      return parser.parse_args()

   args = parse_args()
   print("Max steps: %s" % args.max_steps)

.. admonition:: valohai-utils
   :class: important

   Python users can use the valohai-utils helper library to define and parse parameters.

   .. code:: python

      import valohai

      my_parameters = {
         'max_steps': 300,
         'learning_rate': 0.001,
         'dropout': 0.9,
      }

      valohai.prepare(step="helloworld", default_parameters=my_parameters)

      print("Max steps: %s" % valohai.parameters('max_steps').value)

   ..

   and generate ``valohai.yaml`` configuration file with the parameter definitions:

   .. code:: bash

      vh yaml step helloworld.py
      vh exec run helloworld --adhoc
   ..



Selecting values
~~~~~~~~~~~~~~~~

When you are creating a new Valohai execution using the web user interface, look for the ``Parameters`` subsection at the bottom.

.. thumbnail:: /_images/exec_params.png
   :alt: Execution parameters.

Default values of the parameters are defined by the ``valohai.yaml``, but they can be tweaked in
the web user interface, command-line client or the API.
All changes are version controlled as part of a Valohai execution.

Hyperparameter search
~~~~~~~~~~~~~~~~~~~~~

It can be daunting to try different hyperparameters one-by-one. Valohai offers a mechanism to do
hyperparameter searches using parallel executions and a grid search. These are called :doc:`tasks </topic-guides/core-concepts/tasks>`.

When starting a task, instead of a single value for a single hyperparameter, you get to define multiple values at once.
There are various modes to choose from e.g. Single, Multiple, Linear, Logspace and Random.

Single
------

.. thumbnail:: /_images/hyperparam_single.png
   :alt: Hyperparameter (single).

Single means just a single value for a hyperparameter you do not want to search for.

Multiple
--------

.. thumbnail:: /_images/hyperparam_multiple.png
   :alt: Hyperparameter (multiple).

Multiple means a list of all the values to try for a specific hyperparameter. For example, here we are trying out
4 different values (0.81, 0.84, 0.86 and 0.91).

Logspace
--------

.. thumbnail:: /_images/hyperparam_logspace.png
   :alt: Hyperparameter (logspace).

Logspace is a search with values inside a specific range in logarithmic space. For example, here we are trying out
4 different values between 2^2 - 2^8 (base^start - base^end)

Random
------

.. thumbnail:: /_images/hyperparam_random.png
   :alt: Hyperparameter (random).

Finally, if you want to "gamble", you can search randomly with a specified range and distribution.
For example, here we are trying out 10 different random values between 0.001 and 0.002.

Grid search
-----------

.. thumbnail:: /_images/gridsearch.png
   :alt: Grid search.

When we are searching for multiple values for multiple hyperparameters, all permutations are searched. This is also
called grid search.

For example, here we have 6 different values for learning_rate and 6 different values for dropout. In total this is
6*6 = 36 executions. Valohai calculates the number for permutations for you and you can see it in the right bottom corner
of this screenshot.


Bayesian optimization
----------------------

Using interactive hyperparameter optimisation can make hyperparameter tuning faster and more efficient than for example using a random search or an exhaustive grid search.

Valohai uses the open source Hyperopt-library’s Tree Parzen Estimator algorithm to use the hyperparameters and outputs of the previous executions to suggest future execution hyperparameters.

Under the hood, Bayesian optimization (of which TPE is an implementation) works in the following steps:

* Create startup executions using random search
* Based on these executions, create a simplified function to model the relationship between the hyperparameters and the target metric value (for example “loss”)
* Based on this simplification of their relationship, find the optimal values for the hyper parameter to make the target metric as close to the target value as possible
* Run the next batch of executions and repeat the process from step 2.

.. image:: /_images/bayesian_ui.gif
   :alt: Bayesian optimization.
