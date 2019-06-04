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

.. include:: /_input-custom-store-url.rst

Usage example:

.. code-block:: bash

    $ vh exec run train-model \
        --training-set-images=s3://my-bucket/dataset/images/train.zip \
        --training-set-labels=s3://my-bucket/dataset/labels/train.zip

Option #2: Datum URI
~~~~~~~~~~~~~~~~~~~~

.. include:: /_input-datum-uri.rst

Usage example:

.. code-block:: bash

    $ vh exec run train-model \
        --training-set-images=datum://01685ff1-5a7a-c36b-e79e-80623acea29f \
        --training-set-labels=datum://01685ff1-5930-8c09-83d1-cd174c9770ab

Option #3: Public HTTP(S) URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /_input-http.rst

Usage example:

.. code-block:: bash

    $ vh exec run train-model \
        --training-set-images=https://example.com/train-images.zip \
        --training-set-labels=https://example.com/train-labels.zip
