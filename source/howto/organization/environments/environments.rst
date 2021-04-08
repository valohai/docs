.. meta::
    :description: Manage available environments in your organization 


Configure environments and scaling rules 
##################################################

.. seealso::

    Read more about :doc:`executions and environments </topic-guides/core-concepts/executions/>`

Organization administrators can edit their environment settings, manage which teams have access to which environments and setup scaling rules.

To manage your organization settings:

* Login to `app.valohai.com <https://app.valohai.com>`_
* Click on **Hi, <username>!** on the top right corner
* Select **Manage <organization>**
* Open the Environments tab

The available settings for each environment are:

.. list-table::
    :widths: 30 70
    :header-rows: 0
    :stub-columns: 1

    * - Enabled
      - Determines if users can use this environment for their executions.
    * - Allow personal usage
      - Determines if users can use this environment in projects that are not owned by the organization.
    * - Scale-Down Grace Period
      - How many minutes should Valohai wait after the last completed execution before scaling down them machine. The default value is 15 minutes, so machines are not scaled immediately after the execution ends. Allowing you to quickly start a new execution, without having to wait for the machine to spin up for each execution (and download the Docker image and inputs).
    * - Min. Scale
      - What's the minimum number of machines that Valohai should keep running? By default, this is set to 0.
    * - Max. Scale
      - What's the maximum number of machines that Valohai can launch in parallel? By default, this is set to 5. After a maximum number of machines has been launched, new executions will get queued and executed once a machine frees up from a previous execution. Your max scale might be limited by the quota you have available from your cloud provider. 
    * - Per-User Quota 
      - How many machines can one user run in parallel? The default value is 0 (no limit).

..

.. admonition:: Caching
    :class: tip

    Valohai caches downloaded inputs and Docker images on the machine.
