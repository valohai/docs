.. meta::
    :description: Valohai Pipelines learning path - Creating your first pipeline in Valohai

Advanced pipeline features
############################

.. include:: _intro-pl.rst

In this section you will
 * Learn how to create pipelines with multiple nodes
 * Learn how to use pipeline conditions
 * Learn how to set pipeline triggers


Pipeline with multiple nodes
----------------------------

For an example with multiple nodes, please see our :ref:`example-projects-quick-start-tensorflow`. 

* It is worth noting that when evaluating multiple trained models inside a pipeline, **the comparison for choosing the best model is not done automatically**. 
* The user needs to define the comparison programatically in a separate node and then output the results to the possible next node (see the ``yaml`` file and ``compare.py`` in the example project).


Pipeline conditions
-------------------

In some cases you might want to terminate the pipeline if for example a metadata value exceeds some set limit. This can be done by using a pipeline property called ``actions``.
The structure for ``actions`` is: ``when`` something happens, check ``if`` the condition is true, and if yes, ``then`` stop the pipeline.

The possible options for ``when`` are:

* ``node-starting``
* ``node-complete``
* ``node-error``

The ``if`` condition can be based either on metadata or a parameter. 

Currently, the availables option for ``then`` are:

* ``stop-pipeline`` to stop the complete pipeline.
* ``require-approval`` to pause the pipeline until a user goes to manually approve the previous results of the pipeline.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 7,8,9,10,14,15,16

    - pipeline:
        name: Action pipeline
        nodes:
          - name: train-model
            type: execution
            step: Train model
            actions:
              - when: node-complete
                if: metadata.foo >= 0.8
                then: stop-pipeline
          - name: test-model
            type: execution
            step: Test model
            actions:
              - when: node-starting
                then: require-approval
        edges:
          - [train-model.output.model*, test-model.input.model]

..


Pipeline triggers
-------------------

Valohai triggers allow you to launch a copy of an existing pipeline on a time-based trigger. For example, running a pipeline weekly on Mondays at 09:00.

* Go to project settings
* Navigate to the Triggers tab
* Set your trigger title (e.g. Daily retraining, every 4 hours)
* Select Scheduled (Cron) as the condition, as click Add
* Open the condition and set the schedule you want.
   * You can either use one of the options or select Custom
   * For example a custom value: 0 0/4 * * 1-7 would run the pipeline every 4 hours on every day of the week.
* On the Actions column select the right action and click Add
   * Copy Pipeline reruns always the same pipeline version
      * Select the Source Pipeline that you want to run
   * Run Pipeline runs a pipeline with whatever is the newest version fetched to Valohai
   * Source Commit Reference, could be for example main to always run with the latest pipeline from your main branch
   * Pipeline Name is the name of the pipeline in your valohai.yaml
   * Pipeline Title is the title used in the UI and API results
* Click on Create trigger

.. warning::

    Note that all times are expressed in UTC time.

..

.. image:: /_images/pipeline-trigger.png
    :alt: Create a pipeline trigger

..

.. admonition:: Name your pipelines
    :class: tip

    Open the Pipelines tab and name your pipeline by editing the pipeline title. This will make it easier to find the right pipeline when setting up the triggers.

..