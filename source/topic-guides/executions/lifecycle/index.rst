.. meta::
    :description: Execution lifecycle starts from an execution being created and end when the commands haven been ran.

Creating Executions
===================

Executions implement a step that's defined in ``valohai.yaml``. You can define your :ref:`step` by writing the :ref:`yaml-step` manually, or using valohai-utils.

Executions can be created from the web app, command-line or API call.

.. thumbnail:: /_images/execution-form.jpg
   :alt: Step form to create an execution.

.. role:: created
.. role:: queued
.. role:: started
.. role:: stopping
.. role:: stopped
.. role:: error
.. role:: complete

An execution can be in one of six color-coded states:

* :created:`created`:
  The execution is not yet queued, most likely because you don't have enough quota and the system
  is waiting for one of your older executions to finish.
* :queued:`queued`:
  The execution is queued as there are no free servers which means that either a new server is being
  launched or you'll have to wait for another execution (either your own or someone else's) to finish,
  depending on the installation.
* :started:`started`:
  The execution is currently running on an instance.
  You should see real-time details through the web interface, command-line client and API.
* :stopping:`stopping`:
  An user manually cancelled the execution through the web interface, command-line client or API.
* :stopped:`stopped`:
  The execution has been successfully stopped by the platform.
* :error:`error`:
  The last of the execution commands failed; check the logs for more information.
* :complete:`complete`:
  The execution was ran successfully and its results are available through the web interface and command-line client.

Each execution will always start as :created:`created` and will end
up either :stopped:`stopped`, :error:`error` or :complete:`complete`.

An execution will only run user-defined code in the :started:`started` state.
