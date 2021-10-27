.. meta::
    :description: How to test your Valohai endpoints using endpoint test tool.

.. _howto-deployment-test:

Testing your deployment endpoints
##################################

.. include:: _deployment-introduction.rst

You can test your deployment endpoints directly from the Valohai web app.

* Login to `app.valohai.com <https://app.valohai.com>`_
* Open your project
* Click on your Project's **Deployment** tab
* Select an existing deployment
* Click on the **Test deployment** button
* Select your endpoint from the drop-down
* Add the fields that your endpoint is expecting
* Click on the **Send request** button

Depending on what your endpoint is expecting, you can send it either text or a file e.g. an image.

You'll get the response from your inference service directly in your browser.

.. video:: /_static/videos/test-deployment.mp4
    :autoplay:
    :width: 600
