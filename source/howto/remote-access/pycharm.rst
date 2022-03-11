
.. meta::
    :description: How to attach a remote debugger from PyCharm to a Valohai execution

.. _remote-ssh-pycharm:

Debug from PyCharm
##################

.. warning::

    This guide assumes you're already familiar with the fundamentals of Valohai and are working with a project that's connected to a Git repository, and configured on Valohai.

.. warning::

    Remote debugging is only available in PyCharm Professional.

In this guide we'll look at attaching the PyCharm remote debugger to a Valohai execution.

.. raw:: html

    <div style="position: relative; padding-bottom: 52.17391304347826%; height: 0;"><iframe src="https://www.loom.com/embed/4b09a54ca5094138814b15526755fc14" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

1. Sample Code
---------------

For this example we'll use the following simple example code:

.. code-block:: python

    import numpy as np
    import time

    for x in range(1,20) :
        print(f"Doing computation {x}")
        data = np.random.random((50,50))
        sum = np.sum(data)
        time.sleep(2)

And the corresponding ``valohai.yaml`` file:

.. code-block:: yaml

    - step:
      name: train
      image: python:3.9
      command: 
        - pip install numpy
        - python train.py


1. Create a new Debug Configuration in PyCharm
-----------------------------------------------

Create a new Python Debug Server in PyCharm. The IDE host name should be ``localhost`` and the port should be the port that you want to have listening to incoming debug connections on your local machine (here 1234).

.. image:: /_images/ssh_remote_debug_pycharm_conf1.png
    :alt: Create a new Python Debug Server in PyCharm

.. image:: /_images/ssh_remote_debug_pycharm_conf2.png
    :alt: Create a new Python Debug Server in PyCharm


You can also now start the created Debug Server and leave it to wait for the process connection. 

2. Use ``pydevd_pycharm``
-------------------------

Import ``pydevd_pycharm`` and set it to wait for connection with the debugger. 

.. code-block:: python
    :emphasize-lines: 1,6-15

    import pydevd_pycharm
    import numpy as np
    import time

    # The script is halted here, until a debugger is attached
    connected = False
    while not connected:
        try:
            # The arbitrary container port 1234 on the worker machine is set to connect with the debugger.
            # Note that this is not the same port you specified during step 1 as that is on your local machine. 
            pydevd_pycharm.settrace('localhost', port=1234, stdoutToServer=True, stderrToServer=True)
            connected = True
        except Exception:
            print("Waiting for connection...")
            time.sleep(10)


    for x in range(1,20) :
        print(f"Doing computation {x}")
        data = np.random.random((50,50))
        sum = np.sum(data)
        time.sleep(2)

Now update the ``valohai.yaml`` file to install ``pydevd_pycharm`` in your Valohai execution. You can copy the correct PyCharm version for example from the Run Configuration section.

.. code-block:: yaml
    :emphasize-lines: 5

    - step:
      name: train
      image: python:3.9
      command: 
        - pip install numpy pydevd_pycharm~=<PYCHARM-VERSION>
        - python train.py

Commit your changes and push them to your Git repository.

Then launch a new Valohai execution with SSH debugging enabled. Follow the :ref:`remote-ssh` how-to guide for detailed instructions.

.. note:: 

    You don't need to worry about the ``ConnectionRefusedError: [Errno 111] Connection refused`` in the logs, that will be fixed in the last step. 


3. Connect from PyCharm to a remote execution
-----------------------------------------------

Since ``pydevd_pycharm`` does not have a listen mode, you will need to establish a reverse SSH tunnel between your local machine and Valohai worker instance. 
You'll get the IP of the worker machine from the Valohai execution logs.

.. code-block:: bash

    ssh -i <PATH-TO-YOUR-PRIVATE-SSH-KEY> <IP-FROM-VALOHAI> -p 2222 -R 1234:localhost:1234 -t /bin/bash

You might see a prompt saying that the filepath on the worker machine cannot be found in project. 
This happens because the path mapping was not defined when creating the debugging configuration. You can just click on the "Auto detect" to set the mapping. 

.. image:: /_images/ssh_remote_debug_pycharm_path.png
    :alt: Choose Auto detect for the path mapping

Finally, you should see a message in the Debugger console saying that the connection was established. 

.. note:: 

    If you created the SSH connection without reverse port forwarding, you don't need to interrupt the connection in order to adjust the parameters from SSH's internal shell:

    * Type ``~C`` to access the ``ssh>`` shell.
    * Type ``-R 1234:localhost:1234`` in the ``ssh>`` shell. 



The debugger will wait for you to tell it to continue with the execution by clicking on the green arrow. When you hit a breakpoint, you'll also be able to see your local variables, and edit them on the fly.

