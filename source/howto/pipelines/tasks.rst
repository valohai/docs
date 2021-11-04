.. meta::
    :description: Using Tasks in a pipeline for parameter sweeps and hyperparameter optimization

.. _pipeline-tasks:

Run a task inside a pipeline
################################

.. admonition:: Quick recap
    :class: tip

    * :ref:`tasks` allow you to easily run parameter sweeps and hyperparameter optimization.
    * Use Tasks when you need to run the same code but with different parameters.

..

Tasks inside a pipeline come in handy when you need to run a hyperparameter optimization or parameter sweep as part of a pipeline.

All the outputs of the Task will be passed to the next node.

.. tab:: Web UI

    You can easily convert any existing execution node to a task node in the web ui.

    * Open your project's pipelines tab
    * Create a new pipeline
    * Select the right blueprint from the drop-down menu
    * Click on a node that has parameters
    * Click on **Convert to task** (below the graph)
    * Scroll down to the **Parameters** section and configure your Task
    * Create a pipeline


    .. video:: /_static/videos/pipeline-task.mp4
        :autoplay:
        :nocontrols:
        :width: 500

.. tab:: YAML

    You can define a Task in your :ref:`yaml` by setting the node's execution type to task.

    .. code-block:: yaml
        :linenos:
        :emphasize-lines: 8

        - pipeline:
            name: Training Pipeline
            nodes:
            - name: preprocess
                type: execution
                step: Preprocess dataset (MNIST)
            - name: train
                type: task
                step: Train model (MNIST)
                override:
                inputs:
                    - name: training-set-images
                    - name: training-set-labels
                    - name: test-set-images
                    - name: test-set-labels
            - name: evaluate
                type: execution
                step: Batch inference (MNIST)
            edges:
            - [preprocess.output.*train-images*, train.input.training-set-images]
            - [preprocess.output.*train-labels*, train.input.training-set-labels]
            - [preprocess.output.*test-images*, train.input.test-set-images]
            - [preprocess.output.*test-labels*, train.input.test-set-labels]
            - [train.output.model*, evaluate.input.model]
    ..

Dynamically defining a Task inside a pipeline
---------------------------------------------

You can use an execution node to parametrize a downstream task node's variations by printing out metadata and defining an edge that connects the metadata to the Task's parameter.

List-shaped metadata from executions is automatically "spread" into a Multiple variant parameter if the destination node is a Task.

See the example below where we have two files:

1) ``preprocess.py`` will generate a list of store IDs
2) ``train.py`` will train a model for each store, using the store ID that it gets

``preprocess.py``

.. code-block:: python

    import json

    # Your logic to fetch the right values...

    storeids = [122,154,209,916,345]

    # Print out a list as metadata
    print(json.dumps({
        "storeids": storeids
    }))

``train.py``

.. code-block:: python

    import valohai

    storeid = valohai.parameters('id').value

    # train model...

And the ``valohai.yaml`` that defines our steps, and the pipeline.
In the pipeline's edge we pass the ``storeids`` from ``preprocess`` to the ``train`` Task's ``id`` parameter. This will create a ``train`` task with a set of multiple values for the ``id`` parameter (in our example, a Task with 5 executions, each with it's own ID parameter value)

.. code-block:: yaml
   :linenos:
   :emphasize-lines: 11,25

   - step:
       name: preprocess
       image: python:3.7
       command:
         - python ./preprocess.py
   - step:
       name: train
       image: python:3.7
       command:
         - pip install valohai-utils
         - python ./train.py {parameters}
       parameters:
       - name: id
         type: string
   - pipeline:
       name: dynamic-task
       nodes:
       - name: preprocess
         step: preprocess
         type: execution
       - name: train
         step: train
         type: task
       edges:
       - [preprocess.metadata.storeids, train.parameter.id]


.. image:: /_images/task_in_pipeline.png
    :alt: Dynamically defined Task in a pipeline
