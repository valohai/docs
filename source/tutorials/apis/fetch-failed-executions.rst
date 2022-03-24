.. meta::
    :description: Learn how to use Valohai APIs to fetch all failed executions of a project

Fetching failed executions
=============================

.. include:: _use-apis-basic.rst

* You'll need the ID of a single project to fetch its executions. You can get it from the projects' setting page or `query for it using the Valohai APIs </tutorials/apis/fetch-projects>`_ results.
* Create a new file ``fetchExecutions.py``
    .. code:: Python

      import requests
      import json
      import os

      # Authenticate yourself with the token.
      # Remember to follow your organization's security standards when handling the token.  
      auth_token = os.environ['VH_API_TOKEN']
      headers = {'Authorization': 'Token %s' % auth_token}

      # Send a request (with the authentication headers) to fetch all executions in a project
      # You can get the project ID for example
      resp = requests.get('https://app.valohai.com/api/v0/executions/?project={project_id}', headers=headers)

      # To fetch all failed executions you could run
      # https://app.valohai.com/api/v0/executions/?project={project_id}&status=error

      resp.raise_for_status()

      # Print the response you've received back
      print('# API Response:\n')
      print(json.dumps(resp.json(), indent=4))

  ..
* Save and run ``python fetchExecutions.py`` and you'll see a list of executions with their details.
