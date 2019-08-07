.. meta::
    :description: What are Valohai pipelines? They allow you to standardize how your machine learning project is ran.

Pipelines
=========

.. note::

    **Valohai pipelines are in private beta.**
    Send an email to info@valohai.com for details.

.. seealso::

    For technical specifications, go to :doc:`valohai.yaml pipeline section </valohai-yaml/pipeline/index>`.

**Pipeline** is a version controlled collection of executions some of which rely on the results of the previous
executions thus creating a directed graph. These pipeline graphs consist of nodes and edges and we'll discuss
these further down.

For example, consider the following sequence of data science operations:

1. **preprocess** dataset on a memory-optimized machine
2. **train** multiple machine learning models on GPU machines using the preprocessed data (1)
3. **evaluate** all of the trained models (2) to find the best one

We could say that you have 3 separate operations or :doc:`steps </core-concepts/steps>`:
**preprocess**, **train**, **evaluate**.

This pipeline would have 3 or more **nodes**; at least one for each step mentioned above.
Training could have additional nodes if you are training in parallel but lets keep it simple:

.. thumbnail:: pipelines.png
   :alt: You configure data stores per project-basis on Valohai.

**Nodes** of the pipeline (the circles that receive something and/or produce something):

* Each node has a list of requirements ("edges", explained further below).
* Each node will start automatically when all of the requirements have been met.
* Nodes are currently exclusively Valohai :doc:`executions </core-concepts/executions>`.
* More nodes types are being planned e.g. deployment and integrations with other services.

**Edges** of the pipeline (the lines between nodes) can be:

* :doc:`output </executions/outputs/index>` files used as an input of an upcoming execution
* :doc:`metadata </executions/metadata/index>` used as a parameter of an upcoming execution *(in development)*
* copying a parameter of an previous execution to an upcoming execution *(in development)*

You can manage pipelines under the ``Pipelines`` tab on the web user interface if the feature
has been enabled for your account and you have a pipeline defined in your ``valohai.yaml``.

Full documentation how to define pipelines can be found under :doc:`valohai.yaml pipeline </valohai-yaml/pipeline/index>`
section, but here is a brief overview what the above example pipeline could look like:

.. code-block:: yaml

    # define "preprocess", "train" and "evaluate" steps in the YAML...
    - pipeline:
        name: example-pipeline
        nodes:
          - name: preprocess-node
            type: execution
            step: preprocess
          - name: train-node
            type: execution
            step: train
          - name: evaluate-node
            type: execution
            step: evaluate
        edges:
          - [preprocess-node.output.*x-images*, train-node.input.x-images]
          - [preprocess-node.output.*x-labels*, train-node.input.x-labels]
          - [preprocess-node.output.*y-images*, train-node.input.y-images]
          - [preprocess-node.output.*y-labels*, train-node.input.y-labels]
          - [train-node.output.model.pb, evaluate-node.input.model.pb]
