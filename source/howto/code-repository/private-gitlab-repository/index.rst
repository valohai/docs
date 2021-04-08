.. meta::
    :description: How to use a private GitLab repository with a Valohai project using a deploy key.


.. _repository-gitlab:

Integrating with GitLab
========================

In this guide, we'll link a private GitLab repository to a Valohai project using a deploy key.

.. admonition:: Requirements
   :class: attention

   * A private Gitlab repository
   * A Valohai project
   * A tool that generates SSH keys. This guide uses ``ssh-keygen``

..

Generate an SSH key pair
#########################

Use :code:`ssh-keygen` to create a new SSH key pair.

.. code-block:: bash

   $ ssh-keygen -t rsa -b 4096 -N '' -f my-project-deploy-key

This will generate two files:

* :code:`my-project-deploy-key.pub` is the public key you add to GitLab.
* :code:`my-project-deploy-key` is the private key you add to Valohai.

.. admonition:: Don't include the keys in your version control
   :class: warning

   You should not include these keys in the version control. Anybody that gains access to the :code:`my-project-deploy-key` file contents will have read access to your repository, so use appropriate caution.
..

Add the public key to GitLab
#############################

Find the :code:`my-project-deploy-key.pub` file we generated in the last section, and it should contain one line that starts with :code:`ssh-rsa AAAA...`. This line is the public key that we'll be adding to GitLab.

Navigate to the add deploy key page in your GitLab repository at `Settings` > `Repository` > `Deploy Keys`.

.. note::

    If you can't see this `Deploy Keys` menu, you are most likely lacking the permissions to add deploy keys so contact your GitLab admins.

.. image:: gitlab-key-1.png
   :alt: GitLab - route to the deploy key creation page


* Copy and paste the contents of :code:`my-project-deploy-key.pub` into the `Key` field.
* Give the deploy key an identifying `Title` such as Valohai.
* Valohai doesn't require write access, make sure that is off.

.. thumbnail:: gitlab-key-2.png
   :alt: GitLab - deploy public key setup example

Add the private key to Valohai
####################################

Go to app.valohai.com and navigate to the repository settings in your Valohai Project through `Settings` > `Repository`.

.. image:: /tutorials/valohai-key-1.png
   :alt: Valohai - route to repository settings

To make sure you get the correct repository URL, open GitLab in another tab. On GitLab, navigate to `Code` page and press `Clone or download`.

Make sure you have **Clone with SSH** active on the popup window. If it reads `Clone with HTTPS`, click the `Use SSH` button next to the text.

Then copy the text field with :code:`git@GitLab.com:<owner>/<repository>.git`

.. image:: gitlab-key-3.png
   :alt: GitLab - where to find repository SSH URL


Next paste the SSH URL (:code:`git@GitLab.com:<owner>/<repository>.git`) into the `URL` field.

On your local machine, find the :code:`my-project-deploy-key` file (without the :code:`.pub` extension) we generated before. It should contain multiple lines starting with :code:`-----BEGIN RSA PRIVATE KEY-----`  or something similar. The contents of this file are the private key we'll be adding to Valohai.

Copy and paste the contents of :code:`my-project-deploy-key` into the `SSH private key` field.

.. image:: /tutorials/valohai-key-3.png
   :alt: Valohai - repository configuration example


After you click **Save**, Valohai links the GitLab repository to the project and automatically fetches your code.

After you add new commits to your GitLab repository, remember to press the **Fetch repository** to update the code in Valohai.

.. image:: /tutorials/valohai-key-5.png
   :alt: Valohai - highlighted Fetch repository button
