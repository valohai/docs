.. meta::
    :description: Everything in Valohai deep learning platform works through an API. Learn how to setup and optimize deep learning experiments with direct calls to our RESTful API.

Quick Start - Valohai API
-------------------------

In this tutorial, we will use the Valohai API to login and fetch a list of projects
associated with the user account.

1. Prerequisites
~~~~~~~~~~~~~~~~

You can use any programming language you want to make HTTP requests.

In this tutorial we will be using Python 3 (version 3.4+ recommended).
Installing Python and Pip is outside the scope of this tutorial, but
a good place for information is `docs.python-guide.org <https://docs.python-guide.org/>`_

To validate your enviroment, open a terminal and run:

.. code-block:: bash

    $ python --version


We also need to install the ``requests`` library to make HTTP requests:

.. code-block:: bash

    $ pip install requests

2. Sign in
~~~~~~~~~~

If you don't already have an account, sign up at `the Valohai platform <https://app.valohai.com/>`_.

Also, create an example project if you don't have one.

3. Authentication Token
~~~~~~~~~~~~~~~~~~~~~~~

To make API requests, you need to authenticate yourself.

In the Valohai API, first you request a token using your username and password.
Then you use that token for all following requests.

Here is a Python script for getting a token:

.. code-block:: python

    import requests

    login_url = 'https://app.valohai.com/api/v0/get-token/'
    data = {'username': 'test', 'password': 'test'}

    resp = requests.post(login_url, data=data)
    resp.raise_for_status()  # Raise an exception for unsuccessful request
    auth_token = req.json()['token']

    print('# My auth token is:', auth_token)

Save the code as ``test.py`` and run the following shell command:

.. code-block:: bash

    $ python test.py
    # My auth token is: Alb3r7o5t1F460TiN&TOERaEy77iBuh6uw4NM3L0d14n

Take a note of the authentication token.
In a real application, you might want to save it in a configuration file or a database.

4. Make an API request
~~~~~~~~~~~~~~~~~~~~~~

Let's take the above code and extend it with another request.

We shall fetch a list of all projects accessible from this user account.

.. note::
    We added ``import json`` for nicer output.

.. code-block:: python

    import requests
    import json

    auth_token = '<insert your authentication token from above here>'
    headers = {'Authorization': 'Token %s' % auth_token}

    resp = requests.get('https://app.valohai.com/api/v0/projects/', headers=headers)
    resp.raise_for_status()

    print('# API Response:\n')
    print(json.dumps(req.json(), indent=4))

Save the code as ``test.py`` and run it again:

.. code-block:: bash

    $ python test.py
    # API Response:
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

This is the raw JSON. Next step is to parse it using your favorite parser
and use the data to for amazing things!

The rest of the API is documented here:

* `<https://app.valohai.com/api/v0>`_
* `<https://app.valohai.com/api/docs/>`_
