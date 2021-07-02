.. meta::
    :description: Defining parameters with valohai-utils.

Parameters
==========

To parameterize a :doc:`step </topic-guides/core-concepts/steps>`, you need :doc:`parameters </topic-guides/core-concepts/parameters>`. They can be ``float``, ``integer``, ``string`` or ``boolean`` type.

With ``valohai-utils``, you define the parameters in the call to the :doc:`prepare </topic-guides/valohai-utils/prepare>` method. Feed the ``default_parameters`` argument with a key/value dictionary of the parameters.

* **key** is the name of the parameter. Used in the code, the YAML and the Valohai UI.
* **value** defines the default value of the parameter and also it's type.

.. note::

    Empty values are not supported as they have no type.

Defining parameters with ``valohai-utils`` solves two problems:

* Parsing the command-line overrides
* Managing the duplicate definitions between Python & YAML

train.py
--------

Here we define a :doc:`step </topic-guides/core-concepts/steps>` ``train``,
with a :doc:`parameter </topic-guides/core-concepts/parameters>` ``learning-rate``.

.. code-block:: python

    import valohai


    params = {
        "learning-rate": 0.001,
    }

    valohai.prepare(
        step="train",
        default_parameters=params,
    )

This key/value pair...

.. code-block:: python

    params = {
        "learning-rate": 0.001
    }

...will be transpiled into the following YAML

.. code-block:: yaml

    - name: learning-rate
      default: 0.001
      optional: false
      type: float

Accessing values
----------------

Once you have defined a parameter using the :doc:`prepare </topic-guides/valohai-utils/prepare>` method, you can access it in your code
by referring to the parameter name.

.. code-block:: python

    lr = valohai.parameters("learning-rate").value


Overriding values
-----------------

All parameters defined by the :doc:`prepare </topic-guides/valohai-utils/prepare>` method always have a default value.

There are two ways to override the default value:

* Command-line parameter (local)
* Valohai UI or CLI (remote)

Example (local):

.. code-block:: bash

    python train.py --learning-rate=.002

Example (remote):

.. code-block:: bash

    vh yaml step train.py
    vh exec run -a train --learning-rate=.002

.. seealso::

    * `Running a Grid Search </howto/tasks/grid-search/>`_
    * `Using the Bayesian Optimizer </howto/tasks/bayesian/>`_