.. meta::
    :description: In this guide you'll learn to use your own cloud storage (AWS, Azure, GCP, OpenStack) together with Valohai.

.. _cloud-storage:

Add a cloud data store
---------------------------------

A data store is a secure place to keep your files; you download training data from there and upload your trained models and other artefacts there.

.. toctree::
    :maxdepth: 1
    :titlesonly:

    private-azure-storage/index
    private-gcp-bucket/index
    private-s3-bucket/index
    private-swift-container/index

..

.. admonition:: Default data stores
    :class: tip

    * The organization admin can set a default data store for all new projects under organization settings.
    * Each project owner can define their own default data store under project settings.

..

.. seealso::

    * `Downloading files to executions <https://docs.valohai.com/topic-guides/executions/inputs/>`_
    * `Uploading files from executions <https://docs.valohai.com/topic-guides/executions/outputs/>`_
    * `step.inputs <https://docs.valohai.com/reference-guides/valohai-yaml/step-inputs/index.html>`_

..
