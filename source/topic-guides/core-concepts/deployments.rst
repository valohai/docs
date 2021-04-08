.. meta::
    :description: What are Valohai deployments? Deploy your machine learning models behind a REST API with Valohai.

Deployments
############

.. seealso::

    For the technical specifications, go to :doc:`valohai.yaml endpoint section </reference-guides/valohai-yaml/endpoint/index>`.

**A deployment** is a versioned collection of one or more web endpoints for online inference.

Each deployment has **a deploy target**, which is a Kubernetes cluster the service will be served on. The default deploy target is a shared Kubernetes cluster managed by Valohai but you can also use your own cluster.

You can have multiple deployments if you want to run your service in different geolocations.

You can create and manage deployments under ``Deployment`` tab on Valohai web user interface.

| Each deployment will get an assigned URL:
| ``https://valohai.cloud/<owner>/<project>/<deployment>/``

.. admonition:: Batch predictions
    :class: tip

    If you only need non-interactive batch predictions (taking a lot of samples as input and writing predictions into a file), you can just create a step to handle that, take your model/samples as inputs and write your predictions to ``/valohai/outputs``.

    Valohai Deployments are mainly required if one of the following is true:
    
    * you want to get fast predictions on per-sample basis
    * you want to give prediction endpoint access to application that outside of your organization e.g. a customer that doesn't have a Valohai account

Deployment Version
-----------------------

**A deployment version** is a Docker image that Valohai builds on top of the Docker image you specify in the ``endpoint`` YAML definition. The build image will include 1) your code repository and 2) all files you defined in the YAML file and specified during deployment version creation.

The deployment version is the actual artifact that is served on the target Kubernetes cluster.

| Running deployment versions will be accessible through:
| ``https://valohai.cloud/<owner>/<project>/<deployment>/<version>``
| e.g.
| ``https://valohai.cloud/ruksi/mnist/americas/20181002.0``

Each deployment can have multiple versions at the same time.

Deployment Endpoint
--------------------

An endpoint is a Docker container running a HTTP server in an auto-scaling Kubernetes cluster.

You can have multiple endpoints per deployment version because a single project can have various inference needs for different contexts.

Authentication can be added in various ways but the easiest is to use HTTP Basic Auth.

You define endpoints in the `valohai.yaml`:

.. code-block:: yaml

    - endpoint:
        name: greet-me
        description: Responds with a big hello!
        image: python:3.6
        port: 8000
        server-command: python -m wsgiref.simple_server

    - endpoint:
        name: predict-digit
        description: Predict digits from image inputs ("file" parameter).
        image: gcr.io/tensorflow/tensorflow:1.13.1-py3
        wsgi: predict_wsgi:predict_wsgi
        files:
          - name: model
            description: Model output file from training step.
            path: model.pb

| Note that each endpoint you specified in the YAML file will have separate URL:
| ``https://valohai.cloud/<owner>/<project>/<deployment>/<version>/<endpoint>``
| e.g.
| ``https://valohai.cloud/ruksi/mnist/americas/20181002.0/predict-digit``

Deployment Alias
--------------------

**A deployment version alias** is a human-readable name that points to a specific deployment version e.g. ``staging`` or ``production``.

Aliases create canonical URLs for development so you can use Valohai to control which version is being served in each context. This allows you to update currently used version or rollback to previous version if something goes wrong.

For example, version alias ``https://valohai.cloud/ruksi/mnist/americas/production/predict-digit`` could be used by applications utilizing your predictions and they don't need to change the URL when you a release new version.

Testing an endpoint
---------------------

You can test your endpoint using the **Test deployment** from inside the deployment version and sending a POST/GET/PUT request with a query and/or fields.

A field could be e.g. plain text, a JSON file or an image.

You'll get the response from your inference service directly in your browser.

Environment variables
----------------------

You have two options, when using environment variables in deployments:

* Inherit the `project's environment variables and secrets </reference-guides/valohai-yaml/step-environment-variables/#project-environment-variables>`_
* Define environment variables for a particular deployment version

Deployment monitoring
-------------------------

Under each deployment version, you can view the deployment logs from your deployment endpoints.

You can collect additional metrics from your deployments by printing JSON from your deployment endpoint. Valohai will collect these metrics, and allow you to chart them in both time series and histogram modes.

.. thumbnail:: /topic-guides/core-concepts/monitoring.gif
   :alt: Monitoring Valohai Deployments
..
