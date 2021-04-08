:hide-toc:

.. meta::
    :description: Documentation of Valohai machine learning platform guides through the core concepts of the platform and helps to get started in injecting best practices of machine learning development to everyday work.

Welcome 👋
===========

Valohai is all about taking away the not-so-fun parts of machine learning. Managing cloud instances and writing glue code is neither valuable nor fun. Valohai takes care of that for you.

Get started with Valohai
**************************

Install the Valohai tools and create a new project.

.. code-block:: bash

    pip install valohai-cli valohai-utils
    vh login
    vh project create

..

Create a new file ``train.py``.

.. code-block:: python

    import valohai

    print("Hello Valohai!")

    valohai.prepare(step='hello')

..

Generate a configuration file and run a new execution.

.. code-block:: bash

    vh yaml step train.py
    vh exec run hello --adhoc
..

.. admonition:: See also
    :class: seealso

    * :ref:`quickstart` to learn about data, parameters, collecting metrics, and comparing executions.
    * :ref:`jupyter` add-on
    * :ref:`valohai-cli-tutorial`
    * :ref:`api`

..


How the documentation is organized
***********************************

A high-level overview of how our docs are organized will help you know where to look for certain things:

* :ref:`tutorials` take you by the hand through a series of steps to run your project on Valohai. Start here if you’re new to Valohai.
* :ref:`howto` include the steps involved in addressing key problems and use-cases. They are more advanced than tutorials and assume some knowledge of how Valohai works.
* :ref:`topicguides` discuss key topics and concepts at a fairly high level and provide useful background information and explanation.
* :ref:`referenceguides` contain technical reference for APIs and other aspects of Valohai. They describe how it works and how to use it but assume that you have a basic understanding of key concepts.

.. toctree::
    :maxdepth: 1
    :hidden:

    tutorials/index
    howto/index
    topic-guides/index
    reference-guides/index

