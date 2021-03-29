.. meta::
    :description: Mount local directories to minimize data download and upload duration.

Mounting a Directory
====================

On-premises installations allow users to **mount local directories** during executions.

Specified local directories are mounted inside the Valohai execution containers as Docker volumes.
This allows reading from and writing to the host machine or network disks.

You define the mounts on per-step basis in :doc:`the valohai.yaml</reference-guides/valohai-yaml/index>`:

.. code-block:: yaml

    - step:
        name: mount-example
        image: python:3.6
        command:
          - ls -la /my-data
        mounts:
          - source: /path/to/directory/outside/container
            destination: /my-data
            readonly: false

You can try this out with:

* ``vh exec run --adhoc mount-example`` (if not committed and pushed)
* ``vh exec run mount-example`` (if committed, pushed and fetched)
