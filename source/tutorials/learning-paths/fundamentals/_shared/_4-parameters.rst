
.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`learning-paths-fundamentals` series.
..

This section will show you how to use parameters in Valohai. Defining parameters will allow you to easily rerun your executions and experiment with a different set of values.

In this section you will learn:

- How to define Valohai parameters
- How to change parameter values between executions both in the CLI and in the UI
- Defining Valohai parameters will allow you to easily rerun your executions and experiment with a different set of values.

.. admonition:: A short intro to parameters
    :class: tip

    * A Valohai parameter can be a string, an int, a float or a flag (=bool).
    * The default values for parameters are define in your code. These can be changed when creating an execution from the UI, command-line or API.
    * Parameters get passed to each Valohai execution as command-line arguments (e.g. ``train.py --epoch=5``)

..
