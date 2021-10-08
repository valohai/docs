Finally run a new Valohai execution.

.. code:: bash

    vh exec run train-model --adhoc

..

Rerun an execution with different parameter values
-------------------------------------------------------

* **Open your project** on `app.valohai.com <https://app.valohai.com>`_
* **Open the latest execution**
* Click **Copy**
* Scroll down to the **Parameters** section
* Change the value of **epochs**
* Click **Create execution**


.. video:: /_static/videos/execution_parameters.mp4
    :autoplay:
    :width: 600

.. tip::

    You can also run a new execution with different parameter values from the command line:

    ``vh exec run train-model --adhoc --epochs=10``

.. seealso::

    * Core concept: :ref:`parameters`
    * Core conept: `Hyperparameter search </topic-guides/core-concepts/parameters/#hyperparameter-search>`_
    * Tutorial: :ref:`task-grid-search`
..
