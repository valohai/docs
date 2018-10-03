.. meta::
    :description: How to link a private GitHub repository to a Valohai project using a read-only SSH deploy key. For this tutorial you will need a private GitHub repository that includes your machine learning code and Valohai YAML file.

Use a private GitHub repository using deploy keys
-------------------------------------------------

In this guide, we'll link a private GitHub repository to a Valohai project using a read-only SSH deploy key.

You can also use GitHub App integration to link private repositories, and you can find that setting on the Valohai project repository settings page.

.. contents::
   :backlinks: none
   :local:

1. Requirements
~~~~~~~~~~~~~~~

For this tutorial you will need:

* a private GitHub repository with Valohai YAML defined
* a Valohai project which to link the repository
* a tool that can generate SSH keys, this guide uses :code:`ssh-keygen` commonly found on computers

.. tip::

   You can also link private GitHub repositories through
   `GitHub Apps authorization <https://developer.github.com/apps/differences-between-apps/>`_
   if you don't wish to manage the secrets yourself.

   .. figure:: github-apps.png
      :alt: GitHub Apps integration button

      You will find this in the project repository settings.

2. Generate an SSH key pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ ssh-keygen -t rsa -b 4096 -N '' -f my-project-deploy-key

The :code:`ssh-keygen` above generates two files:

* :code:`my-project-deploy-key.pub` is the public key you add to GitHub.
* :code:`my-project-deploy-key` is the private key you add to Valohai.

You should not include these keys in the version control. Anybody that gains access to the :code:`my-project-deploy-key` file contents will have read access to your repository so use appropriate caution.

3. Add the public key to GitHib
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the :code:`my-project-deploy-key.pub` file we generated in the last section, and it should contain one line that starts with :code:`ssh-rsa AAAA...`. This line is the public key that we'll be adding to GitHub.

3.1 Go to deploy key settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: github-key-1.png
   :alt: GitHub - route to the deploy key creation page

   Navigate to the add deploy key page in your repository through `Settings` > `Deploy keys` > `Add deploy key`.

3.2 Add new deploy key
^^^^^^^^^^^^^^^^^^^^^^

.. figure:: github-key-2.png
   :alt: GitHub - deploy public key setup example

   Copy and paste the contents of :code:`my-project-deploy-key.pub` into the `Key` field.

   Give the deploy key an identifying `Title` such as Valohai.

   Valohai doesn't require write access, make sure that is off.

3.3 Inspect the new deploy key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: github-key-3.png
   :alt: GitHub - created deploy key example

   After adding the deploy key, it should look something like the this.

4. Add the private key to Valohai
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the :code:`my-project-deploy-key` file (without the :code:`.pub` extension) we generated before. It should contain multiple lines starting with :code:`-----BEGIN RSA PRIVATE KEY-----`. The contents of this file are the private key we'll be adding to Valohai.

4.1 Go to repository settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: valohai-key-1.png
   :alt: Valohai - route to repository settings

   Navigate to the repository settings in your Valohai Project through `Settings` > `Repository`.

4.2 Copy the repository SSH URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: valohai-key-2.png
   :alt: GitHub - where to find repository SSH URL

   To make sure you get the correct repository URL, open GitHub in another tab. On Github, navigate to `Code` page and press `Clone or download`.

   Make sure you have **Clone with SSH** active on the popup window. If it reads `Clone with HTTPS`, click the `Use SSH` button next to the text.

   Then copy the text field with :code:`git@github.com:<owner>/<repository>.git`

4.3 Configure repository settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: valohai-key-3.png
   :alt: Valohai - repository configuration example

   Paste the SSH URL (:code:`git@github.com:<owner>/<repository>.git`) into the `URL` field.

   Change `Fetch reference` if applicable to your use-case. It's essentially the branch Valohai uses. `master` is the most commonly used fetch reference.

   Copy and paste the contents of :code:`my-project-deploy-key` file (without the :code:`.pub` extension) into the `SSH private key` field.

4.4 Save the repository settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: valohai-key-4.png
   :alt: Valohai - screen after saving repository settings

   After you click `Save`, Valohai links the GitHub repository to the project and automatically fetches your code.

   On errors, double check the fields or contact support through Intercom.

4.5 Update project as necessary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: valohai-key-5.png
   :alt: Valohai - highlighted Fetch repository button

   After you add new commits to your GitHub repository, remember to press the `Fetch repository` to update the code in Valohai.

5. Results
~~~~~~~~~~

We linked a private GitHub repository to a Valohai project using GitHub deploy keys.
