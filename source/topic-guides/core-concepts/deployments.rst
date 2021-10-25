.. meta::
    :description: What are Valohai deployments? Deploy your machine learning models behind a REST API with Valohai.

Deployments
############

.. seealso::

    For the technical specifications, go to :doc:`valohai.yaml endpoint section </reference-guides/valohai-yaml/endpoint/index>`.

**A deployment** is a group of versioned web endpoints ran on a Kubernetes cluster for online inference.

After you've specified how your model code is served using your project and :doc:`the valohai.yaml endpoint definitions </reference-guides/valohai-yaml/endpoint/index>`, you can create and manage deployments under ``Deployment`` tab on Valohai web interface.

.. admonition:: Batch predictions
    :class: tip

    If you only need non-interactive batch predictions (taking a lot of samples as input and writing predictions into a file), you can just create a step to handle that, take your model/samples as inputs and write your predictions to ``/valohai/outputs``.

    Valohai Deployments are mainly required if one of the following is true:

    * you want to get fast predictions on per-sample basis
    * you want to give prediction endpoint access to application that outside of your organization e.g. a customer that doesn't have a Valohai account

Deployment Target
-----------------------

Each deployment has **a deployment target**, which is a Kubernetes cluster that the service will be served on. The default deployment target is a shared Kubernetes cluster managed by Valohai but you can also use your own cluster.

You can use multiple deployment targets if you want to run your service in different geolocations.

| Each deployment will be assigned an address in the format:
| ``https://<deployment-target>/<owner>/<project>/<deployment>/``
| ... which translates to the following on the shared Kubernetes cluster:
| ``https://valohai.cloud/<owner>/<project>/<deployment>/``

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

**A deployment endpoint** is one or more Docker containers running HTTP servers in an auto-scaling Kubernetes cluster.

You can have multiple endpoints per deployment version because a single project can have various inference needs for different contexts.

Authentication can be added in various ways but the most common approaches are 1) to use HTTP Basic Auth or 2) restricting the access on the load balancer that is in front of the cluster.

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

Endpoint Testing
---------------------

You can test your endpoint using the **Test Deployment** tool from inside the deployment version page of the Valohai web interface.

This constructs ``POST/GET/PUT`` requests with the instructed payloads. The payloads can plain text, a JSON file or an image, for example.

You'll get the response from your inference service directly in your browser.

Endpoints with Environment Variables
--------------------------------------

You have two ways to introduce environment variables into the deployment endpoint runtime:

* Inherit the `project's environment variables and secrets </reference-guides/valohai-yaml/step-environment-variables/#project-environment-variables>`_
* Define environment variables for a particular deployment version

Deployment Alias
--------------------

**A deployment alias** is a human-readable name that points to a specific deployment version e.g. ``staging`` or ``production``.

Aliases create canonical URLs for development so you can use Valohai to control which version is being served in each context. This allows you to update currently used version or rollback to previous version if something goes wrong.

For example, version alias ``https://valohai.cloud/ruksi/mnist/americas/production/predict-digit`` could be used by applications utilizing your predictions and they don't need to change the URL when you a release new version.

Deployment Monitoring
-------------------------

Under each deployment version, you can view the deployment logs from your deployment endpoints.

You can collect additional metrics from your deployments by printing JSON from your deployment endpoint. Valohai will collect these metrics, and allow you to chart them in both time series and histogram modes.

So we can recognize which outputs you might want to chart out, you must wrap those structures in ``{"vh_metadata": {}}``, something like this:

.. code-block:: python

   import json

   print(json.dumps({"vh_metadata": {"accuracy": 0.9247000813484192, "best_guess": "dog"}}))

In *the most* use-cases, each request would log out one of these metrics log rows, but we don't limit that.

.. thumbnail:: /topic-guides/core-concepts/monitoring.gif
   :alt: Monitoring Valohai Deployments
..
