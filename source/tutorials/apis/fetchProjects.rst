.. meta::
    :description: Learn how to use Valohai APIs to automate fetch all your projects

Fetch your projects with Valohai APIs
===============================================

.. include:: _useAPIsbasic.rst

* Create a new file called ``fetchVHProjects.py``
    .. code:: Python

      import requests
      import json

      # Authenticate yourself with the token
      auth_token = '<your-auth-token>'
      headers = {'Authorization': 'Token %s' % auth_token}

      # Send a request (with the authentication headers) to fetch Valohai projects
      resp = requests.get('https://app.valohai.com/api/v0/projects/', headers=headers)
      resp.raise_for_status()

      # Print the response you've received back
      print('# API Response:\n')
      print(json.dumps(resp.json(), indent=4))

  ..
* 🔥 Save the code and run ``python fetchVHProjects.py`` to get your results (ID, name, execution count, owner, queued executions etc.)
