.. meta::
    :description: What are Valohai pipelines? They allow you to standardize how your machine learning project is ran.

Pipelines
##########

.. seealso::

    For the technical specifications, go to :doc:`valohai.yaml pipeline section </reference-guides/valohai-yaml/pipeline/index>`.

.. _pipeline:

**Pipeline** is a version controlled collection of executions some of which rely on the results of the previous
executions thus creating a directed graph. These pipeline graphs consist of nodes and edges and we'll discuss
these further down.

For example, consider the following sequence of data science operations:

1. **Preprocess** dataset on a memory-optimized machine
2. **Train** multiple machine learning models on GPU machines using the preprocessed data
3. **Evaluate** all of the trained models
4. **Find-best-model** compare the models to find the best model
5. **Deploy** a new version of your trained model for online inference

Our pipeline would have 4 or more **nodes**; at least one for each :doc:`step </topic-guides/core-concepts/steps>` mentioned above and one for the deployment.

In the example below we'll train 3 different models in parallel and compare them to find the best performing model that we can deploy to an HTTP endpoint. 
It is worth noting that when evaluating multiple trained models inside a pipeline, **the comparison for choosing the best model is not done automatically**. It's up to you to define the comparison according to your models criteria and run the comparison in its own node (find-best-model node in the figure below). 


.. image:: /topic-guides/core-concepts/pipelines.png
   :alt: You configure data stores per project-basis on Valohai.
..

You can manage pipelines under the ``Pipelines`` tab on the web user interface if the feature has been enabled for your account. Your project will need to connected to a Git repository and have a pipelines section defined in your ``valohai.yaml``.

**Nodes** of the pipeline (the circles that receive something and/or produce something):

* Nodes can be either :doc:`executions </topic-guides/core-concepts/executions>` or :doc:`deployments </topic-guides/core-concepts/deployments>`.
* It is also possible to run Tasks inside pipelines :doc:`by converting an execution node into a task node </howto/pipelines/tasks/>`.
* Each node will start automatically when all of the requirements have been met.
* Each node has a list of "edges" (explained below).

**Edges** of the pipeline (the lines between nodes) are either:

* :doc:`output </topic-guides/executions/outputs/index>` files used as an input of an upcoming execution or deployment.
* :doc:`input </topic-guides/executions/inputs/index>` files, to allow for copying inputs from one node to another and ensure multiple pipeline nodes use the same inputs.
* :doc:`parameters  </topic-guides/core-concepts/parameters>` that are passed from one node to another.
* :doc:`metadata </howto/new-user-guide/code/metadata>` that is passed from the node where it was created to a parameter in the next node.

.. seealso::

    * :ref:`quickstart-pipeline`
    * :ref:`pipeline-triggers`
    
