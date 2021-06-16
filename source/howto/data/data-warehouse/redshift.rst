.. meta::
    :description: This how to guide shows you how to authenticate and run queries on Amazon RedShift.

.. _howto-data-redshift:

Access Redshift from an execution
################################################

.. admonition:: Prequirements
    :class: warning

    This guide assumes that you've:

    * already created a Redshift cluster and have your data imported
    * reviewed the clusters security group to allow connections from the security group ``valohai-sg-workers`` 

You can access Amazon Redshift from your Valohai executions to run queries.


Option 1) Allow ``ValohaiWorkerRole`` role to access your 
-------------------------------------------------------------------

Your AWS account has a IAM Role ``ValohaiWorkerRole``. This role is assigned to all EC2 instances that Valohai spins up to execute machine learning jobs.

You can edit the permissions of that role inside your AWS subscription to give it access for Redshift.


.. code-block:: json

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "redshift:GetClusterCredentials",
                "Resource": [
                    "arn:aws:redshift:<region>:<account-ID>:dbuser:<cluster-identifier>/<username>",
                    "arn:aws:redshift:*:<account-ID>:dbgroup:*/*",
                    "arn:aws:redshift:<region>:<account-ID>:dbname:<cluster-identifier>/<database>"
                ]
            }
        ]
    }

..

.. tip::

    You can create multiple roles and have Valohai environments that are connected to different roles.
    
    For example creating a ``ValohaiWorkerRole-Redshift`` that will be used only by certain Valohai environments, and those can be restricted to only certain teams in your Valohai organization.

..

You can use for example `redshift_connector <https://github.com/aws/amazon-redshift-python-driver>`_  connect to Redshift from your execution.

Here's a simple example:

.. code-block:: python

    import redshift_connector
    import requests
    import json

    # Fetch credentials from the machines ValohaiWorkerRole
    aws_metadata_ip = '169.254.169.254'
    response = requests.get(f'http://{aws_metadata_ip}/latest/meta-data/iam/security-credentials/ValohaiWorkerRole')

    # Parse the JSON results
    credentials = json.loads(response.text)

    # Fill in your details to these variables

    host = '<cluster-identifier>.xxxxxxxxx.xx-xxxx-x.redshift.amazonaws.com'
    database = 'XXX'
    db_user = 'XXX'
    cluster_identifier = '<cluster-identifier>',

    # Connect to Redshift cluster using AWS credentials
    conn = redshift_connector.connect(
        iam=True,
        host=host,
        database=database,
        db_user=db_user,
        user='',
        password='',
        cluster_identifier=cluster_identifier,
        access_key_id=credentials["AccessKeyId"],
        secret_access_key=credentials["SecretAccessKey"],
        session_token=credentials["Token"],
        region='<region>'
    )

.. important::
    
    Make sure you include ``redshift_connector`` in your Docker image or run ``pip install redshift_connector`` in your ``step.command``.


Option 2) Store your credentials in Valohai
-------------------------------------------------------------------
    
You can authenticate to your Redshift database using a username and password combination. 

Start by setting up the connection details as environment variables:

* Open your project at `app.valohai.com <https://app.valohai.com>`_
* Go to project **settings** and open the **Env Variables** tab
* Create the following environment variables

.. list-table::
    :widths: 20 65 15
    :header-rows: 1

    * - Name
      - Value
      - Secret
    * - dbname
      - The name of your database
      - 
    * - redshift_host
      - e.g. ``redshift-valohai-sample.xxxxxxxxx.xx-xxxx-x.redshift.amazonaws.com``
      - 
    * - port
      - Which port are you connecting to? For example 5439.
      - 
    * - user
      - Username that can run operations in your Redshift database
      - 
    * - PGPASSWORD
      - Password of the user
      - Secret

These environment variables will be now available for all executions that are ran inside this project.

Below two examples showing you how to access the environment variables during a Valohai execution.

.. tab:: Using psycopg2

    Make sure you have psycopg2 in your Docker image, or install it with ``pip install psycopg2`` in your ``step.command`` before running your script.

    .. code-block:: python

        import psycopg2

        con= psycopg2.connect(
            dbname= os.getenv('dbname'),
            host = os.getenv('redshift_host',
            port = os.getenv('port'),
            user = os.getenv('user'),
            password = os.getenv('PGPASSWORD')
        )

    ..

.. tab:: Using psql

    You can run ``psql`` directly in the ``step.command`` your Docker image has it installed.

    The code below will execute the query from ``query.sql`` (which is a part of the repository) and then output the results as a csv file to Valohai outputs.

    .. code-block:: yaml

      - step:
          name: Output from Redshift
          image: myorg/redshift-image:latest
          command:
            - psql -h $redshift_host -d $dbname -U $user -p $port -A -f query.sql -F ',' -o /valohai/outputs/redshift_output.csv



.. admonition:: Maintaining reproducability
    :class: tip

    As your data lives and changes in Amazon Redshift so will your query results. Running a query today will return a certain query result but running the same query next week might return a different result.
    
    It's strongly recomended that you save the query result, or a preprocessed dataset, to ``/valohai/outputs/`` to keep a snapshot of the exact query result before you run any trainings with that data.

    For example your pipeline could look like the one below:

    1. Fetch data from Amazon Redshift and preprocess the data. Save the preprocessed data to ``/valohai/outputs`` so it gets saved to Amazon S3.
    2. Use the preprocessed data from Amazon S3 for any further trainings.

    If you then in the future need to reproduce that training, or inspect what's the actual data that your model was trained on, you can easily rerun it on Valohai or download the dataset instead of relying on the query result of that day.

