.. meta::
    :description: A Python toolkit for the everyday Valohai boilerplate.

.. _valohai-utils:

Valohai-utils Python Toolkit
============================

One of the Valohai core design principles is to be an unopinionated agnostic platform. The user is not forced to use
any specific programming language, framework or SDK.

That said, Valohai offers a Python utility library called
``valohai-utils`` to help with the everyday boilerplate.

.. tip::

    This is an in-depth topic guide. If you are just starting out, check the :ref:`learning-paths-fundamentals` first.


Installation
------------

.. code-block:: bash

    pip install valohai-utils

Example Usage
-------------

train.py
########

.. code-block:: python

    import valohai


    params = {
        "iterations": 10,
        "learning-rate": 0.001,
    }

    inputs = {
        "train": "http://example.com/training_set.zip",
        "test": "http://example.com/test_set.zip",
    }

    valohai.prepare(step="train", default_parameters=params, default_inputs=inputs)

    for i in valohai.parameters("iterations").value:
        for path in valohai.inputs("train").paths():
            print(path)


What is it?
-----------

The ``valohai-utils`` is a generic utility library for the Valohai user. In general, it streamlines pipeline definition and writing Valohai-compatible code. This is achieved by offering utility functions for the most common tasks, which are all described in the sections below.

The library is designed to be used hand-in-hand with the `Valohai CLI </reference-guides/valohai-cli>`_. User can update the valohai YAML configuration based on ``valohai-utils`` powered code using the CLI commands ``vh yaml step`` and ``vh yaml pipeline``.

What it isn't?
---------------

The ``valohai-utils`` library is not a machine learning or data science library. It helps in OS-level tasks like figuring out the input file paths or parsing the command-line parameters. It does not tune hyperparameters or train a model.


.. toctree::
    :titlesonly:

    prepare()
    parameters
    inputs
    outputs
    logging







