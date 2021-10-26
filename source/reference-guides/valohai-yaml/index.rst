.. meta::
    :description: The valohai.yaml configuration file defines how the platform runs your experiments. It must be placed at the root of your project version control repository. Read how to create a YAML file for managing steps in a machine learning pipeline.


.. _yaml:

``valohai.yaml`` config file
==============================

The ``valohai.yaml`` configuration file defines steps of your machine learning pipeline.

The configuration file is optional but we recommend adding it so everything stays reproducible between
different Valohai projects using the same git repository. The configuration file must be placed at the root
of your project repository.

Here is a "Hello World" step on ``valohai.yaml`` to print "hello" on a worker machine:

.. code-block:: yaml

    - step:
        name: greet-me
        image: busybox
        command: echo hello

.. seealso::

    `busybox <https://hub.docker.com/_/busybox>`_ is one of the simplest Docker images in existence
    as it includes only the most basic Unix utilities. You can either utilize
    :doc:`freely available images from Docker Hub </howto/docker/index>` or
    :doc:`build your own. </howto/docker/docker-build-image>`

This section describes how to write ``valohai.yaml`` files in more detail.

.. toctree::
    :titlesonly:

    step
    step-name
    step-image
    step-command
    step-parameters
    step-inputs
    step-environment
    step-environment-variables
    pipeline/index
    pipeline/nodes/index
    pipeline/edges/index
    endpoint/index
    endpoint/server-command/index
    endpoint/wsgi/index
    example-tensorflow-mnist
