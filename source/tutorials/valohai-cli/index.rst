.. meta::
    :description: Valohai CLI is a command-line client to manage your deep learning model lifecycle.

.. _valohai-cli-howto:


Valohai CLI client
###############################


Valohai CLI (command-line interface) is a Python command-line client to manage Valohai projects.
``valohai-cli`` is an optional way of interacting with projects in the same capacity as our web user interface and API.

The command-line interface is best suited for iterative development, debugging and automation.


Using valohai-cli
------------------------

``valohai-cli`` supports Python 3.4+ and works on macOS, Windows and Linux.

You can install ``valohai-cli`` from pip:

.. code-block:: bash

    pip install valohai-cli

And now you have ``vh`` command available in your terminal.

.. code-block:: bash

    vh
    # Usage: vh [OPTIONS] COMMAND [ARGS]...

If you want to get an overview how the client works, check out :doc:`our Valohai CLI quick start </tutorials/valohai-cli/index>`.

.. toctree::
    :titlesonly:
    :maxdepth: 1

    quick-start-cli
    using-environments
    using-inputs
    