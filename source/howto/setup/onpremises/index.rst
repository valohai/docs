.. meta::
    :description: How to manually deploy Valohai resources in your GCP environment

.. _onpremises:


Onpremises installation
########################

The "Compute and Data Layer" of Valohai can be deployed to your cloud and/or on-premises environment. This enables you to:

* Use your own on-premises machines to run machine learning jobs
* Use your own cloud storage for storing training artefacts, like trained models, preprocessed datasets, visualizations, etc.
* Mount local data to your on-premises workers
* Access databases and date warehouses directly from the workers, which are inside your network.

Valohai doesn't have direct access to the on-premises machine that executes the machine learning jobs. Instead it communicates with a seperate static virtual machine in your cloud/on-premises that's responsible for storing the job queue, job states, and short-term logs.

.. image:: /_images/valohai_environment.png
    :width: 700
    :alt: Valohai Components


Installing the Valohai worker
-----------------------------

The Valohai agent (Peon) is responsible for fetching new jobs, writing logs, and updating the job states for Valohai.

You'll need to have ``Python 3.6+`` installed on the machines by default. The ``peon-bringup`` (bup) will install other dependencies, like ``docker`` and if needed ``nvidia-docker``.

.. warning::

    Before running the template you'll need the following information from Valohai:

    * ``name`` the queue name that this on-premises machine will use.
    * ``queue-address`` will be assigned for the queue in your subscription.
    * ``redis-password`` that your queue uses. This is usually stored in your cloud providers Secret Manager.
    * ``url`` download URL for the Valohai worker agent.

.. code-block:: bash

    sudo su
    apt-get update -y && apt-get install -y python3 python3-distutils
    
    TEMPDIR=$(mktemp -d)
    pushd $TEMPDIR

    export NAME=<queue-name>
    export QUEUE_ADDRESS=<queue-address>
    export PASSWORD=<redis-password>
    export URL=<bup-url>

    curl $URL --output bup.pex
    chmod u+x bup.pex
    env "CLOUD=none" "ALLOW_MOUNTS=true" "INSTALLATION_TYPE=private-worker" "REDIS_URL=rediss://:$PASSWORD@$QUEUE_ADDRESS:63790"  "QUEUES=$NAME" ./bup.pex

    popd