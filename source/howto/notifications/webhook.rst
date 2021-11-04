
.. meta::
    :description: Use webhooks to trigger notifications and workflows

.. _howto-notifications-webhooks:

Webhooks
##########

Webhooks allow you to automatically trigger messages from Valohai to your application when an Valohai executions state changes.

For example, you could trigger a message from Valohai when:

* an execution completes or fails
* a task completes or fails
* a deployment completes or fails

In your application you could then receive this message from Valohai to for example post an update on a Slack channel, send an email, or start another internal process.


Setup a Slack webhook
-----------------------

`Slack documentation to setup a new webhook <https://api.slack.com/messaging/webhooks>`_. You'll just need to complete the first 3 steps.

Copy the generated Webhook URL from the *Webhook URLs for Your Workspace* page.

Now go to Valohai and open your project's settings.

1. Navigate to the Notifications tab
2. Open Channels
3. Click on **Create a new channel**, change the type to Slack, and add your webhook details
4. Open Project Notifications
5. Click on **Create new notification routing** 
6. Choose your event and channel
7. Save the routing


Setup a custom webhook
-----------------------

.. tip:: 

    You can also use tools like `IFTTT <https://ifttt.com/home>`_ and `Zapier <https://zapier.com/>`_ to automate your workflows with webhooks.


Setup your webhooks under Project -> Settings.

1. Go to project settings
2. Navigate to the Notifications tab
3. Open Channels
4. Click on **Create a new channel** and add your webhook details
5. Open Project Notifications
6. Click on **Create new notification routing** 
7. Choose your event and channel
8. Save the routing

.. video:: /_static/videos/webhooks-setup.mp4
    :autoplay:
    :width: 600

Example of webhook message
--------------------------------

Below an example of a message your application would receive for a completed Valohai execution.

.. code-block:: json

    {
        "project": "016f3203-4a8c-969e-078c-52ab66947746",
        "title": "Execution finished: demo/cool-tensorflow/#736 (completed)",
        "type": "execution_completed",
        "body": "Execution [demo/cool-tensorflow/#736](https://app.demo.com/p/valohai/cool-tensorflow/execution/0178f482-8686-fb28-8af1-3d36af38079d/) (by demouser)\nfinished with duration 11:01.",
        "url": "/p/demo/cool-tensorflow/execution/0178f482-8686-fb28-8af1-3d36af38079d/",
        "data": {
        "valohai.execution-counter": 736,
        "valohai.execution-ctime": "2021-04-21T12:58:18.119973+00:00",
        "valohai.execution-duration": 660.0186445713043,
        "valohai.execution-id": "0178f482-8686-fb28-8af1-3d36af38079d",
        "valohai.execution-qtime": "2021-04-21T12:58:18.201116+00:00",
        "valohai.execution-status": "complete",
        "valohai.execution-step": "Train model (MNIST)",
        "valohai.execution-title": null,
        "valohai.project-id": "016f3203-4a8c-969e-078c-52ab66947746",
        "valohai.project-name": "demo/cool-tensorflow",
        "valohai.creator-id": 3323,
        "valohai.creator-name": "demouser",
        "valohai.commit-identifier": "4d34124453b680daa0ecb881bcf1bd735a3bf99d"
        }
    }

..