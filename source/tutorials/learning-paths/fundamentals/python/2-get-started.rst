.. meta::
    :description: Valohai Fundamentals learning path - Running your first Valohai execution

Getting started
####################

.. include:: ../_shared/_intro.rst

.. include:: ../_shared/_2-get-started.rst

Define a Valohai configuration file
------------------------------------

Now we'll create a :ref:`yaml` for your project. Run the following commands from your command line:

.. code-block:: 

    # Initialize a new Valohai project in this directory
    vh init

    # Confirm the directory (y)

    # valohai-cli will look for any Python files in your directory
    # it will find our train.py and
    # ask if that's the script file you want to use as the command

    # Choose train.py by typing 1
    # Confirm selection (y)

    # Choose a Docker image from the list, or input your own image
    # Choose tensorflow/tensorflow:2.1.0-py3 by typing 12

    # You'll see a preview of the valohai.yaml configuration file
    # accept it (y) to generate the file

Now edit the file and change the name of the step to ``train-model``:

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 4

    ---

    - step:
        name: train-model
        image: tensorflow/tensorflow:2.1.0-py3
        command: python train.py
        #inputs:
        #  - name: example-input
        #    default: https://example.com/
        #parameters:
        # - name: example
        #   description: Example parameter
        #   type: integer
        #   default: 300

Run in Valohai
------------------------

Finally, we run the following commands in the the command line, on your own computer:

.. code:: bash

    vh exec run train-model --adhoc

..
        
.. include:: ../_shared/_2-get-started-end.rst

Next: `Upload output data </tutorials/leaning-paths/fundamentals/python/3-outputs/>`_ 