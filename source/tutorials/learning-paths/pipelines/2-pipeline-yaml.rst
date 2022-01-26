.. meta::
    :description: Valohai Pipelines learning path - Creating your first pipeline in Valohai

Defining a pipeline in the ``valohai.yaml``
#############################################

.. include:: _intro-pl.rst

.. raw:: html

    <div style="position: relative; padding-bottom: 36.32718524458701%; margin-bottom: 20%; height: 0;"><iframe src="https://www.loom.com/embed/f31aac6122f74f859e7b2a285d220d66" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 150%;"></iframe></div>

In this section you will:

- Add a simple pipeline to your ``valohai.yaml``.
- Learn how to use different types of edges (optional).


Add a pipeline to ``valohai.yaml``
-----------------------------------

Open the ``valohai.yaml`` file that is at the root of your project and add the following ``pipeline`` in it. 

.. code-block:: yaml
    :linenos:

    - pipeline:
        name: preprocess-and-train
        nodes:
        - name: preprocess
          type: execution
          step: preprocess-dataset
        - name: train
          type: execution
          step: train-model
        edges:
        - [preprocess.output.preprocessed_mnist.npz, train.input.dataset]

This pipeline will

Create **two nodes:**
    * ``preprocess`` will execute your ``preprocess-dataset`` step.
    * ``train`` will execute your ``train-model`` step.


Create **one edge** to connect the nodes:
    * ``preprocessed_mnist.npz`` from ``preprocess-dataset``'s outputs will be passed into the input called ``dataset`` in the ``train`` node.


.. image:: /_images/pipeline-nodes-edges.png
    :alt: Pipelines consist of nodes connected by edges.


You can now continue to the next part of the learning path. Optionally, you can keep reading to learn more about the different edge types.


Pipeline edges
----------------
The simplest syntax to define edges is ``[<SOURCE>, <TARGET>]``

Both **<SOURCE>** and **<TARGET>** have 3 properties separated by dots: ``node``, ``type`` and ``key``.
Thus the shorthand syntax becomes:
``[<NODE>.<TYPE>.<KEY>, <NODE>.<TYPE>.<KEY>]``


The available edge ``types`` are:
 * outputs (only source node)
 * inputs (only target node)
 * parameters
 * metadata (only source node)
 * files (only for deployment nodes)

In the example above you already saw how to pipe output from the source node into a target node input.
Here are examples for using the other types of edges. 

.. code-block:: yaml
    :linenos:

    edges:
        # Parameter-parameter edge
        # Note that the parameters have to exist in the yaml for both source and target
        - [sourcenode.parameter.parameterkey, targetnode.parameter.parameterkey]

        # Metadata-parameter edge
        # Note that you can only pass single values and not for example list type metadata
        - [sourcenode.metadata.metadatakey, targetnode.parameter.parameterkey]

        # Output-file edge
        # The file type is only available for deployment nodes. 
        # Note that the filename is the name defined in the YAML.
        - [sourcenode.output.outputkey, targetnode.file.endpointname.filename]


