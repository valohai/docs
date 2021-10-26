.. meta::
    :description: Use on-premises machine learning workers to keep your GPU utilization at 100%.

Using on-premises workers
=========================

On-premises Valohai Enterprise installation includes local Valohai workers.

After on-premises worker setup and onboarding, there are four ways to use your local workers:

1. Set project default at ``Project > Settings > General > Default Environment``.
2. Set step default environment with ``environment: <ENVIRONMENT_SLUG>`` in the YAML.
3. Overwrite the environment on web interface with create execution environment dropdown.
4. Overwrite the environment by specifying ``vh exec run -e <ENVIRONMENT_SLUG>``.

If you are unsure what is the "slug" of your on-premises environment, you can run ``vh environments`` on your Valohai command-line client after login.
