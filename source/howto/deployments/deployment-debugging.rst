.. meta::
    :description: How to inspect and debug Valohai endpoints.

.. _howto-deployment-debugging:

Debugging failing deployments
##########################################

.. include:: _deployment-introduction.rst

..

The most straightforward way of debugging is using the endpoint logs. If the error was in the code runtime, the logs should show a stack trace or an error message but this depends on the programming language and libraries used.

You can also print additional details yourself to keep track how the code is progressing.

But sometimes logging doesn't contain enough information about the surrounding infrastructure.

Valohai deployment endpoints report their internal state under the ``Cluster Status`` tab. These more advanced details can give hints why the endpoint might be failing, for example if the previous container state reads ``OOMKilled``, the endpoint was taking more memory than it requested and it was killed by the Kubernetes cluster.

It's recommended to increase your endpoint replica count on the version endpoint listing if you want to make your endpoint less prone to become unavailable. This effectively means there will be more web servers running and one of them crashing doesn't make the whole endpoint unresponsive.

.. thumbnail:: cluster-status-oom.png
   :alt: Cluster status a handy way to see more technical details of the endpoint.
