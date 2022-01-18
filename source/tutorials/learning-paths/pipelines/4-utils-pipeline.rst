.. meta::
    :description: Valohai Pipelines learning path - Creating your first pipeline in Valohai

Creating a pipeline with ``valohai-utils``
############################################

.. include:: _intro-pl.rst

In this section you will
 * Learn how to use ``valohai-utils`` helper library to build and update pipelines in ``valohai.yaml``.

Previously, you defined the pipeline manually in your ``valohai.yaml``. Alternatively, you can define pipelines using the :ref:`valohai-utils` helper library.
Start by creating a new file with the following code in it. 

.. note::

    When creating the ``valohai.yaml`` and updating the step information with ``vh yaml step <filename>`` the code in the file is only parsed and not executed. For ``vh yaml pipeline <filename>`` the ``main`` method defined below is actually run.
    This means that you should have all the libraries that will be imported installed. Thus, it might make more sense to have the pipeline code in a separate file.  

..

.. code-block:: python

    from valohai import Pipeline
    
    def main(config) -> Pipeline:
        
        #Create a pipeline called "utilspipeline".
        pipe = Pipeline(name="utilspipeline", config=config)
        
        # Define the pipeline nodes.
        preprocess = pipe.execution("preprocess-dataset")
        train = pipe.execution("train-model")
        
        # Configure the pipeline, i.e. define the edges.
        preprocess.output("preprocessed_mnist.npz").to(train.input("dataset"))
        
        return pipe
..

Next, run the command:

.. code-block::

    vh yaml pipeline <filename>
..

If you now check your ``valohai.yaml``, you should now have a new pipeline called ``utilspipeline``. Even though otherwise exactly alike, the edges look different for the two pipelines.
When creating the pipeline manually, you used the `shorthand syntax </reference-guides/valohai-yaml/pipeline/edges/#edge-shorthand-syntax>`_ but ``valohai-utils`` doesn't. Regardless, the pipeline will be built in a similar manner in the UI. 

.. code-block:: YAML

    - pipeline:
        name: utilspipeline
        edges:
        - configuration: {}
          source: preprocess-dataset_1.output.preprocessed_mnist.npz
          target: train-model_1.input.dataset
        nodes:
        - name: preprocess-dataset_1
          actions: []
          override: {}
          step: preprocess-dataset
          type: execution
        - name: train-model_1
          actions: []
          override: {}
          step: train-model
          type: execution

..

If you want to run your pipeline from the CLI, you should first update your git repository.  

.. code-block::

    git add valohai.yaml
    git commit -m "Added pipeline definition"
    git push

..

Next, fetch the changes to the Valohai project and run the pipeline. If you now go to the UI, you should see the pipeline there under your project.

.. code-block::

    vh project fetch
    vh pipeline run mypipeline

..

.. note::

    Be careful that you are actually reading and updating the right ``valohai.yaml`` file when creating pipelines. If you get a message saying that the step is not found, check both the ``valohai.yaml`` and the project linked to your working directory.

..

