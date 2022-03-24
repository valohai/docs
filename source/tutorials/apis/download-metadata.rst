.. meta::
    :description: Learn how to use Valohai APIs to download metadata of an execution

Downloading metadata of a single execution
===============================================

.. include:: _use-apis-basic.rst

* You'll need the ID of a single execution to fetch its metadata.
    * You can query for it with Valohai APIs or by going to the browser and navigating inside an execution. You'll see the ID in the url.
* Create a new folder on your computer and inside it create a new file ``fetchMetadata.py``
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
      resp = requests.get('https://app.valohai.com/api/v0/executions/{execution_id}/metadata/', headers=headers)

      resp.raise_for_status()

      # Print the response you've received back
      print('# API Response:\n')
      print(json.dumps(resp.json(), indent=4))
* 🔥 Save and run ``python fetchMetadata.py`` and you'll see the metadata stream of a single execution.
