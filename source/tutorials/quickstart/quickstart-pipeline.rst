.. meta::
    :description: Create a Valohai training and deployment pipelines

.. _quickstart-pipeline:

Create a pipeline
#############################

.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`quickstart` series.
..

Pipelines automate your machine learning operations on Valohai ecosystem. A pipeline is a series of executions, Tasks and deployments.

.. admonition:: A short recap on pipelines
    :class: tip
    
    * A pipeline graphs consist of nodes and edges
    * You can launch pipelines manually, on a schedule or trigger them from your internal systems using the API
    * Read more about `pipelines </topic-guides/core-concept/pipelines>`_
  
..

.. admonition:: Prerequirements
    :class: attention

    * :ref:`repository` before using pipelines

..

Define your pipeline in YAML 
---------------------------------------------

We'll continue from the previous part of this tutorial series by creating a pipeline that trains a new model and then publishes it as an endpoint.

Add a new definition for pipeline:

.. list-table::
   :widths: 10 90
   :stub-columns: 1

   * - ``nodes``
     - A node can be type of a execution, task or a deployment. It's a "single step" in the pipeline.
   * - ``edges``
     - Edges define how does data flow from one node to another. For example *move all files that start with "model" from train-node outputs, to deployment-node as the model file for the digits endpoint*

Create **two nodes:**
    * ``train-node`` will execute our ``train-model`` step
    * ``deploy-node`` will deploy our ``digits`` endpoint on an existing deployment called ``mydeployment`` (created in the previous tutorial).

Create **one edge** to connect the nodes:
    * ``model.h5`` from ``train-node``'s outputs will be passed as a file to the ``deploy-node``'s ``digits`` endpoint as the file ``model`` (that's defined in the endpoint).

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 30,33,36,38,39,40

    - step:
      name: train-model
      image: tensorflow/tensorflow:2.4.1
      command:
        - pip install -r requirements.txt
        - python ./train.py {parameters}
      parameters:
        - name: epoch
          default: 5
          multiple-separator: ','
          optional: false
          type: integer
      inputs:
        - name: mnist
          default: s3://onboard-sample/tf-sample/mnist.npz
          optional: false

    - endpoint:
        name: digits
        description: predict digits from image inputs
        image: tiangolo/uvicorn-gunicorn-fastapi:python3.7
        server-command: uvicorn predict:app --host 0.0.0.0 --port 8000
        files:
            - name: model
              description: Model output file from TensorFlow
              path: model.h5

    - pipeline:
      name: Train and deploy
      nodes:
        - name: train-node
          type: execution
          step: train-model
        - name: deploy-node
          type: deployment
          deployment: mydeployment
          endpoints:
            - digits
      edges:
        - [train-node.output.model.h5, deploy-node.file.digits.model]

..

You can now push a new version of ``valohai.yaml`` to your code repository.

.. code-block:: bash

    git add valohai.yaml
    git commit -m "Added pipeline definition"
    git push

..

Launch a pipeline in Valohai
--------------------------------

* Login to `app.valohai.com <https://app.valohai.com>`_ 
* Open your project
* Click on the **Fetch repository** button to fetch a new commit
* Click on your project's **Pipelines** tab
* Click on the **Create pipeline** button
* Select the **blueprint** from the dropdown menu
* You can click on either of the nodes to change their default settings
* Click on **Create pipeline**

The pipeline will start execution the train-model step and once it's done start a new deployment. When the deployment goes to ``100% Available`` the pipeline will be marked as completed.

.. admonition:: Launch pipelines without YAML
    :class: tip

    You can also generate and launch a new pipeline directly with an API call, without having to define the YAML. The YAML definition is used only in the web app of Valohai, to visualize the pipeline and allow you to edit the default settings.

.. seealso::

    * `Core concepts: Pipelines </topic-guides/core-concepts/pipelines>`_
    * :ref:`pipeline-triggers`