.. meta::
    :description: Creating pipelines with valohai-utils helper library.

.. _pipeline-utils:

Create pipelines by using valohai-utils
#######################################

It's possible to define pipelines using the ``valohai-utils`` helper library, in addition to manually defining them in the ``valohai.yaml`` configuration file.
First, create a file with the instructions how to build the pipeline in it (see the example below). Remember to define the nodes and edges according to the steps you have in your `valohai.yaml` file. 

.. note::

    When creating the ``valohai.yaml`` and updating the step information with ``vh yaml step <filename>`` the code in the file is only parsed and not executed. For ``vh yaml pipeline <filename>`` the ``main`` method is actually run.

..

.. code-block:: python

    from valohai import Pipeline
    
    def main(config) -> Pipeline:
        
        #Create a pipeline called "mypipeline".
        pipe = Pipeline(name="mypipeline", config=config)
        
        # Define the pipeline nodes.
        train = pipe.task("train-model")
        test = pipe.execution("test")
        
        # Configure the pipeline, i.e. define the edges.
        train.output("*").to(test.input("models"))
        
        return pipe
..

Next, run the command:

.. code-block::

    vh yaml pipeline <filename>
..

If you now check your ``valohai.yaml``, you might notice that the pipeline block looks different from that described in the section :ref:`quickstart-pipeline`. The quickstart uses the `shorthand syntax </reference-guides/valohai-yaml/pipeline/edges/#edge-shorthand-syntax>`_ but ``valohai-utils`` doesn't. Regardless, the pipeline will be built in a similar manner in the UI. 

.. code-block:: YAML

    - pipeline:
        name: mypipeline
        edges:
        - configuration: {}
          source: train-model_1.output.*
          target: test_1.input.model
        nodes:
        - name: train-model_1
          override: {}
          step: train-model
          type: execution
        - name: test_1
          override: {}
          step: test
          type: execution

..

If you want to run your pipeline from the CLI, you should first update your git repository.  

.. code-block::

    git add valohai.yaml
    git commit -m "Added pipeline definition"
    git push

..

Next, fetch the changes to the Valohai project and run the pipeline. If you know go to the UI, you should see the pipeline there under your project.

.. code-block::

    vh project fetch
    vh pipeline run mypipeline

..

.. note::

    Be careful that you are actually reading and updating the right ``valohai.yaml`` file when creating pipelines. If you get a message saying that the step is not found, check both the ``valohai.yaml`` and the project linked to your working directory.

..


.. seealso::

    * Tutorial: :ref:`quickstart-pipeline`
    * Topic guide: :ref:`valohai-utils`
..
