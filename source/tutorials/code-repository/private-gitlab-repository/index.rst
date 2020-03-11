.. meta::
    :description: How to use a private GitLab repository with a Valohai project using a deploy key.

Integrating with GitLab
=======================

In this guide, we'll link a private GitLab repository to a Valohai project using a deploy key.

.. contents::
   :backlinks: none
   :local:

1. Requirements
~~~~~~~~~~~~~~~

For this tutorial you will need:

* a private GitLab repository
* a Valohai project which to link the repository
* a tool that generates SSH keys, this guide uses :code:`ssh-keygen`
* access from Valohai (IP address: 34.248.245.191) through your firewall to your private GitLab

2. Generate an SSH key pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ ssh-keygen -t rsa -b 4096 -N '' -f my-project-deploy-key

The :code:`ssh-keygen` above generates two files:

* :code:`my-project-deploy-key.pub` is the public key you add to GitLab.
* :code:`my-project-deploy-key` is the private key you add to Valohai.

You should not include these keys in the version control. Anybody that gains access to the :code:`my-project-deploy-key` file contents will have read access to your repository so use appropriate caution.

3. Add the public key to GitLab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the :code:`my-project-deploy-key.pub` file we generated in the last section, and it should contain one line that starts with :code:`ssh-rsa AAAA...`. This line is the public key that we'll be adding to GitLab.

3.1 Go to deploy key settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: gitlab-key-1.png
   :alt: GitLab - route to the deploy key creation page

Navigate to the add deploy key page in your repository at `Settings` > `Repository` > `Deploy Keys`.

.. note::

    If you can't see this `Deploy Keys` menu, you are most likely lacking the permissions to add deploy keys so contact your GitLab admins.

3.2 Add new deploy key
^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: gitlab-key-2.png
   :alt: GitLab - deploy public key setup example

Copy and paste the contents of :code:`my-project-deploy-key.pub` into the `Key` field.

Give the deploy key an identifying `Title` such as Valohai.

Valohai doesn't require write access, make sure that is off.

4. Add the private key to Valohai
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the :code:`my-project-deploy-key` file (without the :code:`.pub` extension) we generated before. It should contain multiple lines starting with :code:`-----BEGIN RSA PRIVATE KEY-----` or something similar. The contents of this file are the private key we'll be adding to Valohai.

4.1 Go to repository settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: /tutorials/valohai-key-1.png
   :alt: Valohai - route to repository settings

Navigate to the repository settings in your Valohai Project through `Settings` > `Repository`.

4.2 Copy the repository SSH URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: gitlab-key-3.png
   :alt: GitLab - where to find repository SSH URL

To make sure you get the correct repository URL, open GitLab in another tab. On GitLab, navigate to `Project Details` page and press `Clone`.

Make sure you select the **Clone with SSH** field.

Then copy the field contents, something like :code:`git@gitlab.com:<owner>/<repository>.git`

4.3 Configure repository settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: /tutorials/valohai-key-3.png
   :alt: Valohai - repository configuration example

Paste the SSH URL (:code:`git@gitlab.com:<owner>/<repository>.git`) into the `URL` field.

Change `Fetch reference` if applicable to your use-case. It's essentially the branch Valohai uses. `master` is the most commonly used fetch reference.

Copy and paste the contents of :code:`my-project-deploy-key` file (without the :code:`.pub` extension) into the `SSH private key` field.

4.4 Save the repository settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: /tutorials/valohai-key-4.png
   :alt: Valohai - screen after saving repository settings

After you click `Save`, the repository links to the project and automatically fetches your code.

On errors, double check the fields or contact support through Intercom.

4.5 Update project as necessary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: /tutorials/valohai-key-5.png
   :alt: Valohai - highlighted Fetch repository button

After you add new commits to your GitLab repository, remember to press the `Fetch repository` to update the code in Valohai.

5. Results
~~~~~~~~~~

We linked a private GitLab repository to a Valohai project using GitLab deploy keys.
