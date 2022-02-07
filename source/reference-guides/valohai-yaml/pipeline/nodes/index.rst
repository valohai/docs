.. meta::
    :description: Valohai pipelines consist of various nodes for e.g. data preprocessing, training, evaluation and data generation.

``pipeline.nodes``
==================

``pipeline.nodes`` is **an array of objects**, each object having the following properties:

* ``name``: name of the node, used in edge definitions ``edges:``
* ``type``: type of the node, accepts "execution", :doc:`step "task" </howto/pipelines/tasks/>`, or "deployment"
* ``step``: name of the step to be executed, defined in the same file
* ``override``: **(optional)** override values defined in the original :doc:`step </reference-guides/valohai-yaml/step>`

Other than that, pipeline execution nodes behave like you would expect:

* it will use the defaults from the original step
* you can customize the parameters and inputs before starting the pipeline
* you can override values when defining the pipeline using the ``override:`` syntax

Note that separate nodes in a pipeline can implement the same step multiple times.

.. code-block:: yaml

    # define "gather-dataset" and "train-model" steps above...
    - pipeline:
        name: gatherer-pipeline
        nodes:
          - name: gather-node
            type: execution
            step: gather-dataset
          - name: train-node
            type: execution
            step: train-model
            override:
              image: tensorflow/tensorflow:1.13.1-py3
          - name: deploy-node
            type: deployment
            deployment: predict-digit
            endpoints:
              - predict-digit
        edges:
          - [gather-node.output.images*, train-node.input.dataset-images]
          - [gather-node.output.labels*, train-node.input.dataset-labels]
          - [train-node.output.model*, deploy-node.file.predict-digit.model]
