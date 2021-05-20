.. meta::
    :description: Everything in Valohai deep learning platform works through an API. Learn how to setup and optimize deep learning experiments with direct calls to our RESTful API.

Valohai API Tutorial
####################################

In this tutorial, we will use the Valohai API to login and fetch a list of projects.

.. admonition:: Prerequirements
    :class: attention

    You can use any programming language you want to make HTTP requests.

    In this tutorial we will be using Python 3 (version 3.4+ recommended).
    Installing Python and Pip is outside the scope of this tutorial, but a good place for information is `docs.python-guide.org <https://docs.python-guide.org/>`_

    To validate your enviroment, open a terminal and run:

    .. code:: bash

        python --version
    ..

    We also need to install the ``requests`` library to make HTTP requests:

    .. code-block:: bash

        pip install requests


Get an authentication token
---------------------------------

* Sign in at `app.valohai.com <https://app.valohai.com/>`_.
* Create a new example project
* `Create an auth token <https://app.valohai.com/auth/tokens/>`_ to use when calling Valohai API.

.. admonition:: Store your token in a secure location
    :class: warning

    The generated token is personal and it gives you access to Valohai features through your account. You might want to save the token in a configuration file or a database.

    Don't include it directly in your version controlled files.

.. figure:: /_images/get_auth_token.gif
   :alt: Getting auth token from the Valohai UI.


Make an API request
---------------------------------

Let's take the above code and extend it with another request.

We will fetch a list of all projects accessible from this user account.

.. code-block:: python

    import requests
    import json

    auth_token = '<insert your authentication token from step 3 here>'
    headers = {'Authorization': 'Token %s' % auth_token}

    resp = requests.get('https://app.valohai.com/api/v0/projects/', headers=headers)
    resp.raise_for_status()

    print(json.dumps(resp.json(), indent=4))

Save the code as ``test.py`` and run it again with ``python test.py``.

You should get a response like the one below:

.. code-block:: json

    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": "015f25c1-0101-1010-fefe-a0a0a0a0a0a0",
                "name": "my-project",
                "description": "",
                "owner": {
                    "id": 1337,
                    "username": "myusername"
                },
                "ctime": "2017-10-16T15:16:19.230872Z",
                "mtime": "2017-10-16T15:16:19.230895Z",
                "url": "https://app.valohai.com/api/v0/projects/015f25c1-0101-1010-fefe-a0a0a0a0a0a0/",
                "urls": {
                    "display": "https://app.valohai.com/p/myusername/my-project/",
                    "display_repository": "https://app.valohai.com/p/myusername/my-project/settings/repository/"
                },
                "execution_count": 0,
                "last_execution_ctime": null
            }
        ]
    }

Next steps
-----------

Next step is to parse it using your favorite parser and use the data to for amazing things!

The rest of the API is documented here, you must be logged in to read them:

* `<https://app.valohai.com/api/v0>`_
* `<https://app.valohai.com/api/docs/>`_
