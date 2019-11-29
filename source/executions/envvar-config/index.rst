.. meta::
    :description: If you wish to parse runtime configuration from files instead of command-line parameters, use /valohai/config.

Variable-based Configuration
============================

You can configure your executions by using **standard environment variables**.

We record and highlight what environmental variables were used if you define them through the web UI,
command-line client parameters or :doc:`/valohai-yaml/step-environment-variables` definitions.

By default, Valohai defines the following environment variables:

.. code-block:: bash

    VH_CONFIG_DIR=/valohai/config           # info about the execution itself
    VH_INPUTS_DIR=/valohai/inputs           # downloaded files will be saved
    VH_OUTPUTS_DIR=/valohai/outputs         # save files to be uploaded
    VH_REPOSITORY_DIR=/valohai/repository   # your git repository code,
                                            # also the working directory

    # the following will change between each execution
    # it includes the execution UUID
    VH_JOB_ID=exec-016eb6ec-50cb-0031-3f48-d556e47b1c78

.. tip::

    In your code, you can check if ``VH_JOB_ID`` exists to know if you are running on Valohai.

