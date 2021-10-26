.. meta::
    :description: With live outputs, you don't need to wait your executions to finish to receive you results.

.. _live-outputs:

Live outputs
============

You use **live outputs** to upload files mid-execution.

Normally, executions will upload all files stored at ``/valohai/outputs`` **at the end** of the execution,
even if the code crashes or is stopped. But in some long running workloads, you might want to
save checkpoints or other artifacts mid-execution.

When Valohai detects that a file under ``/valohai/outputs`` is marked as read-only, Valohai will remove
that file from the directory and upload it right away. All programming languages and shells have a way
for marking files read-only e.g. ``os.chmod`` in Python.

A simple example:

.. code-block:: bash

    echo hello >> /valohai/outputs/greeting.txt
    chmod 0444 /valohai/outputs/greeting.txt
    sleep 30
    echo bye >> /valohai/outputs/farewell.txt
    # => Generates 2 files:
    #    - 'greeting.txt' with 'hello', uploaded right away
    #    - 'farewell.txt' with 'bye', uploaded after the execution finishes

.. note::

    If the file permissions change commands are quick, they might not register before the code continues its progress.
    Because of this, we advice not to generate multiple live outputs with exactly the same name.

    That can lead to some *funky* behaviour.
