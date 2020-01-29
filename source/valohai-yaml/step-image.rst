.. meta::
    :description: The image section lets you decide which Docker container to run your code within.

``step.image``
~~~~~~~~~~~~~~

Your code will be run inside a Docker container based on the defined Docker ``image``.

The Docker image should preferably contain all dependencies you need, to ensure your runs can get to work
as quickly as possible.

.. tip::

   You can run dependency installation commands as part of your ``command`` but it will result in slower
   computation time as then each execution starts by dependency setup, which is sub-optimal but nevertheless
   a good staring point.

You can find Docker images for the most popular machine learning libraries on
`Docker Hub <https://hub.docker.com/>`_.

You can also create and host your images on `Docker Hub <https://hub.docker.com/>`_ or any other Docker repository.

.. include:: /_partials/_image-list.rst
