.. meta::
    :description: In this guide you'll learn to use your own cloud storage (AWS, Azure, GCP, OpenStack) together with Valohai.

Connect to a cloud storage
----------------------------

You can connect your cloud storage to Valohai, so you can easily fetch files as executions inputs and save your outputs to your private data store. If no data store is defined, Valohai will store the files in the Valohai S3 Managed storage and it will only be assissible by the project members.


.. toctree::
    :maxdepth: 1
    :titlesonly:

    /tutorials/cloud-storage/private-azure-storage/index
    /tutorials/cloud-storage/private-gcp-bucket/index
    /tutorials/cloud-storage/private-s3-bucket/index
    /tutorials/cloud-storage/private-swift-container/index

..

Once you've connected your data store you can set it as the **Default upload store** for each project in *Project->Settings->General*

.. seealso:: 

    * `Downloading files to executions <https://docs.valohai.com/executions/inputs/>`_
    * `Uploading files from executions <https://docs.valohai.com/executions/outputs/?highlight=outputs>`_
    * `step.inputs <https://docs.valohai.com/valohai-yaml/step-inputs/>`_

..