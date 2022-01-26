.. meta::
    :description: How to link a private Azure DevOps repository to a Valohai project using a read-only SSH deploy key. For this tutorial you will need a private GitHub repository that includes your machine learning code and Valohai YAML file.

.. _repository-azuredevops:

Integrating with Azure DevOps
==============================

In this guide, we'll link a private Azure Devops repository to a Valohai project using a deploy key.

.. admonition:: Requirements
   :class: attention

   * A private Azure DevOps repository
   * A Valohai project
   * A tool that generates SSH keys. This guide uses ``ssh-keygen``

..

Generate an SSH key pair
#########################

Use :code:`ssh-keygen` to create a new SSH key pair.

.. code-block:: bash

   $ ssh-keygen -t rsa -b 4096 -N '' -f my-project-deploy-key

This will generate two files:

* :code:`my-project-deploy-key.pub` is the public key you add to GitHub.
* :code:`my-project-deploy-key` is the private key you add to Valohai.

.. admonition:: Don't include the keys in your version control
   :class: warning

   You should not include these keys in the version control. Anybody that gains access to the :code:`my-project-deploy-key` file contents will have read access to your repository, so use appropriate caution.
..

Add the public key to Azure DevOps
###################################

Find the :code:`my-project-deploy-key.pub` file we generated in the last section, and it should contain one line that starts with :code:`ssh-rsa AAAA...`. This line is the public key that we'll be adding to Azure DevOps.

Now go to your Azure DevOps repository and navigate to the add deploy key page by clicking on  `User settings` > `SSH Public Keys`

.. image:: azure-devops-key-1.png
   :alt: Azure DevOps - route to the deploy key creation page


Add the private key to Valohai
#################################

Go to app.valohai.com and navigate to the repository settings in your Valohai Project through `Settings` > `Repository`.

.. image:: /tutorials/valohai-key-1.png
   :alt: Valohai - route to repository settings

To make sure you get the correct repository URL, open Azure DevOps in another tab. On Azure DevOps, navigate to your project > `Repos` page and under `Clone to your computer`

Make sure you **Clone with SSH**. By default the `HTTPS` is selected so make sure you click the `SSH` button to get the right URL.

Then copy the text field with :code:`git@github.com:<owner>/<repository>.git`

.. image:: azure-devops-choose-ssh.png
   :alt: Azure DevOps - where to find repository SSH URL


Next paste the SSH URL (:code:`git@ssh.dev.azure.com:v3/<owner>/<project>/<repository>`) into the `URL` field.

On your local machine, find the :code:`my-project-deploy-key` file (without the :code:`.pub` extension) we generated before. It should contain multiple lines starting with :code:`-----BEGIN RSA PRIVATE KEY-----`  or something similar. The contents of this file are the private key we'll be adding to Valohai.
Copy and paste the contents of :code:`my-project-deploy-key` into the `SSH private key` field.

.. image:: /tutorials/valohai-key-3.png
   :alt: Valohai - repository configuration example


After you click **Save**, Valohai links the GitHub repository to the project and automatically fetches your code.

After you add new commits to your GitHub repository, remember to press the **Fetch repository** to update the code in Valohai.

.. image:: /tutorials/valohai-key-5.png
   :alt: Valohai - highlighted Fetch repository button
