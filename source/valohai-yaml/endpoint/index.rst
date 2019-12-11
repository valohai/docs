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

.. tip::

    It is optional to use deployment endpoints in Valohai.
    You can also download the trained model and do more complex deployments.
    I would say it is even more common that people have custom deployments but Valohai deployment endpoints are
    especially excellent for quality assurance and testing.

.. seealso::

    Read more about deployments from :doc:`/core-concepts/deployments` documentation page.
