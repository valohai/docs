.. meta::
    :description: Command listing for the Valohai command-line client

.. _cli:


``valohai-cli`` command-line
=============================

``valohai-cli`` is a command-line tool to manage your Valohai experiments and installations.

This reference guide gives you an overview of the command available in the client, and you can dive
deeper by with ``vh --help`` or adding the ``--help`` to any of the commands.

More information about the specific commands:

.. toctree::
    :titlesonly:

    environments
    execution
    init
    lint
    login
    logout
    parcel
    project
    update-check

.. click:: valohai_cli.cli:cli
   :prog: vh
