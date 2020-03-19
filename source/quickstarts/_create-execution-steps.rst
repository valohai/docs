1. Go to the **Executions** tab inside your project
2. Press the **Create execution** button
3. The ``Step`` field lists all available types of executions. Make sure |example-step-name| is selected.
4. You don't need to worry about the rest of the configuration for now.
   The default inputs and parameters of the form are loaded from the ``valohai.yaml`` configuration file
   and should be good for this example execution.
5. Press **Submit** to start the execution.

.. tip::

    Valohai command-line client allows creating one-off executions from local files.
    See :doc:`quick-start-cli` for more details.

    .. code-block:: bash

        $ vh exec run --adhoc --watch name-of-your-step
        # sends local source code to a worker and runs commands in valohai.yaml
