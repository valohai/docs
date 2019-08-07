.. meta::
    :description: Automate your machine learning workflow with Valohai pipelines.

``pipeline``
============

Pipelines automate your machine learning operations on Valohai ecosystem.

.. seealso::

    You can read more about the reasoning behind general pipeline concepts like
    graphs, nodes and edges on the :doc:`/core-concepts/pipelines` core concepts page.

``pipeline`` definition has 3 required properties:

* ``name``: name for the pipeline
* ``nodes``: list of all :doc:`nodes </valohai-yaml/pipeline/nodes/index>` (executions) in the pipeline
* ``edges``: list of all :doc:`edges </valohai-yaml/pipeline/edges/index>`  (requirements) between the nodes

A simple pipeline could look something like this:

.. code-block:: yaml

    # define "generate-dataset" and "train-model" steps above...
    - pipeline:
        name: simple-pipeline
        nodes:
          - name: generate
            type: execution
            step: generate-dataset
          - name: train
            type: execution
            step: train-model
        edges:
          - [generate.output.images*, train.input.dataset-images]
          - [generate.output.labels*, train.input.dataset-labels]

Here we have a pipeline with 2 nodes, and the second node **train** will wait its inputs to be generated
by **generate** node. All files in ``/valohai/outputs`` that start with either ``images`` or ``labels`` will be passed
between the executions.

.. seealso::

    * :doc:`pipeline.nodes </valohai-yaml/pipeline/nodes/index>`
    * :doc:`pipeline.edges </valohai-yaml/pipeline/edges/index>`
