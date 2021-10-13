
.. meta::
    :description: How remotely access and debug live execution

.. _remote-ssh:

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

  Remote access is available for enterprise users who are using onprem, AWS, or GCP environments.

  Your organization admin needs to enable SSH connection to the workers and edit the firewall rules in your cloud provider.

0. Configure SSH Access for your organization
-----------------------------------------------

Your organization admin will need to configure the organization wide settings and firewall rules before you can use remote SSH connections.

Define the default SSH port
============================

Define a default port for SSH connections in your organization
    
* Navigate to ``Hi, <name> (the top right menu) > Manage <organization>``
* Go to *Settings* under the organization controls
* Set a *Default Debug Port* for your organization. Note, the value must be above 1023

Allow connections on selected port
==================================

You'll need to edit the firewall rules in your cloud to allow users to connect to the workers on the defined port.

.. tab:: AWS

   In AWS open the Security Group ``valohai-sg-workers`` and click *Edit Inbound rules* to add a new inbound Custom TCP rule:

   * **Type:** Custom TCP
   * **Port range:** The port number you specified in your Valohai organization's settings.
   * **Source:** Depending on your organization settings you can either set Source as 0.0.0.0/0 to allow connections from anywhere or whitelist certain IP ranges / source tags
   * **Description:** Allows connecting to Valohai jobs over SSH

   Setting the source as 0.0.0.0/0 means that inbound connections will be allowed from all addresses. However, you'll still need the SSH Private Key (generated below) in order to authenticate and successfully connect.


.. tab:: GCP

   In GCP create a new firewall rule:

   * **Name:** ``valohai-fr-worker-ssh``
   * **Description:** Allows connecting to Valohai jobs over SSH
   * **Network:** The network where your Valohai resources are created (e.g. ``valohai-vpc``)
   * **Direction:** Ingress
   * **Targets:** Specificed target tags: ``valohai-worker``
   * **Source:** Depending on your organization settings you can either set Source as 0.0.0.0/0 to allow connections from anywhere or whitelist certain IP ranges / source tags.
   * **Specified protocols and ports:**
     * TCP: with the port number you specified in your Valohai organization's settings.

   Setting the source as 0.0.0.0/0 means that inbound connections will be allowed from all addresses.. However, you'll still need the SSH Private Key (generated below) in order to authenticate and successfully connect.


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

   vh exec run --adhoc --debug-key-file=/tmp/remote-debug-key.pub train

3. Wait for an IP address
----------------------------------

You need to start the Valohai execution before you can connect to it. Valohai will either run the execution on an existing virtual machine or create a new instance. Each machine has its own IP which is allocated by the cloud provider (e.g. AWS, GCP, Azure). You'll need the IP in order to SSH into the execution.

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

This will execute the command and return the results to your terminal.
.. code-block:: bash

   # template
   ssh -i <path-to-private-key> <ip-address> -p <port> -t <command>

   # example
   ssh -i /home/johndoe/.ssh/my-debug-key 52.214.159.193 -p 2222 -t ps aux

**Open an interactive shell**

Allows you to connect to the execution and run commands directly inside the Docker container that's running your execution.
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
