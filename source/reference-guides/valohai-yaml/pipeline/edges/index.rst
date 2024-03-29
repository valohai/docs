.. meta::
    :description: Pipeline edges connect workload nodes of Valohai pipelines, defining their requirements.

``pipeline.edges``
==================

Pipeline edges model the data flow through your pipeline.

Edges are unidirectional links and they have **a source node** and **a target node**.

* **a source node** promises to produce some information e.g. files or metadata
* **a target node** requires the information that the source provides

Each edge has two traits; source trait to listen to and target trait to pass it to.

Valid **source node edge traits** you can listen for are:

* **output**: these outputs of the source execution will be passed to the paired execution.
* **parameter**: these parameters of the source execution will be passed to the paired execution.
* **metadata**: metadata produced during the execution will be passed to the paired execution.

Valid **target node edge traits** you can specify are:

* **input**: this execution node requires files from the specified execution outputs.
* **parameter**: this execution node requires parameters from the specified execution outputs.
* **file**: this deployment node requires files from a specified execution output.

| For example:
| ``[gather-node.output.images*, train-node.input.dataset-images]``
| means that all files starting with the name **images*** under **/valohai/outputs** of the source node execution will be passed to the input directory **/valohai/inputs/dataset-images** of the target node execution.

Edge Shorthand Syntax
~~~~~~~~~~~~~~~~~~~~~

| The simplest syntax to define edges is,
| ``[<SOURCE>, <TARGET>]``
|
| Both **<SOURCE>** and **<TARGET>** have 3 properties separated by dots; ``node``, ``type`` and ``key``.
| Thus the shorthand syntax becomes:
| ``[<NODE>.<TYPE>.<KEY>, <NODE>.<TYPE>.<KEY>]``

In practice, shorthand syntax looks something like this:

.. code-block:: yaml

    # define "generate-dataset" and "train-model" steps above...
    - pipeline:
        name: gatherer-pipeline
        nodes:
          - name: gather-node
            type: execution
            step: gather-dataset
          - name: train-node
            type: execution
            step: train-model
          - name: deploy-node
            type: deployment
            deployment: MyDeployment
            endpoints:
              - predict-digit
        edges:
          - [gather-node.output.images*, train-node.input.dataset-images]
          - [gather-node.output.labels*, train-node.input.dataset-labels]
          - [train-node.output.model*, deploy-node.file.predict-digit.model]

    - endpoint:
        name: predict-digit
        description: predict digits from image inputs ("file" parameter)
        image: tensorflow/tensorflow:1.13.1-py3
        wsgi: predict_wsgi:predict_wsgi
        files:
          - name: model
            description: Model output file from TensorFlow
            path: model.pb

Edge Full Syntax
~~~~~~~~~~~~~~~~

You can also define edges as full objects with ``source`` and ``target`` expanded instead of the shorthand
syntax.

.. code-block:: yaml

    # define "generate-dataset" and "train-model" steps above...
    - pipeline:
        name: gatherer-pipeline
        nodes:
          - name: gather-node
            type: execution
            step: gather-dataset
          - name: train-node
            type: execution
            step: train-model
        edges:
          - source: gather-node.output.images*
            target: train-node.input.dataset-images
          - source: gather-node.output.labels*
            target: train-node.input.dataset-labels
          - source: train-node.output.model*
            target: deploy-node.file.predict-digit.model
