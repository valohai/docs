.. meta::
    :description: Logging with valohai-utils.

``valohai.metadata.logger()``
=============================

When your training code is running on the Valohai platform, it is a good idea to store some metadata
or metrics for the model training performance.

Everything you ``print()`` during a remote execution is collected and stored by Valohai as raw logs.

To save the explicitly tracked metrics -- the execution metadata -- you need to print them out as a JSON object.

The ``valohai-utils`` custom logger automatically handles the grouping of the metrics into a single JSON object.

.. code-block:: python

    import valohai

    for i in range(3):
        with valohai.metadata.logger() as logger:
            logger.log("iteration", i)
            logger.log("accuracy", 0.001)
            logger.log("loss", 12.456)

This example would print:

.. code-block:: Python

    {"iteration": 0, "accuracy": 0.001, "loss": 12.456}
    {"iteration": 1, "accuracy": 0.001, "loss": 12.456}
    {"iteration": 2, "accuracy": 0.001, "loss": 12.456}

It is important to use the ``with`` block so that the logger knows how to group the metrics of a single iteration.

The metrics of a single ``iteration``, ``epoch`` or similar, need to be grouped into
a single JSON object printout. If printed out as separated objects, the platform doesn't understand
them as a meaningful set.

.. seealso::

    * `Compare executions </howto/executions/compare/>`_
    * `Save graphs from executions </howto/executions/complex-visualizations/>`_