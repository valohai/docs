.. meta::
    :description: Learn how to access additional private repositories during your execution

Access additional git repository during execution runs
#########################################################

Each Valohai project can be connected either to a public or a private Git repository. Having a repository linked to a project will allow you to easily reproduce your experiments with the exact code and configuration files used in your commit.

When you run a Valohai execution all the files from the specified commit will be copied to your working folder (``/valohai/repository/``)

However, sometimes you might want to connect and fetch additional files from a different private repository. In this tutorial we'll show you how to authenticate and fetch files from another private repository during an execution run.

.. admonition:: A note on versioning and reproducability
    :class: warning
    
    Valohai allows you easily to reproduce past executions with the exact same code version by keeping track of the repository connected to the project and the commit used for the execution.
    
    Valohai won't keep track of the commits from other repositories that you access and clone in your code.

..


Generate a new ssh key
-------------------------

- Generate a new `SSH Key <https://www.ssh.com/ssh/keygen/>`_ For example ``ssh-keygen -t rsa -b 4096 -C "me@example.com"``
- Add the `.pub` file as a Deploy key to your code source control (GitHub, GitLab, BitBucket etc.)

Add the private key to Valohai
---------------------------------

Next we'll need to add the private key to Valohai, so we can access it during an execution. You can safely store this value as a environment variable under your project settings on Valohai.

.. container:: alert alert-warning

    The Valohai environment secret doesn’t encode the newlines from your ssh key. So you'll need to edit your key and add ``\n`` around the secret before pasting it to Valohai.
    
    Your key should look like this:
    
    ``-----BEGIN OPENSSH PRIVATE KEY-----\n<your-secret>\n-----END OPENSSH PRIVATE KEY-----``

..

* Go to `app.valohai.com <https://app.valohai.com>`_
* Open your project and go to Settings -> Environment Variables to add a new secret.
* Give the variable a name ``PRIVATE_KEY`` and paste in the value of the private key you generated (with the ``\n``).
* Check the *secret* box to hide the value from the UI and save the value.

Clone the repository
----------------------

Finally edit your ``valohai.yaml`` configuration file to download the git repository.

.. code:: yaml

    ---

    - step:
        name: Download repo
        image: python:3.6
        command:
            - apt-get update
            # Install Git
            - apt-get install -y git
            # Store the environment variable in a file
            - echo -e $PRIVATE_KEY > ~/key_file
            - chmod 600 ~/key_file
            # Configure git to use the key
            - export GIT_SSH_COMMAND="ssh -vvv -o StrictHostKeyChecking=no -i ~/key_file"
            # Clone the repository
            - git clone git@github.com:account/repository.git /downloaded_repo 
            - ls -la /downloaded_repo # List contents of the download folder (optional)
            # Run your script
            - python main.py

..

You'll then be able to access the files during runtime from your scripts. For example:

.. code:: python

    with open('/downloaded_repo/README.md', 'r') as f:
        print(f.read())

..