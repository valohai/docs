.. meta::
    :description: With live outputs, you don't need to wait your executions to finish to receive you results.

Live Outputs
============

Normally, executions will upload all files stored at ``/valohai/outputs`` **at the end** of the execution, even if the code crashes or is stopped. But in some long running model trainings, you might want to get checkpoints or other artifacts mid-execution. We call this **live outputs** or **live upload**.

When Valohai detects that a file under ``/valohai/outputs`` is marked as read-only, Valohai will remove that file from the directory and upload it right away. All programming languages and tooling have a way for marking files read-only e.g. ``os.chmod`` in Python or ``chmod`` command in Unix-like systems.

Here are some free-form examples:

.. code-block:: bash

    echo hello >> /valohai/outputs/greeting.txt
    sleep 3
    echo mello >> /valohai/outputs/greeting.txt
    # => Generates 1 file:
    #    - 'greeting.txt' containing 'hello mello'
    #    because it was not marked as read-only

    echo hello >> /valohai/outputs/greeting.txt
    chmod 0444 /valohai/outputs/greeting.txt
    sleep 3
    echo mello >> /valohai/outputs/greeting.txt
    # => Generates 2 files:
    #    - 'greeting.txt' containing 'hello'
    #    - 'greeting.txt' containing 'mello'

    echo hello >> /valohai/outputs/greeting.txt
    chmod 0444 /valohai/outputs/greeting.txt
    sleep 3
    echo mello >> /valohai/outputs/greeting.txt
    chmod 0444 /valohai/outputs/greeting.txt
    sleep 3
    echo bello >> /valohai/outputs/greeting.txt
    # => Generates 3 files:
    #    - 'greeting.txt' containing 'hello'
    #    - 'greeting.txt' containing 'mello'
    #    - 'greeting.txt' containing 'bello'

.. note::

    If the file permissions change commands are quick, they might not register before the code continues its progress. Because of this, we advice not to generate multiple live outputs with exactly the same name, even though it is technically possible.
