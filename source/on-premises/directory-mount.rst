.. meta::
    :description: Mount local directories to minimize data download and upload duration.

Directory Mounts
================

On-premises Valohai Enterprise installation allows users to use **local directory mounts**.

How this technically works is that specified local directories are mounted inside the Valohai execution containers as Docker volumes. This allows reading and writing to the host machine or local network disks.

You define the mounts on per-step basis in :doc:`valohai.yaml</valohai-yaml/index>`:

.. code-block:: yaml

    - step:
        name: mount-example
        image: tensorflow/tensorflow:1.13.1-gpu-py3
        command:
          - ls -la /my-data
        mounts:
          - source: /path/to/directory/outside/container
            destination: /my-data
            readonly: false

You can try this out with:

* ``vh exec run --adhoc mount-example`` (if not committed and pushed)
* ``vh exec run mount-example`` (if committed, pushed and fetched)
