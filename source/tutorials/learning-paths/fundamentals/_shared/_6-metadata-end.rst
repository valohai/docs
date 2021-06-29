
Run in Valohai
------------------------

Adding or changing metadata doesn't require any changes to the :ref:`yaml`.

You can immediately launch a new execution and view the collected metadata.

.. code:: bash

    vh exec run train-model --adhoc

..

View metrics
-------------------

* Go to your project's executions
* Click on the **Show columns** button on the right side, above the table
* **Select accuracy and loss** to show them in the table.
* **Open the latest execution**
* **Go to the metadata tab** to view metrics from that executions.
* Select **epoch on X-axis** and **accuracy and loss on Y-axis**

.. admonition:: Latest metada value
    :class: Important

    The metadata value displayed in the table is always the latest printed metadata. In your script you should ensure that the last value you print out for ``accuracy`` is the best value for your use case.

.. video:: /_static/videos/execution_metadata.mp4
    :autoplay:
    :width: 600

.. seealso::

    * :ref:`executions-compare`
    * :ref:`executions-graphs`

..