.. meta::
    :description: Setting a private Bitbucket repository to a Valohai project using an read-only access key.

Private Bitbucket Repository
============================

In this guide, we'll link a private Bitbucket repository to a Valohai project using an access key.

.. contents::
   :backlinks: none
   :local:

1. Requirements
~~~~~~~~~~~~~~~

For this tutorial you will need:

* a private Bitbucket repository
* a Valohai project which to link the repository
* a tool that generates SSH keys, this guide uses :code:`ssh-keygen`

2. Generate an SSH key pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ ssh-keygen -t rsa -b 4096 -N '' -f my-project-access-key

The :code:`ssh-keygen` above generates two files:

* :code:`my-project-access-key.pub` is the public key you add to Bitbucket.
* :code:`my-project-access-key` is the private key you add to Valohai.

You should not include these keys in the version control. Anybody that gains access to the :code:`my-project-access-key` file contents will have read access to your repository so use appropriate caution.

3. Add the public key to Bitbucket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the :code:`my-project-access-key.pub` file we generated in the last section, and it should contain one line that starts with :code:`ssh-rsa AAAA...`. This line is the public key that we'll be adding to Bitbucket.

3.1 Go to access key settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: bitbucket-key-1.png
   :alt: Bitbucket - route to the access key creation page

   Navigate to the add access key page in your repository at `Settings` > `Access Keys` > `Add key`.

3.2 Add new access key
^^^^^^^^^^^^^^^^^^^^^^

.. figure:: bitbucket-key-2.png
   :alt: Bitbucket - access key setup example

   Copy and paste the contents of :code:`my-project-access-key.pub` into the `Key` field.

   Give the access key an identifying `Label` such as Valohai.

4. Add the private key to Valohai
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the :code:`my-project-access-key` file (without the :code:`.pub` extension) we generated before. It should contain multiple lines starting with :code:`-----BEGIN RSA PRIVATE KEY-----` or something similar. The contents of this file are the private key we'll be adding to Valohai.

4.1 Go to repository settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: valohai-key-1.png
   :alt: Valohai - route to repository settings

   Navigate to the repository settings in your Valohai Project through `Settings` > `Repository`.

4.2 Copy the repository SSH URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: bitbucket-key-3.png
   :alt: Bitbucket - where to find repository SSH URL

   To make sure you get the correct repository URL, open Bitbucket in another tab. On Bitbucket, navigate to `Source` page and press `Clone`.

   Make sure you select **SSH** at the top right dropdown.

   Copy the SSH address without the ``git clone``, something like :code:`git@bitbucket.com:<owner>/<repository>.git`

4.3 Configure repository settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: valohai-key-3.png
   :alt: Valohai - repository configuration example

   Paste the SSH URL (:code:`git@bitbucket.com:<owner>/<repository>.git`) into the `URL` field.

   Change `Fetch reference` if applicable to your use-case. It's essentially the branch Valohai uses. `master` is the most commonly used fetch reference.

   Copy and paste the contents of :code:`my-project-access-key` file (without the :code:`.pub` extension) into the `SSH private key` field.

4.4 Save the repository settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: valohai-key-4.png
   :alt: Valohai - screen after saving repository settings

   After you click `Save`, the repository links to the project and automatically fetches your code.

   On errors, double check the fields or contact support through Intercom.

4.5 Update project as necessary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: valohai-key-5.png
   :alt: Valohai - highlighted Fetch repository button

   After you add new commits to your Bitbucket repository, remember to press the `Fetch repository` to update the code in Valohai.

5. Results
~~~~~~~~~~

We linked a private Bitbucket repository to a Valohai project using access keys.
