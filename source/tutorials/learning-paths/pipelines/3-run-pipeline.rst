.. meta::
    :description: Valohai Pipelines learning path - Creating your first pipeline in Valohai

Running a pipeline
####################

.. include:: _intro-pl.rst

In this section you will:

- Run pipelines from the command line.
- Run pipelines in the Valohai UI.
- Reuse pipeline nodes.


Run an ``--adhoc`` pipeline from the command line
--------------------------------------------------

Before running your pipeline, make sure to login to Valohai and connect the working directory to a Valohai project. 

.. code-block:: bash

    vh login
    vh project status

    # Link to and existing project
    vh project link

    # Create a new project
    vh project create

..

Next, you can start your pipeline by running the following command.  

.. code-block:: bash

    vh pipeline run preprocess-and-train --adhoc

..

If you now go to the Valohai UI you can see the whole pipeline under the Pipeline tab and the related executions under the Executions tab. 


Run a pipeline after pushing to Git
------------------------------------

If you have connected your project to a Git repository, you can also run the pipeline defined in your latest commit from the command line. 

Start by pushing the sample code, ``valohai.yaml`` and the ``requirements.txt`` to your code repository.

.. code-block:: bash

    git add preprocess_dataset.py train_model.py valohai.yaml requirement.txt
    git commit -m "Add pipeline definition"
    git push

..

Before running the code, you will need to fetch the code to Valohai. You can do it either from the command line or by pushing the button in the UI.

.. code-block:: bash

    vh project fetch
    vh pipeline run preprocess-and-train

..

Run a pipeline in the Valohai UI
---------------------------------

Before the proceeding with the next steps, make sure you have pushed the latest version of ``valohai.yaml`` to your code repository. 

.. code-block:: bash

    git add preprocess_dataset.py train_model.py valohai.yaml requirement.txt
    git commit -m "Add pipeline definition"
    git push

..

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

