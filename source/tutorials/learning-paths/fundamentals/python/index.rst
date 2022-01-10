.. meta::
    :description: Valohai Fundamentals learning path - Running your first Valohai execution with Python

:orphan:

Python
^^^^^^^

This learning path will show you how to get started with Valohai and Python, without using the ``valohai-utils`` helper library.

.. admonition:: Prerequirements
    :class: attention

    Before starting make sure you have created and account at `app.valohai.com <https://app.valohai.com>`_ and that you have been added to a Valohai organization. Your organization admin can invite you to join the organization.


Start by creating a new folder on your local machine, and installing the Valohai tools:

.. code-block:: bash

    mkdir valohai-tutorial
    cd valohai-tutorial

    # Install the Valohai command line tools
    pip install valohai-cli


Next login to Valohai and link your local folder to a new Valohai project:

.. code-block:: bash

    vh login
    # ... login with your username and password

    vh project create
    # give the project a name

.. note:: 

    Depending on your organization settings, you might be asked to choose the owner for the project. We suggest choosing the organization as the owner of the project.

.. note:: 

    If your organization is on a self-hosted version of Valohai, you'll need to specify the login address with ``vh login --host https://myvalohai.com``

.. toctree::
    :titlesonly:

    2-get-started
    3-outputs
    4-parameters
    5-inputs
    6-metadata
    7-recap

..