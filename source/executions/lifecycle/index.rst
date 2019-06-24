.. meta::
    :description: Runtime lifecycle starts from an execution being created and end when the commands haven been ran.

Lifecycle
=========

An execution can be in one of six states:

* **created**: The execution is not yet queued, most likely because you don't have enough quota and the system is waiting for one of your older executions to finish.
* **queued**: The execution is queued as there are no free servers which means that either a new server is being launched or you'll have to wait for another execution (either your own or someone else's) to finish, depending on the installation.
* **started**: The execution is currently running on an instance. You should see real-time details through the web interface, command-line client and API.
* **error**: The last of the execution commands failed; check the logs for more information.
* **stopping**: An user manually cancelled the execution through the web interface, command-line client or API.
* **stopped**: The execution has been successfully stopped by the platform.
* **complete**: The execution was ran successfully and its results are available through the web interface and command-line client.

Each execution will always start as **created** and will end up either **error**, **stopped** or **complete**.

An execution will only run user-defined code in the **started** state.
