.. meta::
    :description: Connect an OpenStack Swift container holding your data to a Valohai project to automate machine learning workloads. Consider creating many containers to streamline data science team collaboration over different projects.

Linking OpenStack Swift
=======================

In this guide, we'll link a private `OpenStack Swift <https://wiki.openstack.org/wiki/Swift>`_ container to a Valohai project.

.. contents::
   :backlinks: none
   :local:

1. Requirements
~~~~~~~~~~~~~~~

For this tutorial you will need:

* an OpenStack account you can administer
* a Valohai project which to link the Swift container to
* any modern version of Python

2. Install OpenStack clients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First we need to install OpenStack and Swift command-line clients.

.. code-block:: bash

    pip install python-openstackclient python-swiftclient

Then we need to authenticate to your OpenStack installation.
The easiest way to authenticate is using an OpenStack RC File if your provider allows generating those.
More authentication methods in `OpenStack documentation <https://docs.openstack.org/python-openstackclient/latest/cli/authentication.html>`_.

For example:

.. thumbnail:: swift-01.png
   :alt: An example how to get OpenStack RC File on Pouta OpenStack installation.

Run the OpenStack RC File:

.. code-block:: bash

    source project-1234-openrc.sh
    # it will ask your password but you can optionally edit the .sh file
    # to include your password automatically by editing the OS_PASSWORD variable

Now your OpenStack client is ready for use.

3. Create a container
~~~~~~~~~~~~~~~~~~~~~

Create a Swift container for your Valohai project.

.. code-block:: bash

    openstack container create my-project-data
    +----------------+-----------------+------------+
    | account        | container       | x-trans-id |
    +----------------+-----------------+------------+
    | AUTH_123456789 | my-project-data | 1234567890 |
    +----------------+-----------------+------------+

    openstack container show my-project-data
    +--------------+--------------------------------+
    | Field        | Value                          |
    +--------------+--------------------------------+
    | account      | AUTH_123456789                 |
    | bytes_used   | 0                              |
    | container    | my-project-data                |
    | object_count | 0                              |
    +--------------+--------------------------------+

3.1 Configure Temporary URL key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Temporary URL keys are required to give secure download privileges for Valohai workers.

.. code-block:: bash

    # generate random string from somewhere to use as Temporary URL key, e.g.
    cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1
    # set the key to the Swift cluster
    swift post -m "Temp-URL-Key:randomlygeneratedkey"

3.2 Configure CORS
^^^^^^^^^^^^^^^^^^

If you wish to be able to upload files to the store using the Valohai web user interface, you will need to
add a CORS (Cross-Origin Resource Sharing) policy to the Swift container.

.. code-block:: bash

    openstack container set \
        --property Access-Control-Allow-Origin='https://app.valohai.com' \
        --property Access-Control-Max-Age='3000' \
        my-project-data

    swift stat -v my-project-data
    # ...
    Meta Access-Control-Allow-Origin: https://app.valohai.com
    Meta Access-Control-Max-Age: 3000
    # ...

Now your container allows uploads from `https://app.valohai.com` website

4. Link the store to Valohai
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: swift-02.png
   :alt: Where to find the OpenStack Swift container configuration.

Navigate to `Project > Settings > Data Stores > Add OpenStack Swift Object Store`

.. thumbnail:: swift-03.png
   :alt: Screenshot with some example Swift data store configuration.

Required fields:

- **Name:** Understandable name for the storage.
- **Auth URL:** This can be found in the OpenStack RC File, variable :code:`OS_AUTH_URL`.
- **Auth Version:** Valohai currently only supports 3.0. Contact support for more information.
- **Username:** Your OpenStack account username.
- **Password:** Your OpenStack account password.
- **Container Name:** The name of the container. We used :code:`my-project-data` in this guide.
- **Region Name:** :code:`openstack region list` gives you a list of all the regions for your installation.
- **Temp URL Key:** This is the key we previously generated in step 3.1.

.. thumbnail:: swift-04.png
   :alt: Making the new data store default data store for the project.

Once the store has been set up, you can set the store as your project's default store in
the `Settings > Basic Information` view. This ensures outputs will be stored in your Swift container.
