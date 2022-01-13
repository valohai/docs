.. meta::
    :description: If you wish to parse runtime configuration from files instead of command-line parameters, use /valohai/config.

File-based configuration
========================

File-based configuration is an alternative to placeholder-based execution configuration.

The following six config files will always be found at ``/valohai/config``:

* ``/valohai/config/execution.json``: Valohai specifics like project and creator in JSON.
* ``/valohai/config/execution.yaml``: Valohai specifics like project and creator in YAML.
* ``/valohai/config/inputs.json``: Lists all downloaded inputs in JSON.
* ``/valohai/config/inputs.yaml``: Lists all downloaded inputs in YAML.
* ``/valohai/config/parameters.json``: Defined parameter values in JSON.
* ``/valohai/config/parameters.yaml``: Defined parameter values in YAML.

It is common to use these in the following manner:

.. code-block:: bash

    python train.py \
        --parameters-file="/valohai/config/parameters.json" \
        --inputs-file="/valohai/config/inputs.json"

This makes it easy to run the same code in a non-Valohai environment or if you prefer parsing a configuration file
over parsing command-line arguments.

**The rest of the page contains examples what the configuration files will look like.**

``/valohai/config/execution.json``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
        "valohai.commit-identifier": "<commit-id>",
        "valohai.creator-id": <creator-id>,
        "valohai.creator-name": "<creator-username>",
        "valohai.environment-id": "<environmet-id>",
        "valohai.environment-name": "<environment-name>",
        "valohai.environment-slug": "<environment-slug>",
        "valohai.execution-counter": <execution-counter>,
        "valohai.execution-ctime": "<execution-ctime>",
        "valohai.execution-duration": <execution-duration>,
        "valohai.execution-id": "<execution-id>",
        "valohai.execution-image": "<execution-image>",
        "valohai.execution-qtime": <execution-queue-time>,
        "valohai.execution-status": "created",
        "valohai.execution-step": "<step-name>",
        "valohai.execution-tags": [],
        "valohai.execution-title": None,
        "valohai.pipeline-counter": <pipeline-counter>,
        "valohai.pipeline-id": "<pipeline-id>",
        "valohai.pipeline-node-id": "<pipeline-node-id>",
        "valohai.pipeline-tags": [],
        "valohai.pipeline-title": "<pipeline-name>",
        "valohai.project-id": "<project-id>",
        "valohai.project-name": "<project-owner/project-name>",
        "valohai.task-counter": <task-counter>,
        "valohai.task-id": "<task-id>

    }

``/valohai/config/execution.yaml``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    valohai.commit-identifier: <commit-id>,
    valohai.creator-id: <creator-id>,
    valohai.creator-name: <creator-username>,
    valohai.environment-id: <environmet-id>,
    valohai.environment-name: <environment-name>,
    valohai.environment-slug: <environment-slug>,
    valohai.execution-counter: <execution-counter>,
    valohai.execution-ctime: <execution-ctime>,
    valohai.execution-duration: <execution-duration>,
    valohai.execution-id: <execution-id>,
    valohai.execution-image: <execution-image>,
    valohai.execution-qtime: <execution-queue-time>,
    valohai.execution-status: created,
    valohai.execution-step: <step-name>,
    valohai.execution-tags: [],
    valohai.execution-title: None,
    valohai.pipeline-counter: <pipeline-counter>,
    valohai.pipeline-id: <pipeline-id>,
    valohai.pipeline-node-id: <pipeline-node-id>,
    valohai.pipeline-tags: [],
    valohai.pipeline-title: <pipeline-name>,
    valohai.project-id: <project-id>,
    valohai.project-name: <project-owner/project-name>,
    valohai.task-counter: <task-counter>,
    valohai.task-id: <task-id>

``/valohai/config/inputs.json``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Inputs file is a mapping from ``<input-name>`` to a ``files`` array.
* ``size`` on input files is in bytes so 1.6 MB and 4.5 kB on the following two files.
* ``uri`` will be a datum identifier if not a HTTP(S) file e.g. ``datum://016b8893-047a-b24a-a200-c1331f825cef``

.. code-block:: json

    {
      "dataset-images": {
        "files": [
          {
            "name": "t10k-images-idx3-ubyte.gz",
            "path": "/valohai/inputs/dataset-images/t10k-images-idx3-ubyte.gz",
            "size": 1648877,
            "uri": "https://valohai-mnist.s3.amazonaws.com/t10k-images-idx3-ubyte.gz",
            "metadata": [
              {
                "mykey": "myvalue",
                "category": "images"
              }
            ],
            "checksums": {
              "md5": "9fb629c4189551a2d022fa330f9573f3",
              "sha1": "c3a25af1f52dad7f726cce8cacb138654b760d48",
              "sha256": "8d422c7b0a1c1c79245a5bcf07fe86e33eeafe..."
            }
          }
        ]
      },
      "dataset-labels": {
        "files": [
          {
            "name": "t10k-labels-idx1-ubyte.gz",
            "path": "/valohai/inputs/dataset-labels/t10k-labels-idx1-ubyte.gz",
            "size": 4542,
            "uri": "https://valohai-mnist.s3.amazonaws.com/t10k-labels-idx1-ubyte.gz",
            "checksums": {
              "md5": "ec29112dd5afa0611ce80d1b7f02629c",
              "sha1": "763e7fa3757d93b0cdec073cef058b2004252c17",
              "sha256": "f7ae60f92e00ec6debd23a6088c31dbd2371ec..."
            }
          }
        ]
      }
    }

``/valohai/config/inputs.yaml``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Inputs file is a mapping from ``<input-name>`` to a ``files`` array.
* ``size`` on input files is in bytes so 1.6 MB and 4.5 kB on the following two files.
* ``uri`` will be a datum identifier if not a HTTP(S) file e.g. ``datum://016b8893-047a-b24a-a200-c1331f825cef``

.. code-block:: yaml

    dataset-images:
      files:
      - name: t10k-images-idx3-ubyte.gz
        path: /valohai/inputs/dataset-images/t10k-images-idx3-ubyte.gz
        uri: https://valohai-mnist.s3.amazonaws.com/t10k-images-idx3-ubyte.gz
        size: 1648877
        checksums:
          md5: 9fb629c4189551a2d022fa330f9573f3
          sha1: c3a25af1f52dad7f726cce8cacb138654b760d48
          sha256: 8d422c7b0a1c1c79245a5bcf07fe86e33eeafee792b84584aec276f5a2dbc4e6
        metadata:
          - mykey: myvalue
            category: images
    dataset-labels:
      files:
      - name: t10k-labels-idx1-ubyte.gz
        path: /valohai/inputs/dataset-labels/t10k-labels-idx1-ubyte.gz
        uri: https://valohai-mnist.s3.amazonaws.com/t10k-labels-idx1-ubyte.gz
        size: 4542
        checksums:
          md5: ec29112dd5afa0611ce80d1b7f02629c
          sha1: 763e7fa3757d93b0cdec073cef058b2004252c17
          sha256: f7ae60f92e00ec6debd23a6088c31dbd2371eca3ffa0defaefb259924204aec6

``/valohai/config/parameters.json``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that these parameters change depending what parameters you have defined in your step.

.. code-block:: json

    {
        "dropout": 0.9,
        "learning_rate": 0.001,
        "max_steps": 300
    }

``/valohai/config/parameters.yaml``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that these parameters change depending what parameters you have defined in your step.

.. code-block:: yaml

    dropout: 0.9
    learning_rate: 0.001
    max_steps: 300
