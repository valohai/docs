You can connect :doc:`private data stores </core-concepts/data-stores>` to Valohai projects.

If you connect a store that contains files that Valohai doesn't know about,
like the files that you have uploaded there yourself, you can use the following syntax to refer to the files.

* Azure Blob Storage: ``azure://{account_name}/{container_name}/{blob_name}``
* Google Storage: ``gs://{bucket}/{key}``
* Amazon S3: ``s3://{bucket}/{key}``
* OpenStack Swift: ``swift://{project}/{container}/{key}``

This syntax also has supports wildcard syntax to download multiple files:

* ``s3://my-bucket/dataset/images/*.jpg`` for all .jpg (JPEG) files
* ``s3://my-bucket/dataset/image-sets/**.jpg`` for recursing subdirectories for all .jpg (JPEG) files
