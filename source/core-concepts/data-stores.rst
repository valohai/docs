.. meta::
    :description: What are Valohai data stores? Keep your training data secure and scalable.

Data Stores
===========

Each Valohai project has one or more **data stores**.

A data store is a secure place to keep your files; you download training data from there and upload your trained models to there.

Valohai supports the following data store types:

* AWS S3
* Azure Storage Account
* Google Cloud Storage
* OpenStack Swift

If you don't assing a data store to your project, your files will be uploaded to a Amazon S3 bucket under Valohai account. The bucket is not public so your data is safe with us but we do recommend setting up your own private data store.

In addition to downloading files from data stores, you can also download from any public HTTP(S) address. For private installations, we also provide mount-based data ingestion options.

.. thumbnail:: data-stores.jpg
   :alt: You configure data stores per project-basis on Valohai.

.. seealso::

    * :doc:`/guides/private-s3-bucket/index`
    * :doc:`/guides/private-azure-storage/index`
    * :doc:`/guides/private-gcp-bucket/index`
    * :doc:`/guides/private-swift-container/index`
