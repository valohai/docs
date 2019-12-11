.. meta::
    :description: Endpoints describe how deployments are accessed.

``endpoint`` from a WSGI definition
===================================

``endpoint`` using WSGI specification, which works with Python servers using WSGI-interface.

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

.. seealso::

    Read more about WSGI on their `website <https://wsgi.readthedocs.io/en/latest/>`_.
