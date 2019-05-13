``step.environment``
~~~~~~~~~~~~~~~~~~~~

Environment defines the hardware and the location where to run your code.

Environments encapsulate the following information:

* Who owns the environment instances?
* Are you running on Azure, Amazon, Google, OpenStack or on-premises?
* Are you running in USA, Asia, Europe, etc.
* How much memory and CPU is available?
* Does it have GPUs?

Environment defined in the YAML is the default value for executions of that particular step type. In other words, it can overwritten by selecting a separate environment in the web interface dropdown or with ``vh exec run -e <SLUG> <STEP_NAME>`` command-line parameter.

You can use ``vh environments`` command to see available environments after logging in.

The most common environment slug syntax is ``<OWNER_IF_NOT_VALOHAI>-<CLOUD_PROVIDER>-<LOCATION>-<HARDWARE_TYPE>``. For example:

* ``environment: aws-eu-west-1-g3s-xlarge``
* ``environment: acme-azure-westeurope-nc24``
* ``environment: awesome-corporation-gcp-europe-west4-b-custom-2-8192``

.. tip::

   It is wise to use an environment in the same data center or geographical location as your data store to minimize the data transfer durations.
