.. meta::
    :description: Executions can automatically download inputs from various data sources like AWS S3, Azure Blob Storage or custom databases.

Downloading Files to Executions
===============================

You frequently have changing files like training samples/labels or pretrained models you want to use during
your executions. I mean, what would you otherwise operate on.

You can either:

1. **download the files manually yourself using the tools you want**;
   we don't recommend this but might be easy way to get started if you've already mastered them
2. **use Valohai's input mechanism**
   to leverage our automatic record keeping, version control, reproducibility and caching features

This section covers Valohai's input concept in more detail.

For a file to be usable by an execution, you first have to upload it to :doc:`a data stores </topic-guides/core-concepts/data-stores>`
connected to the project either manually or by using our web user interface upload utility.

Here is how to upload files using the web user interface after the data store has been configured:

   .. thumbnail:: uploading-files-web.png
      :alt: Showing how to upload file with the web user interface.

      You can upload files to connected data stores using the web user interface.

During an execution, Valohai inputs are available under ``/valohai/inputs/<INPUT_NAME>/<INPUT_FILE_NAME>``.
To see this in action, try running ``ls -laR /valohai/inputs/`` as the main command of an execution which has inputs.

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
