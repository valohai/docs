.. meta::
    :description: Find the most common Docker images currently used in machine learning projects on the platform. It is possible to run any kind of code from C to Python as long as it runs inside a Docker container.

Docker Images
=============

Valohai utilizes Docker images to define your runtime environment.
This means that the platform is capable of running any code from C to Python
as long as it can run inside a Docker container.

You can use any Docker image available online.
After getting initial versions working, it makes sense to package your dependencies by
:doc:`building your own images </tutorials/build-docker-image/index>`.

We recommend hosting your images on `Docker Hub <https://hub.docker.com/>`_ but you can use any Docker registry.
You can configure authenticated access under organization settings.

.. include:: /_partials/_image-list.rst

Which images to use depend on your specific use-case, but it usually makes sense to:

* start with as minimal image as possible
* use a specific image tag (the ``:<VERSION>`` part) so everything stays reproducible

Access Private Docker Repositories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Organizations can use private repositories from Docker Hub or Azure Container Registry for Valohai executions.

Create an `Access token on Docker Hub <https://docs.docker.com/docker-hub/access-tokens/>`_ or a `service principal for Azure Container Registry <https://docs.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal>`_ to generate credentials that Valohai can use to access your private repository.

1. Login at `<https://app.valohai.com>`_
2. Navigate to ``Hi, <name> (the top right menu) > Manage <organization>``. 
3. Go to *Registries* under the organization controls
4. Add a new entry
5. Insert the name in the format of *docker.io/myusername/** or *myregistry.azurecr.io/**.
6. Use the previously generated credentials as the username and password (Docker username and access token or Azure Service Principal credentials)

To use a private Docker image in your executions specify the image in the step of your ``valohai.yaml`` using the full name like ``docker.io/myusername/name:tag``.