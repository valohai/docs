.. meta::
    :description: Valohai Pipelines learning path - Creating your first pipeline in Valohai

Running a pipeline
####################

.. include:: _intro-pl.rst

In this section you will:

- Run a pipeline in Valohai.
- Reuse pipeline nodes.
- Learn how to run a pipeline from the command line.

Run a pipeline in Valohai
----------------------------

Before the proceeding with the next steps, make sure you have pushed the latest version of ``valohai.yaml`` to your code repository.

* Login to `app.valohai.com <https://app.valohai.com>`_
* Open your project
* Click on the **Fetch repository** button to fetch a new commit
* Click on your project's **Pipelines** tab
* Click on the **Create Pipeline** button
* Select the **branch**, **commit** and **blueprint** from the dropdown menus
* Click on the **Create Pipeline from Template** button
* You can click on either of the nodes to change their default settings
* Click on the **Create pipeline** button

.. image:: /_images/create-pipeline-template.png
    :alt: Creating pipeline from a template.

The pipeline will start executing the ``preprocess-dataset`` step and once it's done, move on to the ``train-model`` step. When the training step is finished, the pipeline will be marked as Completed. 

Reuse pipeline nodes
---------------------

Sometimes you might want to run only some of the pipeline nodes and reuse the results from a previous pipeline run. 
For example, for the sample pipeline in this tutorial, might want to change a parameter value for the training. You don't need to run the preprocessing again but you can reuse that node from an earlier run.

* Start by creating a new pipeline by clicking on the **Create pipeline** button
* Select the **branch**, **commit** and **blueprint** from the dropdown menus
* Click on the **Reuse nodes...** button
* Select the source pipeline
* Select the node(s) to reuse 
* Click on the **Apply** button
* You can change the default settings for the non-reused nodes by clicking on them.
* Click on the **Create pipeline** button

.. image:: /_images/reuse-nodes.png
    :alt: Reusing nodes in pipelines.

Run a pipeline from the command line
--------------------------------------

After pushing to Git, you can run the latest version of the pipeline also from the CLI.

.. code-block:: bash

    vh project fetch
    vh pipeline run preprocess-and-train

..

If you want to run a the latest version of the pipeline without pushing to Git, you can add the ``--adhoc`` flag to the previous command.
Similarly to single executions, this allows you to also use local file as they will be uploaded to the worker instance.

.. code-block:: bash

    vh pipeline run preprocess-and-train --adhoc

..