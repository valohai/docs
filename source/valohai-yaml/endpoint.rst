.. meta::
    :description: Endpoints describe how deployments are accessed.

``endpoint``
============

Endpoint definitions are used to setup auto-scaling REST endpoints for **real-time** predictions.

.. tip::

    If you are doing batch predictions that could take multiple minutes to run,
    we recommend sticking with normal Valohai executions.

Technically, endpoint creates a group of Docker containers running HTTP servers deployed to a Kubernetes cluster.

You can have multiple endpoints as a single project can have various inference requirements
for different contexts e.g. teams working on the project.

.. tip::

    It is fully optional to use deployment endpoints in Valohai.
    You can also download the trained model and do more complex deployments.
    I would say it is even more common that people have custom deployments but Valohai deployment endpoints are
    especially excellent for quality assurance and testing.

.. seealso::

    Read more about deployments from :doc:`/core-concepts/deployments` documentation page.

``endpoint.server-command`` variant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``endpoint`` using a raw start command that works with any programming language or framework.

* ``name``: name of the deployment endpoint, this will be the final part of the URL
* ``image``: the Docker image that will be used as the deployment environment
* ``server-command``: command that runs a HTTP server
* ``port``: **(optional)** where should Valohai expect to find the web server, defaults to 8000
* ``description``: **(optional)** more detailed human-readable description of the endpoint
* ``files``: **(optional)** files that will be loaded into the image, for example the trained model. The files will be in the same directory as your code, modified by the ``path`` property.

.. code-block:: yaml

    - endpoint:
        name: server-endpoint
        image: python:3.6
        port: 1453
        server-command: python run_server.py
        files:
          - name: model
            description: Model output file from TensorFlow
            path: model.pb

``endpoint.wsgi`` variant
~~~~~~~~~~~~~~~~~~~~~~~~~

``endpoint`` using a WSGI specification, which works with Python servers using WSGI-interface.

* ``name``: name of the deployment endpoint, this will be the final part of the URL
* ``image``: the Docker image that will be used as the deployment environment
* ``wsgi``: specifies the WSGI application to serve, specify the module (e.g. ``package.app``) or the module and the WSGI callable (e.g. ``package.app:wsgi_callable``)
* ``description``: **(optional)** more detailed human-readable description of the endpoint
* ``files``: **(optional)** files that will be loaded into the image, for example the trained model. The files will be in the same directory as your code, modified by the ``path`` property.

.. code-block:: yaml

    - endpoint:
        name: wsgi-endpoint
        description: predict digits from image inputs
        image: tensorflow/tensorflow:1.3.0-py3
        wsgi: predict_wsgi:predict_wsgi
        files:
          - name: model
            description: Model output file from TensorFlow
            path: model.pb
