.. meta::
    :description: Overview of how you'll read and write data in Valohai

.. _migrate-data:

Input and output data
###########################

.. seealso::

    This how-to is a part of our :ref:`new-user-guide` series.


.. include:: /_partials/_recap-inputs.rst

Read files from ``/valohai/inputs/``
--------------------------------------

Start by configuring inputs to your step in ``valohai.yaml`` and update your code to read the data from Valohai inputs, rather than directly from your cloud storage.

.. tab:: valohai-utils (Python)

    .. code-block:: python

        import valohai

        # Define inputs available for this step and their default location
        # The default location can be overriden when you create a new execution (UI, API or CLI)
        default_inputs = {
            'myinput': 's3://bucket/mydata.csv'
        }

        # Create a step 'train' in valohai.yaml with a set of inputs
        valohai.prepare(step="train", image="tensorflow/tensorflow:2.6.1-gpu", default_inputs=default_inputs)

        # Open the CSV file from Valohai inputs
        with open(valohai.inputs("myinput").path()) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')

    ..

    Generate or update your existing YAML file by running

    .. code-block:: bash

        vh yaml step myfile.py

    ..

    The generated ``valohai.yaml`` configuration file looks like:

.. tab:: Python

    .. code-block:: python

        # Get the location of Valohai inputs directory
        VH_INPUTS_DIR = os.getenv('VH_INPUTS_DIR', '.inputs')

        # Get the path to your individual inputs file
        # e.g. /valohai/inputs/<input-name>/<filename.ext>
        path_to_file = os.path.join(VH_INPUTS_DIR, 'myinput/mydata.csv')

        pd.read_csv(path_to_file)

    ..

    Create a ``valohai.yaml`` configuration file and define your step in it:

.. tab:: R

    .. code-block:: r

        # Get the location of Valohai inputs directory
        vh_inputs_dir <- Sys.getenv("VH_INPUTS_DIR", unset = ".inputs")

        # Get the path to your individual inputs file
        # e.g. /valohai/inputs/<input-name>/<filename.ext>
        path_to_file <- file.path(vh_inputs_dir, "myinput/mydata.csv")

        import_df <- read.csv(path_to_file, stringsAsFactors = F)

    ..

    Create a ``valohai.yaml`` configuration file and define your step in it:
    

.. code-block:: yaml

    - step:
        name: train
        image: tensorflow/tensorflow:2.6.1-gpu
        command: python myfile.py
        inputs:
          - name: myinput
            default: s3://bucket/mydata.csv

..

.. seealso::

    * `Download multiple files to a single input using keep-directories </reference-guides/valohai-yaml/step-inputs/>`_
    * `Add a cloud storage </howto/data/cloud-storage/>`_

.. admonition:: Accessing databases and datawarehouses
    :class: tip

    You can also query data from sources like BigQuery, MongoDB, RedShift, Snowflake, BigTable and other databases and data warehouses. These are not accessed through Valohai inputs but instead you should run your existing code on Valohai to query from these data sources. 
    
    As database contents change over time, we recommend saving the query results as a file in Valohai outputs to make sure there is a snapshot of the query result, and you can later on easily reproduce your jobs with the exact same data.

    * :ref:`howto-data-bigquery`
    * :ref:`howto-data-redshift`

Save files to ``/valohai/outputs/``
---------------------------------------

.. include:: /_partials/_recap-outputs.rst

.. tab:: valohai-utils (Python)

    .. code-block:: python

        import valohai

        out_path = valohai.outputs().path('mydata.csv')
        df.to_csv(out_path)

    ..

.. tab:: Python

    .. code-block:: python

        # Get the location of Valohai outputs directory
        VH_OUTPUTS_DIR = os.getenv('VH_OUTPUTS_DIR', '.outputs')
        
        # Define a filepath in Valohai outputs directory
        # e.g. /valohai/outputs/<filename.ext>
        out_path = os.path.join(VH_OUTPUTS_DIR, 'mydata.csv')
        df.to_csv(out_path)

    ..


.. tab:: R

    .. code-block:: r
        
        # Get the location of Valohai outputs directory
        vh_outputs_path <- Sys.getenv("VH_OUTPUTS_DIR", unset = ".outputs")

        # Define a filepath in Valohai outputs directory
        # e.g. /valohai/outputs/<filename.ext>
        out_path <- file.path(vh_outputs_path, "mydata.csv")
        write.csv(output, file = out_path)
    ..

.. seealso::

    * `Save files from trainings </howto/data/save-files/>`_
    * `Attach tags and metadata to your files </howto/data/tag-files>`_
    * `Upload files mid-execution </topic-guides/executions/live-outputs/>`_
    * `Trace modes and data files </topic-guides/reproducibility.html#trace-models-and-data-files>`_
    * `Mount a network file system (NFS) </howto/data/mount-nfs.html>`_ 

.. hint:: 

    `Read more about valohai-utils </topic-guides/valohai-utils/>`_