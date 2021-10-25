.. meta::
    :description: If you wish to parse runtime configuration from files instead of command-line parameters, use /valohai/config.

Variable-based configuration
============================

You can configure your executions by using **standard environment variables**.

We record and highlight what environmental variables were used if you define them through the web UI,
command-line client parameters or :doc:`/reference-guides/valohai-yaml/step-environment-variables` definitions.

By default, Valohai defines the following environment variables:

.. code-block:: bash

    # info about the execution itself
    VH_CONFIG_DIR=/valohai/config
    # downloaded files will be saved here
    VH_INPUTS_DIR=/valohai/inputs
    # save files to be uploaded here
    VH_OUTPUTS_DIR=/valohai/outputs
    # your git repository code,  also the working directory
    VH_REPOSITORY_DIR=/valohai/repository
    # the following will change between each execution; it includes the execution UUID
    VH_JOB_ID=exec-016eb6ec-50cb-0031-3f48-d556e47b1c78
    # the execution ID
    VH_EXECUTION_ID=016eb6ec-50cb-0031-3f48-d556e47b1c78
    # the project ID
    VH_PROJECT_ID=04a37c09-dbe1-4c01-b715-0a3223c50188
    # the task ID (if any)
    VH_TASK_ID=f9c97759-513e-44a1-9666-97cf198cde80
    # the pipeline ID (if any)
    VH_PIPELINE_ID=f403603b-ad11-4cc4-a90d-3118f51c8dcd
    # the pipeline node ID (if any)
    VH_PIPELINE_NODE_ID=972834e2-23b5-429a-9f6d-80b8c4a75c8a


.. tip::

    In your code, you can check if any of the above variables exists to know if you are running on Valohai.


Special environment variables
-----------------------------

``VH_TPU``
  For private environments where Google Cloud TPU is enabled, this environment variable will contain the GRPC endpoint(s)
  of the allocated Cloud TPU(s), separated by spaces.  This may be passed in as the argument for ``TPUClusterResolver``,
  e.g. ``TPUClusterResolver(tpu=os.environ["VH_TPU"].split()).get_master()`` or similar.
  When TPUs are not enabled, this variable will not be set.
