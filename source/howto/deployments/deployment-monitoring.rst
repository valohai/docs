.. meta::
    :description: How monitoring works on Valohai endpoints.

.. _howto-deployment-monitoring:

Monitoring your deployment endpoints
#####################################

.. include:: _deployment-introduction.rst

..

Under each deployment version, you can view the deployment logs from your deployment endpoints.

You can collect additional metrics from your deployments by printing JSON from your deployment endpoint. Valohai will collect these metrics, and allow you to chart them in both time series and histogram modes.

So we can recognize which outputs you might want to chart out, you must wrap those structures in ``{"vh_metadata": {}}``, something like this:

.. code-block:: python

   import json

   print(json.dumps({"vh_metadata": {"accuracy": 0.9247000813484192, "best_guess": "dog"}}))

In *most* use-cases, each request would log out one of these metrics log rows, but we don't limit that.

.. thumbnail:: /topic-guides/core-concepts/monitoring.gif
   :alt: Monitoring Valohai Deployments
..
