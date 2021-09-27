
.. meta::
    :description: How remotely access and debug live execution

.. _executions-compare:

Remote access (SSH)
################################

Valohai offers remote access to a live execution with `SSH <https://en.wikipedia.org/wiki/Secure_Shell>`_ (Secure Shell).
It is a low-level and agnostic protocol, which makes it usable for a wide array of tasks.

**Common use-cases**

* Inspecting the execution using an interactive terminal
* Connect your favorite IDE debugger like VSCode or PyCharm
* Low-latency integration with 3rd party tools like Tensorboard

.. admonition:: Prerequirements
  :class: attention

  * TODO

1. Create an SSH keypair
----------------------------------

An SSH keypair is required for securing the connection. You may re-use an existing keypair, but please be mindful of
regenerating it periodically according to your security standards.

Use :code:`ssh-keygen` to create a new SSH key pair.

.. code-block:: bash

   $ ssh-keygen -t rsa -b 4096 -N '' -f my-debug-key

This will generate two files:

* :code:`my-debug-key.pub` is the public key you paste into UI before starting an execution.
* :code:`my-debug-key` is the private key you need for connecting to the execution.

.. admonition:: Don't include the keys in your version control
   :class: warning

   You should **not** include these keys in the version control. Anybody that gains access to the :code:`valohai-debug-key` file contents will have access to your execution, so use appropriate caution.
..

2. Start an execution
----------------------------------

Valohai GUI
===========

.. thumbnail:: /howto/remote-access/start-execution.png
   :alt: Start Valohai execution with SSH enabled
..

Start a Valohai execution with the "Run with SSH" enabled.

Copy-paste the entire contents of the :code:`my-debug-key.pub` file into the text field. Change the TCP/IP port if
your network setup requires it.

Valohai CLI
===========

Start a Valohai execution with extra parameter :code:`debug-key-file` for your public key file (and additionally :code:`debug-port`).

.. code-block:: bash

   vh exec run -a --debug-key-file=/tmp/remote-debug-key.pub train

3. Wait for an IP address
----------------------------------

In order to connect to a remote execution, we need for it to start first. The worker IP address
can't be known beforehand as multiple workers are available to pick up the job from the Valohai job queue.

Wait for the execution to start and watch for the first log events. Look for (something like) this:

.. code-block:: bash

   You can now add the path to your private key and connect:
   $ ssh -i <path-to-private-key> 52.214.159.193 -p 2222 -t /bin/bash


.. thumbnail:: /howto/remote-access/execution-logs.png
   :alt: Start Valohai execution with SSH enabled
..

4. Open an SSH connection
----------------------------------

Now depending on what your use-case, you may want to do one of these things:

* Run a single remote command
* Open an interactive shell
* Open an SSH tunnel

**Run a single command**

.. code-block:: bash

   # template
   ssh -i <path-to-private-key> <ip-address> -p <port> -t <command>

   # example
   ssh -i /home/johndoe/.ssh/my-debug-key 52.214.159.193 -p 2222 -t ps aux

**Open an interactive shell**

.. code-block:: bash

   # template
   ssh -i <path-to-private-key> <ip-address> -p <port> -t /bin/bash

   # example
   ssh -i /home/johndoe/.ssh/my-debug-key 52.214.159.193 -p 2222 -t /bin/bash

**Open an SSH tunnel**

.. code-block:: bash

   # template
   ssh -i <path-to-private-key> <ip-address> -p <port> -t -L<local-port>:<localhost>:<local-port>

.. code-block:: bash

   # example
   ssh -i ~/.ssh/remote-debug-key 34.245.207.101 -p 2222 -t -L5678:127.0.0.1:5678


How to keep the execution running?
----------------------------------

You execution is designed to start, compute, and shut down on errors. When debugging, we want to keep the
execution running even if it fails.

The safest way is to add a sleep command at the end of the execution.

.. code-block:: bash

   python train.py {parameters}
   sleep 1h

This way, the execution will wait for an hour and then shut down. It is better to set a reasonable
time limit instead of an infinite uptime to avoid costly mistakes.

Limitations
----------------------------------

It is essential to understand that the SSH connection is not directly to the worker operating system.

We are opening remote access to the docker container running within that host operating system. It means that
the Valohai platform internals and the rest of the host operating system are not available for inspection
