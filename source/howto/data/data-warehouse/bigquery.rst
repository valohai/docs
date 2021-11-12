.. meta::
    :description: This how to guide shows you how to authenticate and run queries on BigQuery.

.. _howto-data-bigquery:

Access BigQuery from an execution
#################################

You can access BigQuery from your Valohai executions to run queries.

.. admonition:: Prequirements
    :class: warning

    This guide assumes that you have an existing BigQuery data warehouses with your data.


Create a Service Account
-------------------------

The easiest way to authenticate your Valohai jobs with BigQuery is using a GCP Service Account. 

* Go to your GCP Project that hosts all the Valohai resources
* Navigate to `IAM -> Service Accounts <https://console.cloud.google.com/iam-admin/serviceaccounts>`_
* Create a new a service account
* Give the service account ``BigQuery User`` permissions.

Share the email of the service account with Valohai with the information on which environments you'd like to attach this service account to. Each Valohai environment can be configured to use a different service account. 

.. admonition:: Accessing BigQuery from another GCP Project
    :class: tip

    If your BigQuery data is in a different GCP Project than your Valohai resources, you'll need to go to that project and give the newly created service account ``BigQuery User`` permissions there.

    In this case your service account doesn't need ``BigQuery User`` and ``BigQuery Data Viewer`` permissions in the project where you have just the Valohai resources, but no BigQuery data.


Connect to BigQuery
-------------------

In your code you can use the Python Client for Google BigQuery and directly connect to the BigQuery.
When you launch your Valohai executions, choose the environment that has the service account attached and it will be automatically authenticated with the service account credentials.

.. code-block:: python

    from google.cloud import bigquery

    bqclient = bigquery.Client(project='myproject')

    # Download query results.
    query_string = """
    SELECT
        CONCAT(
            'https://stackoverflow.com/questions/',
            CAST(id as STRING)) as url,
            view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags like '%google-bigquery%'
    ORDER BY view_count DESC
    """

    df = (
        bqclient.query(query=query_string)
        .result()
        .to_dataframe()
    )
    print(df.head())

.. tip::

    You'll need to have the google-cloud-bigquery[bqstorage,pandas] packages run the example above.

    ``pip install --upgrade 'google-cloud-bigquery[bqstorage,pandas]'``
