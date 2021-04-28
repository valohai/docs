.. meta::
    :description: The inputs section defines the data files for your execution.

``step.inputs``
===============

``inputs`` are the data files that are available during step execution.

An input in ``inputs`` has four potential properties:

.. list-table:: 
   :widths: 15 75 10 
   :header-rows: 1

   * - Property
     - Description
     - Optional
   * - ``name``
     - The input name; this is shown on the user interface and names the directory where the input files will be placed during execution like ``/valohai/inputs/my-input-name``.
     - No
   * - ``optional``
     - Marks that this input is optional and an URL definition is not necessary before execution of the step.
     - Yes
   * - ``filename``
     - Set a custom name to the downloaded file.
     - Yes
   * - ``keep-directories``
     -    * ``none``: **(default)** all files are downloaded to ``/valohai/inputs/myinput``
          * ``full``: keeps the full path from the storage root. For example ``s3://special-bucket/foo/bar/**.jpg`` could end up as ``/valohai/inputs/myinput/foo/bar/dataset1/a.jpg``
          * ``suffix``: keeps the suffix from the "wildcard root". For example ``s3://special-bucket/foo/bar/*`` the ``special-bucket/foo/bar/`` would be removed, but any relative path after it would be kept, and you might end up with ``/valohai/inputs/myinput/dataset1/a.jpg``
     - Yes


Currently valid sources for inputs are HTTP(S) and various cloud provider specific data
stores such as AWS S3 (``s3://...``), Azure Storage (``azure://...``), Google Cloud Store (``gs://..``).


.. seealso::

    Read more about custom data stores from :doc:`/topic-guides/core-concepts/data-stores` documentation page.

For these HTTP(S) endpoints basic access authentication is supported, but for the cloud provider stores,
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
