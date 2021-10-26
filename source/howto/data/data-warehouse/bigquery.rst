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

* Go to your GCP Project's `IAM -> Service Accounts <https://console.cloud.google.com/iam-admin/serviceaccounts>`_
* Create a new a service account
* Give the service account ``BigQuery User`` permissions.

Share the email of the service account with Valohai with the information on which environments you'd like to attach this service account to. Each Valohai environment can be configured to use a different service account. 

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
