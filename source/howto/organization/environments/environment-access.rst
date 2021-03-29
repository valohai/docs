.. meta::
    :description: Limit access to a certain environment type to only a certain team


Manage team quotas for environments
##################################################

Valohai allows you to set team quotas for each environment type. Using quotas you can also limit access to certain environments to only some teams inside your organization.

.. seealso::

    You'll need to :doc:`create teams inside your organization </howto/organization/user-management/teams>` before you can.

To manage the environment's team quotas:

* Login to `app.valohai.com <https://app.valohai.com>`_
* Click on **Hi, <username>!** on the top right corner
* Select **Manage <organization>**
* Open the Environments tab
* Click on the blue **Manage team quotas** button
* Select the environment and team from the drop-down menu
* Set a quota value (= how many machines can that team use in parallel)
* Click **Add**


.. tip::

    If you set the quota value to 0, the selected team won't be able to start any executions using that environment.