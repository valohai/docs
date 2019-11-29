.. meta::
    :description: Use Valohai local workers to manage and version control your data science workloads.

Managing On-premises Workers
============================

On-premises Valohai Enterprise installation allows managing your local Valohai workers.

A single physical or virtual machine can have any number of workers but we recommend allocating at least one GPU per worker if you are utilizing graphic cards in your machine learning workloads.

.. tip::

    Depending on the setup, you might be required to invoke the following commands using ``sudo <COMMAND>``. You can also call ``sudo su`` to switch to administrator user for the duration of the current terminal session.

At its core, Valohai worker is a systemd-based service called ``peon``.

.. code-block:: bash

    service "peon@*" status    # see status of all local workers
    service "peon@*" stop      # stop all workers e.g. if you want to do an update
    service "peon@*" start     # start all workers
    service "peon@*" restart   # restart all workers

You can also control individual workers. Worker numbering starts from 0.

.. code-block:: bash

    service "peon@0" status
    service "peon@1" stop
    service "peon@2" start

These worker will take new executions from your work queue as they appear.
You can queue as much work as you wish and the workers will process them as they become free.

Valohai worker runs encapsulated workloads in Docker containers, here are helpful commands that you can use to managed those:

.. note::

    Valohai also includes a cleanup service called ``peon-clean`` so running the following Docker maintenance commands
    is not necessary except in special cases.


.. code-block:: bash

    docker ps         # see all containers; note that all might not be from Valohai
    docker stop <id>  # kill a running container
    docker rm <id>    # remove container history information to free up space
    docker rmi <name> # remove a cached image to free up space
