``step.command``
~~~~~~~~~~~

The ``command`` section defines one or more commands that are run during execution.

For example, the following configuration file defines two steps:

* **hardware-check**: executes ``nvidia-smi`` to check the status of server GPU using ``tensorflow/tensorflow:0.12.1-devel-gpu`` Docker image
* **environment-check**: executes ``printenv`` followed by ``python --version`` to check how the runtime environment looks like inside ``python:3.6`` Docker image

.. code-block:: yaml

    - step:
        name: hardware-check
        image: tensorflow/tensorflow:0.12.1-devel-gpu
        command: nvidia-smi

    - step:
        name: environment-check
        image: python:3.6
        command:
          - printenv
          - python --version

.. tip::

   The platform will mark execution as crashed if *the last* command returns an error code other than 0.
