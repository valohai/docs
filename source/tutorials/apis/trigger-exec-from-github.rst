.. meta::
    :description: In this tutorial you'll learn to use GitHub Actions to trigger a Valohai execution from a new push to a GitHub repository.

Triggering an execution after a push to a code repository
=========================================================

.. container:: alert alert-success

    **Not using GitHub?** Scroll down to `see a example of the Valohai API call </tutorials/apis/trigger-exec-from-github/#define-the-action-that-should-be-triggered>`_ you'd need to trigger from your own code repository (e.g. WebHooks on `GitLab <https://docs.gitlab.com/ee/user/project/integrations/webhooks.html>`_ or `BitBucket <https://confluence.atlassian.com/bitbucket/manage-webhooks-735643732.html>`_)

..

GitHub Actions allow you to automate development workflows right from your repository. In this tutorial we'll use GitHub Actions to trigger a new execution on Valohai every time a new push is made to our repository.

➡️ Check out `GitHub Actions Documentation <https://help.github.com/en/actions>`_ to learn more about Actions.

.. container:: alert alert-warning

    **Pre-requisites**

    * Existing Valohai project with a ``valohai.yaml`` file and at least one step. You can find a sample valohai.yaml and train.py from the `sample repository <https://github.com/DrazenDodik/vh_execution_onpush>`_ of this tutorial.
    * Your project is `connected to a GitHub repository </tutorials/code-repository/private-github-repository/>`_ (either public or private)

..


Create your GitHub Action workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Workflows are used to define an automated process for your repository. In our case we'll define a workflow that triggers a new action every time there is a push to the repository.

A workflow needs to know when it should be triggered, what are the jobs to run and in which environment should it run these jobs.

* In your existing project, create a new folder ``.github/``
* Add a new folder to keep our workflows ``.github/workflows/``
* Create a new file called ``.github/workflows/main.yml`` and define the workflow as:

    .. code:: yaml

        name: Workflow for Create Valohai execution on push
        on: push
        jobs:
        build:
            name: Create Valohai execution on push
            runs-on: ubuntu-latest
            steps:
            - uses: actions/checkout@v1
            - uses: ./valohai-execution-action

    ..

Define the action that should be triggered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GitHub Actions can run directly on the machine (JavaScript) on in a Docker container.

Our action will run a Python script inside a Docker container. That script will use the Valohai APIs to trigger a new Valohai execution based on the new commit.

* Start by creating a new folder in the root of your directory ``valohai-execution-action/``.

* Create a new file ``valohai-execution-action/runExecution.py``. In there create a new call to the Valohai APIs.
    * You'll need an `authentication token <https://app.valohai.com/auth/>`_ and know your project ID to continue. You can find your project's ID under its Settings-tab.

    .. code:: python

        import requests
        import json
        import os

        # Authenticate yourself with the token
        auth_token = '<your-auth-token>'
        headers = {'Authorization': 'Token %s' % auth_token}
        project_id = '<your-project-id>'
        step_name = '<your-step-name-from-valohai.yaml>'

        # Fetch all new changes from the repository
        # https://app.valohai.com/api/docs/#projects-fetch
        # This will fetch changes from all the branches that you've defined on the Project->Settings->Repository tab
        fetchResponse = requests.post(('https://app.valohai.com/api/v0/projects/{0}/fetch/').format(project_id), data={'id': project_id}, headers=headers)
        fetchResponse.raise_for_status()


        # Define the payload for a new execution
        # https://app.valohai.com/api/docs/#executions-create
        #
        # GitHub Actions creates an environment variable on the Docker container
        # Called GITHUB_SHA that stores the identifier of the commit that was created
        new_exec_payload = {
        "project": project_id,
        "commit": os.getenv('GITHUB_SHA'),
        "step": step_name,
        }

        # Send a POST request to create a new execution
        createExecutionResponse = requests.post('https://app.valohai.com/api/v0/executions/', data=new_exec_payload, headers=headers)
        createExecutionResponse.raise_for_status()

        # Print the response you've received back
        print('# API Response:\n')
        print(json.dumps(createExecutionResponse.json(), indent=4))


    ..

* Next create a ``valohai-execution-action/Dockerfile`` that will be used to build your container
    .. code:: yaml

        # We'll use a slim python image as a base
        FROM python:3.8.2-slim-buster

        # Our code will need requests, so we can install them on the image with pip
        RUN pip install requests

        # Add our file and run it
        ADD runExecution.py /runExecution.py
        CMD ["/runExecution.py"]
        ENTRYPOINT ["python"]

    ..

* Finally we'll need to create ``valohai-execution-action/action.yml`` to describe our action for GitHub
    .. code:: yaml

        name: "Create Valohai execution on push"
        description: "Run a new execution on app.valohai.com on each new push to repository"
        author: "<your-email>"

        runs:
          using: "docker"
          image: "Dockerfile"

    ..

Push a new commit
^^^^^^^^^^^^^^^^^^^

✨ Ta-da! That's it! Now you can commit your code and the push changes.
    * ``git add .github/ *``
    * ``git commit -m "added github action to trigger vh executions"```
    * ``git push``

Navigate to your GitHub repository's ``Actions`` tab to see the new action...in action 😂

You can test it out by making some changes to your step's code (e.g. ``train.py``) and push the changes to GitHub. You should see the Action trigger and create a new execution on Valohai with that new commit.
