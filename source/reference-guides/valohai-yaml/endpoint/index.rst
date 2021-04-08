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

.. tip::

    It's optional to use Valohai deployments. You can also choose to download the trained models and deploy to your own existing environment, if you want more control over the deployments and integrate to existing. Check out Valohai APIs to understand how to automate this.

.. seealso::

    Read more about deployments from :doc:`/topic-guides/core-concepts/deployments` documentation page.

Deployment prefix
-----------------

The ``VH_DEFAULT_PREFIX`` environment variable contains the **default** prefix the application is served under; i.e. something like ``organization/project/deployment/version/endpoint``. This will *not* take into account any deployment aliases.

The WSGI/HTTP application will also receive a ``X-VH-Prefix`` HTTP header containing the root path the application is served under regardless of whether it's being served via the default version moniker or an alias; i.e. something like ``organization/project/deployment/versionalias/endpoint``.

If you use path-based routing (as opposed to e.g. RPC style) in your deployment code, you may need to use this header or variable to properly route your requests. (Another option is to simply allow any prefix for all of your app's routes, e.g. ``^.*/foo/$``).

.. seealso::

    `Examples on how to handle Valohai deployment prefixes using common frameworks. <https://github.com/valohai/deployment-prefixes>`_

..
