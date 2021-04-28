.. meta::
    :description: What are Valohai pipelines? They allow you to standardize how your machine learning project is ran.

.. _pipeline-triggers:

Schedule pipelines
################################

Valohai triggers allow you to launch a copy of an existing pipeline on a time-based trigger. For example, running a pipeline weekly on Mondays at 09:00.

.. note::

    You can create a trigger after you've ran at least one succesfully completed pipeline.

..

1. Go to project settings
2. Navigate to the Triggers tab
3. Set your trigger title (e.g. *Weekly re-training*)
4. Select *Scheduled (Cron)* as the condition, as click *Add*
5. Open the condition and set the schedule you want. For example, Weekly on Mondays at 09:00
6. On the *Actions* column select *Copy Pipeline* and click *Add*
7. Open the action and select the *Source Pipeline* that you want to run
8. Click on *Create trigger*

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
