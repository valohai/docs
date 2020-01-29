.. meta::
    :description: The inputs section defines the data files for your execution.

``step.inputs``
===============

``inputs`` are the data files that are available during step execution.

An input in ``inputs`` has three potential properties:

* ``name``: The input name; this is shown on the user interface and names the directory where the input files
  will be placed during execution like ``/valohai/inputs/my-input-name``.
* ``default``: **(optional)** The default source where the input will be fetched from.
  If not defined, the user has to define the source at the start of the execution.
* ``optional``: **(optional)** Marks that this input is optional and an URL definition is not
  necessary before execution of the step.

Currently valid sources for inputs are HTTP, HTTPS and various cloud provider specific data
stores such as AWS S3 (``s3://...``) and Azure Storage (``azure://...``).

.. seealso::

    Read more about custom data stores from :doc:`/core-concepts/data-stores` documentation page.

For these HTTP/S endpoints basic access authentication is supported, but for the cloud provider stores,
the access credentials must be configured under project settings.

During the step execution, inputs are available under ``/valohai/inputs/<input name>/<input file>``.
To see this in action, try running ``ls -la /valohai/inputs/`` as the main command of execution which has inputs.

.. tip::

   You can download any files you want during the execution with e.g. Python libraries or command-line tools
   but then your executions become slower as it circumvents our input file caching system.

When you specify the actual input or default for one, you have 3 options:

Option #1: Custom Store URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /_partials/_input-custom-store-url.rst

Option #2: Datum URI
~~~~~~~~~~~~~~~~~~~~

.. include:: /_partials/_input-datum-uri.rst

Option #3: Public HTTP(S) URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /_partials/_input-http.rst
