.. meta::
    :description: Explaining the valohai-utils prepare() method.

``valohai.prepare()``
=====================

In Valohai jargon, a :doc:`step </topic-guides/core-concepts/steps>` is a piece of code that performs a single operation like "train" or "preprocess".
A single step is defined by calling the ``valohai.prepare()`` method.

Under the hood, Valohai steps are always defined in the `valohai.yaml </reference-guides/valohai-yaml>`_ config file. What ``valohai-utils``
offers is a shortcut for defining the step in your Python code. Those steps can then be transpiled into
corresponding YAML using the Valohai CLI.

train.py
----------------------------------------

.. code-block:: python

    import valohai


    params = {
        "learning-rate": 0.001,
    }

    inputs = {
        "training-set": "http://example.com/training_set.zip",
    }

    valohai.prepare(
        step="train",
        default_parameters=params,
        default_inputs=inputs,
        image="tensorflow/tensorflow:gpu"
    )

Here we define a :doc:`step </topic-guides/core-concepts/steps>` ``train``,
with a :doc:`parameter </topic-guides/core-concepts/parameters>` ``learning-rate``
and an :doc:`input </reference-guides/valohai-yaml/step-inputs>` ``training-set``.

We also define default values and a default Docker image
``tensorflow/tensorflow:gpu``. The Docker image is used during remote execution on the Valohai platform.

Valohai platform is agnostic and doesn't understand Python directly. It can only understand YAML and OS-level commands (bash). Thus, this step needs to be transpiled into YAML and bash using the Valohai command-line client.

To update our YAML, we use the ``vh yaml step`` command.

.. code-block:: bash

    vh yaml step train.py

valohai.yaml (generated)
----------------------------------------

.. code-block:: yaml

    - step:
        name: train
        image: tensorflow/tensorflow:gpu
        command:
        - pip install -r requirements.txt
        - python ./test.py {parameters}
        parameters:
        - name: learning-rate
          default: 0.001
          optional: false
          type: float
        inputs:
        - name: training-set
          default:
          - http://example.com/training_set.zip
          optional: false


This solves two main issues:

* Writing the YAML manually
* Managing the duplicate definitions between Python & YAML

What does the prepare() actually do?
------------------------------------------

The ``prepare()`` method has a dual purpose.

1. Define a Valohai :doc:`step </topic-guides/core-concepts/steps>`
2. Parse the command-line overrides

3. Define a Valohai step
----------------------------------------
To define a step, the call to the ``prepare()`` method doesn't actually do anything. It just acts as a decorator.
A decorator for what? A decorator for the ``vh yaml step`` command.

When the ``vh yaml step train.py`` CLI command is executed, the ``train.py`` is parsed by the CLI program.

.. important::

	Parsing is not the same as executing!

	Parsing here means that the parser parses through the source code file and looks for the call to the ``prepare()`` method.

Once found, the parser grabs the step name, parameters, inputs and the Docker image. With this newly aquired information, the YAML
representation of the step can be generated.

This is why we call the ``prepare()`` method a decorator.

.. note::

    Because the parser doesn't execute the Python file - it simply parses it - you can't use variables for your definitions.

    This works:

    ``inputs = {"training-set": "http://example.com/training_set.zip"}``

    This does **not** work:

    ``inputs = {"training-set": f"http://{my_domain}/training_set.zip"}``

    The value of ``my_domain`` variable is unknown to the parser and the parsing will fail.

2. Parse the command-line overrides
------------------------------------------------------------

If the ``prepare()`` was simply a decorator, it would not do anything. But it actually does, because it
has another purpose in life: Parsing the command-line overrides.

If we use the ``prepare()``, we have the opportunity to override default values via command-line. **You can override
both the parameters and the inputs** of a step.

Let's say we have the ``train.py`` from our earlier example.

.. code-block:: python

    import valohai


    params = {
        "learning-rate": 0.001,
    }

    inputs = {
        "training-set": "http://example.com/training_set.zip",
    }

    valohai.prepare(
        step="train",
        default_parameters=params,
        default_inputs=inputs,
        image="tensorflow/tensorflow:gpu"
    )

We can now override ``learning-rate`` and ``training-set``:

.. code-block:: bash

    python train.py --learning-rate=.002 --training-set=https://alt.com/training_set_2.zip

This means that you don't need to go through the hassle of writing your custom parser for the command-line
parameters. The ``prepare()`` method does that for you.

