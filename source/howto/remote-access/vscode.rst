
.. meta::
    :description: How to attach a remote debugger from VSCode to a Valohai execution

.. _remote-ssh-vscode:

Debug from VSCode
##################

.. warning::

    This guide assumes you're already familiar with the fundamentals of Valohai and are working with a project that's connected to a Git repository, and configured on Valohai.

In this guide we'll look at attaching the VSCode remote debugger to a Valohai execution.

.. raw:: html

    <div style="position: relative; padding-bottom: 50.42016806722689%; height: 0;"><iframe src="https://www.loom.com/embed/5112c1c0b4fc4842abfde80463c5ccc1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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

1. Use ``debugpy``
-------------------

Import ``debugpy`` and set it to listen on port ``5678``.

.. code-block:: python
    :emphasize-lines: 1,5,7

    import debugpy
    import numpy as np
    import time

    debugpy.listen(5678)

    # The script is halted here, until a debugger is attached
    debugpy.wait_for_client()

    for x in range(1,20) :
        print(f"Doing computation {x}")
        data = np.random.random((50,50))
        sum = np.sum(data)
        time.sleep(2)

Now update the ``valohai.yaml`` file to install debugpy in your Valohai execution.

.. code-block:: yaml
    :emphasize-lines: 5

    - step:
      name: train
      image: python:3.9
      command: 
        - pip install numpy debugpy
        - python train.py

Commit your changes and push them to your Git repository.

Then launch a new Valohai execution with SSH debugging enabled. Follow the :ref:`remote-ssh` how-to guide for detailed instructions.

2. Connect from VSCode to a remote execution
-----------------------------------------------

Start by opening a SSH tunnel to the Valohai execution. You'll get the IP of the machine from the Valohai execution logs.

.. code-block:: bash

    ssh -i <PATH-TO-YOUR-PRIVATE-SSH-KEY> <IP-FROM-VALOHAI> -p 2222 -L5678:127.0.0.1:5678

..

Open the ``Run and Debug`` panel from VSCode and hit ``Run and Debug`` while you have your ``train.py`` open. Make sure you select the ``Remote Attach`` debug configuration.

.. image:: /_images/ssh_remote_debug_vscode.png
    :alt: Choose Remote Attach as the debug configuration

As soon as your debugger is attached, the code will continue from ``debugpy.wait_for_client()`` and start hitting your breakpoints. When you hit a breakpoint, you'll also be able to see your local variables, and edit them on the fly.

.. video:: /_static/videos/ssh_vscode.mp4
    :autoplay:
    :width: 600

