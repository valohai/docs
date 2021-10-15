
.. meta::
    :description: Get email notifications about the status of your executions, tasks, and pipelines

.. _howto-notifications-email:

Email notifications
####################

You can configure email notifications to receive notifications when your execution, task, pipeline, or deployment changes state.

For example, you could trigger an email from Valohai when:

* an execution completes or fails
* a task completes or fails
* a deployment completes or fails

.. warning::

    Valohai will trigger email notifications only for executions that longer than 1 minute.

Configure notifications
------------------------

Setup your webhooks under Project -> Settings.

1. Go to project settings
2. Navigate to the Notifications tab
3. Open **My Notifications**
4. Select the events you want to receive an email for notification for by clicking the checkbox under the email icon

.. tip::

    You can select to either receive notifications from all jobs in that project, or just the ones that you started.