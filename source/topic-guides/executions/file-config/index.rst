.. meta::
    :description: If you wish to parse runtime configuration from files instead of command-line parameters, use /valohai/config.

File-based Configuration
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
        "valohai.creator-id": 3,
        "valohai.creator-name": "ruksi",
        "valohai.execution-counter": 92,
        "valohai.execution-ctime": "2019-06-24T08:11:35.700911+00:00",
        "valohai.execution-id": "016b888a-5592-17d2-b3b0-c343f919e739",
        "valohai.execution-qtime": "2019-06-24T08:11:35.700911+00:00",
        "valohai.execution-step": "Train",
        "valohai.pipeline-counter": null,
        "valohai.pipeline-id": null,
        "valohai.pipeline-node-id": null,
        "valohai.project-id": "0169386e-bf30-a59e-7561-fabc2bcf026c",
        "valohai.project-name": "illuminati/great-tensorflow",
        "valohai.task-counter": null,
        "valohai.task-id": null
    }

``/valohai/config/execution.yaml``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    valohai.creator-id: 3
    valohai.creator-name: ruksi
    valohai.execution-counter: 94
    valohai.execution-ctime: '2019-06-24T08:12:58.527200+00:00'
    valohai.execution-id: 016b888b-991c-43e0-6220-fd07d43aa440
    valohai.execution-qtime: '2019-06-24T08:12:58.527200+00:00'
    valohai.execution-step: Train
    valohai.pipeline-counter: null
    valohai.pipeline-id: null
    valohai.pipeline-node-id: null
    valohai.project-id: 0169386e-bf30-a59e-7561-fabc2bcf026c
    valohai.project-name: illuminati/great-tensorflow
    valohai.task-counter: null
    valohai.task-id: null

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
