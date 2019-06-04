.. meta::
    :description: You can define which files to be downloaded from various data sources when using Valohai CLI.

Inputs with Valohai CLI
=======================

Let's assume we have something similar to the following set up in Valohai YAML:

.. code-block:: yaml

    - step:
      # ...
      name: train-model
      # ...
      inputs:
        - name: training-set-images
        - name: training-set-labels

And you have a local project linked to Valohai, then you can run the step with the following.

.. code-block:: bash

    $ vh exec run train-model

But this will crash because the inputs aren't defined.

So, how can you refer to various datasets?

Option #1: Custom Store URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Usage example:

.. code-block:: bash

    $ vh exec run train-model \
        --training-set-images=s3://my-bucket/dataset/images/train.zip \
        --training-set-labels=s3://my-bucket/dataset/labels/train.zip

Option #2: Datum URL
~~~~~~~~~~~~~~~~~~~~

You can use the ``datum://<identifier>`` syntax to refer to specific files Valohai platform already knows about.

Files will have a datum URL if the files were uploaded to Valohai either:

1) as outputs from another execution
2) or using the Valohai web interface uploader under "Data" tab of the project

You can find the datum URL by clicking the "datum://" button under "Data" tab of the project.

.. thumbnail:: datum-url-button.jpg
   :alt: Where to find datum URL with identifier.

    You can use datum URLs to download specific files.

Usage example:

.. code-block:: bash

    $ vh exec run train-model \
        --training-set-images=datum://01685ff1-5a7a-c36b-e79e-80623acea29f \
        --training-set-labels=datum://01685ff1-5930-8c09-83d1-cd174c9770ab

Option #3: Public HTTP(S) URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your dataset is public and available through an HTTP(S) address, you can use that.

Usage example:

.. code-block:: bash

    $ vh exec run train-model \
        --training-set-images=https://example.com/train-images.zip \
        --training-set-labels=https://example.com/train-labels.zip
