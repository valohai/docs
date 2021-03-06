.. meta::
    :description: Everything in Valohai deep learning platform works through an API. Learn how to setup and optimize deep learning experiments with direct calls to our RESTful API.

Quick Start - API Automation
----------------------------

In this tutorial, we will use the Valohai API to login and fetch a list of projects.

.. contents::
   :backlinks: none
   :local:

1. Requirements
~~~~~~~~~~~~~~~

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

3. Get an authentication token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make API requests, you need to authenticate yourself.

Before you can use the Valohai REST API, you need to `create an auth token <https://app.valohai.com/auth/tokens/>`_.

.. figure:: /_images/get_auth_token.gif
   :alt: Getting auth token from the Valohai UI.

You might want to save the token in a configuration file or a database.

4. Make an API request
~~~~~~~~~~~~~~~~~~~~~~

Let's take the above code and extend it with another request.

We shall fetch a list of all projects accessible from this user account.

.. note::
    We added ``import json`` for nicer output.

.. code-block:: python

    import requests
    import json

    auth_token = '<insert your authentication token from step 3 here>'
    headers = {'Authorization': 'Token %s' % auth_token}

    resp = requests.get('https://app.valohai.com/api/v0/projects/', headers=headers)
    resp.raise_for_status()

    print('# API Response:\n')
    print(json.dumps(resp.json(), indent=4))

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

5. Next steps
~~~~~~~~~~~~~

Next step is to parse it using your favorite parser and use the data to for amazing things!

The rest of the API is documented here, you must be logged in to read them:

* `<https://app.valohai.com/api/v0>`_
* `<https://app.valohai.com/api/docs/>`_
