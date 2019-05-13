.. meta::
    :description: Use on-premises machine learning workers to keep your GPU utilization at 100%.

How to Use On-premises Workers
==============================

On-premises Valohai Enterprise installation includes local Valohai workers.

After on-premises worker setup and onboarding, there are four ways to use your local workers:

1. Set project default environment as the on-premises worker environment under ``Project > Settings > Basic Information > Default Environment``.
2. Set step default environment as ``environment: <ENVIRONMENT_SLUG>`` in ``valohai.yaml``.
3. Overwrite the environment on web interface with create execution environment dropdown.
4. Overwrite the environment by specifying ``vh exec run -e <ENVIRONMENT_SLUG>``.

If you are unsure what is the "slug" of your on-premises environment, you can run ``vh environments`` on your Valohai command-line client after login.

.. tip::

    When using on-premises workers, note that downloading and uploading files can be slow so I would advice not to use ``/valohai/inputs`` and ``/valohai/outputs`` except for small files.
