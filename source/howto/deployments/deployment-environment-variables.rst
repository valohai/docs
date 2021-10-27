.. meta::
    :description: How to use environmental variables with your Valohai endpoints.

.. _howto-deployment-environment-variables:

Using environment variables to configure endpoint behavior
######################################################################

.. include:: _deployment-introduction.rst

..

You have two ways to introduce environment variables into the deployment endpoint runtime:

* Inherit the `project's environment variables and secrets </reference-guides/valohai-yaml/step-environment-variables/#project-environment-variables>`_
* Define environment variables for a particular deployment version

Then you can read those values with the library of your choice e.g. ``os.getenv()`` in Python.
