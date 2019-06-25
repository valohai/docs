.. meta::
    :description: Executions can automatically download inputs from various data sources like AWS S3, Azure Blob Storage or custom databases.

Downloading Inputs
==================

During an execution, inputs are available under ``/valohai/inputs/<input name>/<input file>``.
To see this in action, try running ``ls -la /valohai/inputs/`` as the main command of execution which has inputs.

When you specify the actual input or default for one, you have 3 options:

Option #1: Custom Store URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /_input-custom-store-url.rst

Option #2: Datum URI
~~~~~~~~~~~~~~~~~~~~

.. include:: /_input-datum-uri.rst

Option #3: Public HTTP(S) URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /_input-http.rst
