.. meta::
    :description: The environment variables section lets you pass additional environment variables to your commands.


``step.environment-variables``
==============================

Environment variables are dynamic key-value pairs that running processes can write and read.
This also holds true in the context of Valohai.

You can define environment variables in three ways:

1. Simply write ``export MY_KEY="my-value"`` in your commands.
   This is the most flexible  way but won't be tracked or easily searchable in Valohai.
2. Define expected environment variables in the ``valohai.yaml``.
   You can define a default value which can be overwritten by the execution creator.
3. Define environment variables in the project settings.
   Any execution in the project can optionally be instructed to inherit the project environment variables.
   Project environment variables can be set to secret so they are not shown anywhere on the UI.

1. Environment variables in commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can define your environment variables in the commands like this:

.. code-block:: yaml

    - step:
        name: train-model
        image: python:3.6
        command:
        - export MODE="1"
        - export POST="clip"
        - python train.py

This is an acceptable approach if you are debugging, prototyping or the variables never change.

2. Environment variables in YAML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A better way is to explicitly define what environmental variables the execution expects:

.. code-block:: yaml

    - step:
        name: train-model
        image: python:3.6
        command: python train.py
        environment-variables:
          - name: MODE
            default: "1"
          - name: POST
            default: "clip"

A variable in ``environment-variables`` has four potential properties:

* ``name``: The environment variable name how it will be passed to the execution.
* ``description``: **(optional)** More detailed human-readable description of the variable.
* ``default``: **(optional)** Default value for the environment variable.
* ``optional``: **(optional)** Whether this environment variable is optional.
  All environment variables are optional by default so only ``optional: false`` would make sense.

This way the environment variables can easily be tracked and edited when creating executions either through
the graphical user interface, command-line client or API.

.. thumbnail:: environment-variables-execution.png
   :alt: Editing environment variables on the Valohai graphical user interface.

3. Project environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Project level environment variables are excellent for private keys when doing more advanced data source integrations;
or when you have some project-wide settings you want to share between executions.

Make sure that the ``[X] Inherit project's environment variables and secrets`` checkbox is ticked when creating
the execution.

.. thumbnail:: environment-variables-project.png
   :alt: Project environment variables are useful for secrets.
