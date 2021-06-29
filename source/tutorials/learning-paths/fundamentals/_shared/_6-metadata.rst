.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`learning-paths-fundamentals` series.
..

Valohai allows you to easily collect metadata, such as key performance metrics from executions, visualize it and compare it across multiple executions. 

In this section you will learn:

- How to collect metadata
- How to visualize metadata in the UI
- How to compare metadata between executions

.. admonition:: A short introduction to metadata
    :class: tip

    * Valohai metadata is collected as key:value pairs
    * Easily visualized as a time series graph or a scatter plot in the web app
    * Used to compare performance of multiple executions
    * Sort and find executions based on metadata metrics

..

Update **train.py** to add metadata logging: