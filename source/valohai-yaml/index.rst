.. meta::
    :description: The valohai.yaml configuration file defines how the platform runs your experiments. It must be placed at the root of your project version control repository. Read how to create a YAML file for managing steps in a machine learning pipeline.

Valohai YAML
============

The ``valohai.yaml`` configuration file defines steps of your machine learning pipeline.

The configuration file is optional but we recommend adding it so everything stays reproducible between different Valohai projects using the same git repository. The configuration file must be placed at the root of your project repository.

Here is a very simple ``valohai.yaml`` to print "hello" on a worker machine with Python 3.6.

.. code-block:: yaml

    - step:
        name: greet-me
        image: python:3.6
        command: echo hello

.. toctree::
    :titlesonly:

    step
    step-environment
    step-image
    step-command
    step-inputs
    step-parameters
    example-tensorflow-mnist
