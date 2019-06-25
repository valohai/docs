.. meta::
    :description: If you want to save results from an execution, store your files in /valohai/outputs and they are automatically uploaded.

Uploading Outputs
=================

At the end of an execution, anything stored in the ``/valohai/outputs`` directory will be uploaded
to your configured data store.
This is the place to store your neural network weights and biases if you want to access them later.

All other files and processes are destroyed at the end of an execution.

**Valohai output uploads never overwrite data.**
You can upload multiple files with the same name and they will be stored separately in the selected data store.
Although it might sometimes be wise to add timestamps to your files, depending on your use-case.

Each uploaded file will get a datum identifier which looks like this:

.. code::

    datum://016b8e3f-f22c-c0ac-b2fc-4cb7a40b8258

This is unique to that file alone and you can use that identifier to select that particular file as input
for future executions.

.. thumbnail:: /datum-url-button.jpg
   :alt: Where to find datum URL with identifier.

    You can use datum URLs to download specific files.
