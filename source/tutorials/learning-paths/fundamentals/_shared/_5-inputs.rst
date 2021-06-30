
.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`learning-paths-fundamentals` series.
..

By defining inputs you can easily download data from a public address or your private cloud storage. 

In this section you will learn:

- How to define Valohai inputs
- How to change inputs between executions both in the CLI and in the UI

.. admonition:: A short introduction inputs
    :class: tip

    * Valohai inputs can be from a public location (HTTP/HTTPS) or from your private cloud storage (AWS S3, Azure Storage, GCP Cloud Storage, OpenStack Swift)
    * The input values you define in your code are default values. You can replace any defined inputs file(s) when creating an execution from the UI, command-line or API.
    * All inputs are downloaded and available during an execution to ``/valohai/inputs/<input-name>/``
    * An input value can be a single file (e.g. ``myimages.tar.gz``) or you can use a wildcard to download multiple files from a private cloud storage (e.g. ``s3://mybucket/images/*.jpeg``)
    * You can interpolate parameter values into input URIs with the syntax ``s3://mybucket/images/{parameter:myparam}/**.jpeg``. This is of particular use in tasks, where you can now easily run your execution on multiple variable datasets. 
    * Valohai inputs are cached on the virtual machine.

..
