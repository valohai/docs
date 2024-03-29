.. meta::
    :description: Endpoints describe how deployments are accessed.

``endpoint`` from a command
===========================

``endpoint`` using a raw start command that works with any programming language or framework.

* ``name``: name of the deployment endpoint, this will be the final part of the URL
* ``image``: the Docker image that will be used as the deployment environment
* ``server-command``: command that runs a HTTP server
* ``port``: **(optional)** where should Valohai expect to find the web server, defaults to 8000. Note the server must be bound to ``0.0.0.0`` (all interfaces), *not* only ``localhost``.
* ``description``: **(optional)** more detailed human-readable description of the endpoint
* ``files``: **(optional)** files that will be loaded into the image, for example the trained model. The files will be in the same directory as your code, modified by the ``path`` property.

.. code-block:: yaml

    - endpoint:
        name: server-endpoint
        image: python:3.6
        server-command: python run_server.py
        port: 1453
        files:
          - name: model
            description: Model output file from TensorFlow
            path: model.pb

Valohai automatically runs ``pip install --user -r requirements-deployment.txt`` in case you have additional dependencies defined in *requirements-deployment.txt* in your project root.

If you don't have a ``requirements-deployment.txt`` file, Valohai will check if there is a ``requirements.txt`` file and then run ``pip install --user -r requirements.txt`` in your project root.

Commands from installed packages end up in ``~/.local/bin``, following the standards for ``pip --user`` installation.
