.. meta::
    :description: Valohai Fundamentals learning path - Running your first Valohai execution with valohai-utils

``valohai-utils`` (Python)
##########################

This learning path will show you how to get started with Valohai and Python, using the valohai-utils helper library.

valohai-utils streamlines pipeline definition and writing Valohai-compatible code. This is achieved by offering utility functions for the most common tasks.

**What does valohai-utils do?**

* Generates and updates the :ref:`yaml` based on the source code
* Agnostic input handling (single file, multiple files, zip, tar)
* Parse command-line parameters
* Compress outputs
* Download inputs for local experiments
* Straightforward way to print metrics as Valohai metadata
* Code parity between local vs. cloud

.. seealso::

    `Read more about valohai-utils </topic-guides/valohai-utils/>`_

Install the tools
-------------------

Start by creating a new folder on your local machine, and installing the Valohai tools:

.. code-block:: bash

    mkdir valohai-tutorial
    cd valohai-tutorial

    # Install the Valohai command line tools
    pip install valohai-cli valohai-utils


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