.. meta::
    :description: Find the most common Docker images currently used in machine learning projects on the platform. It is possible to run any kind of code from C to Python as long as it runs inside a Docker container.

.. _docker:

Docker images
#################################################

Valohai utilizes Docker images to define your runtime environment.
This means that the platform is capable of running any code from C to Python
as long as it can run inside a Docker container.

You can use any Docker image available online.
After getting initial versions working, it makes sense to package your dependencies by
:doc:`building your own images </howto/docker/docker-build-image/>`.

We recommend hosting your images on `Docker Hub <https://hub.docker.com/>`_ as it's the most straight forward
but you can use any Docker registry. You can configure authenticated access under organization settings.

.. include:: /_partials/_image-list.rst

Which images to use depend on your specific use-case, but it usually makes sense to:

* start with as minimal image as possible
* use a specific image tag (the ``:<VERSION>`` part) so everything stays reproducible

.. seealso::

    * :ref:`docker-private-registries`
    * :ref:`docker-build`

.. toctree::
    :titlesonly:
    :maxdepth: 1

    docker-private-registry
    popular-notebook-images
    docker-build-image