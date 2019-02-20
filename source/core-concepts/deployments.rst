.. meta::
    :description: What are Valohai deployments? Deploy your machine learning models behind a REST API with Valohai.

Deployments
===========

**Deployment** is a versioned collection of one or more HTTPS endpoints that you can call to get your predictions

Each deployment has a deploy target, which is the Kubernetes cluster the service will be served on. This can be configured when creating the deployment and we provide a default Kubernetes cluster for you to try it out.

You can have multiple deployments if you want to run your prediction service on multiple clusters around the world.

Deployment will get an URL ``https://valohai.cloud/<owner-name>/<project-name>/<deployment-name>/`` and various deployment versions and aliases will be accessible under that path.

You can create and manage deployments under ``Deployment`` tab on Valohai web app.

.. tip::

    If you only need non-interactive batch predictions (taking a lot of samples as input and writing predictions into a file), you can just create a step to handle that, take your model/samples as inputs and write your predictions to ``/valohai/outputs``.

    Deployments are mainly required if one of the following is true:

    * you want to get fast predictions on per-sample basis
    * you want to give prediction endpoint access to application that outside of your organization e.g. a customer that doesn't have a Valohai account
