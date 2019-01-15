.. meta::
    :description: Everything in Valohai deep learning platform works through an API. Learn how to setup and optimize deep learning experiments with direct calls to our RESTful API.

Quick Start - Valohai API
---------------------------------

In this tutorial, we will use Valohai API to login and fetch a list of organizations
associated with the user account.

1. Prerequisites
~~~~~~~~~~~~~~~

You can use any programming language you want to make HTTP requests.

In this tutorial we will be using Python 3 (version 3.4+ recommended).
Installing Python and Pip is outside the scope of this tutorial, but
a good place for information is `docs.python-guide.org <https://docs.python-guide.org/>`_

To validate your enviroment, open a terminal and run:

.. code-block:: bash

    $ python --version


We also need to install the `Requests <http://python-requests.org>` library:

.. code-block:: bash

    $ pip install requests

2. Sign in
~~~~~~~~~~

If you don't already have an account, sign up at `the Valohai platform <https://app.valohai.com/>`_.


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
~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's take the above code and extend it with another request.

We shall fetch a list of all organizations accessible from this user account. For most people, the list will only
have one item.

.. note::
    We added ``import json`` for nicer output.

.. code-block:: python

    import requests
    import json

    auth_token = '<insert your authentication token from above here>'
    headers = {'Authorization': 'Token %s' % auth_token}

    req = requests.get(organizations_list_url, headers=headers)
    req.raise_for_status()
    response = json.dumps(req.json(), indent=4)

    print(f'# API Response:\n{response}')

Save the code as ``test.py`` and run it again:

.. code-block:: bash

    $ python test.py
    # My auth token is: JUFyi0Kj9ccJV98mY5I2E7wKc5oWFANhGR5Zdbsk
    # API Response:
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 123,
                "name": "testorg",
                "url": "https://app.valohai.com/api/v0/organizations/123/"
            }
        ]
    }

This is the raw JSON. Next step is to parse it using your favorite parser
and use the data to for amazing things!

The rest of the API is documented here: `<https://app.valohai.com/api/v0>`_
