Using the Valohai APIs is rather straightforward, you'll need to create an API token to authenticate your requests and then write your code to send & receive requests.

* Go to your profile setting and `create an authentication token <https://app.valohai.com/auth/tokens/>`_
    * In our sample we'll paste this directly to the file but you should consider saving this token in a configuration file or database for secure storage.
* Consider creating a custom virtual environment for Python before continuing.
    * ``python3 -m virtualenv .venv``
    * ``source .venv/bin/activate``