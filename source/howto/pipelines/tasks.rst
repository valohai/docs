.. meta::
    :description: Using Tasks in a pipeline for parameter sweeps and hyperparameter optimization

.. _pipeline-tasks:

Run a Task inside a pipeline
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

