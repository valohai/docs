.. meta::
    :description: Endpoints describe how deployments are accessed.

``endpoint``
============

Endpoint definitions are used to setup auto-scaling REST endpoints for **real-time** predictions.

.. tip::

    If you are doing batch predictions that could take multiple minutes to run,
    we recommend sticking with normal Valohai executions.

Technically, endpoint creates a group of Docker containers running HTTP servers deployed to a Kubernetes cluster.
You can either use your own Kubernetes cluster or our clusters.

You can have multiple endpoints as a single project can have various inference requirements
for different contexts e.g. various teams working on the project.

The endpoints are defined in the ``valohai.yaml`` file, which specifies the WSGI application to serve.
In the application, the ``SCRIPT_NAME`` environment variable contains the path the application is served under; i.e. something like ``organization/project/deployment/version/endpoint``.
For Python applications, depending on the web framework being used, this prefix might be automatically used when the ``SCRIPT_NAME`` environment variable is present, or you may need to manage it separately.

When using Flask, Django, or FastAPI with the Gunicorn server, things should work without configuration. If you use the ``wsgi: module.app`` configuration within your endpoint configuration, we will automatically set up a Gunicorn WSGI server, so everything should work out of the box.

If you use FastAPI with the Uvicorn server, the environment variable's contents must at the time of writing be added to each route manually.

If you choose to use a server that does not automatically take ``SCRIPT_NAME`` into account, you'll have to do so manually in your URL routes.
For Python apps, the Werkzeug package contains ``DispatchMiddleware``, which is useful for this.
For instance, for a Flask app, you can use it to wrap the Flask WSGI app:

.. code-block:: python

    from flask import Flask
    import os
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    app = Flask(__name__)
    # ...
    app.wsgi_app = DispatcherMiddleware(app.wsgi, {os.environ.get("SCRIPT_NAME", "/"): app.wsgi_app})


.. tip::

    It is optional to use deployment endpoints in Valohai.
    You can also download the trained model and do more complex deployments.
    I would say it is even more common that people have custom deployments but Valohai deployment endpoints are
    especially excellent for quality assurance and testing.

.. seealso::

    Read more about deployments from :doc:`/core-concepts/deployments` documentation page.
