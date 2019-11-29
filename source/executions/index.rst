.. meta::
    :description: Execution is an abstraction of a machine learning workload in the Valohai ecosystem.

Workload Management
===================

We encapsulate machine learning workloads in entities called **executions**.
An execution is a similar concept as "a job" or "an experiment" in other systems,
but emphasis being that an execution is a smaller piece in a much larger data science process.

Simply put, an execution is one or more commands run on a remote server, check out
:doc:`Executions documentation page </core-concepts/executions>` to learn more about the high level
principles of executions.

Executions can be anything from data generation and preprocessing to model training and evaluation;
:doc:`What is Valohai? page </core-concepts/what-is-valohai>` explains different use-cases in more detail.

.. note::

    Your executions can be said to implement **a step** e.g. "preprocessing" or "training".
    Steps are defined in :doc:`the valohai.yaml configuration file </valohai-yaml/index>`. If your project doesn't
    yet have a ``valohai.yaml`` defined, your executions don't implement any step.

This section explains how to run and manage data science workloads on Valohai.

.. toctree::
    :titlesonly:

    lifecycle/index
    placeholder-config/index
    file-config/index
    envvar-config/index
    logs/index
    metadata/index
    inputs/index
    outputs/index
    live-outputs/index
