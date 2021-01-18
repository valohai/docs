.. meta::
    :description: How to link your Valohai project and a private Google Cloud Platform bucket containing your data science datasets.

Connecting to Google Cloud Storage
==================================

In this guide, we'll link a private Google Cloud Platform bucket to a Valohai project.

.. contents::
   :backlinks: none
   :local:

.. container:: alert alert-warning

   Data Stores can be either configured on a project-level, or as shared Data Stores across your organization.
   
   This guide will show you how to configure a Data Store for a single project, but you can follow the same steps to configure a shared Data Store under your settings.

..

1. Requirements
~~~~~~~~~~~~~~~

For this tutorial you will need:

* a Google Cloud Platform (GCP) project you can administer
* a Valohai project which to link the bucket to

2. Create the bucket
~~~~~~~~~~~~~~~~~~~~

Skip this step if you already have a bucket.

.. thumbnail:: gcp-bucket-01.png
   :alt: Path to GCP bucket creation

Create a bucket through Google Cloud Platform web console (https://console.cloud.google.com/storage/browser).

.. thumbnail:: gcp-bucket-02.png
   :alt: Main steps of the GCP bucket creation

Recommended configuration for the bucket:

* **Name:** can be anything valid for GCP, here are using ``my-valohai-bucket`` as an example
* **Region:** pick the region that hosts majority of the workers you'll be using to minimize transfer
* **Storage Class:** use *Standard* if you have no further preference
* **Access Control:** *Uniform* (allow only bucket-level permissions)
* **Encryption:** *Google-managed key*
* **Retention Policy:** none
* **Labels:** none

Keep pressing the `Continue` until you've created the bucket.

.. thumbnail:: gcp-bucket-03.png
   :alt: An empty GCP bucket for models and datasets

Now you have an empty bucket that you can use for your data; e.g. training datasets and models.

3. Create a service account
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next, we'll create a new service account using the GCP console.
The service account is effectively "an account" that Valohai workers use to access this particular GCP bucket.

.. thumbnail:: gcp-bucket-04.png
   :alt: Path to service account creation

Navigate to `IAM & admin > Service accounts > Create service account`

.. thumbnail:: gcp-bucket-05.png
   :alt: The first step of service account creation

Name your service account so that you can later remember what it's meant for
(here we are using ``my-valohai-bucket-admin``) and press `Create`.

.. thumbnail:: gcp-bucket-06.png
   :alt: The second step of service account creation

On the next screen, you don't need to add any roles as we will configure more limited access rights later. Just press `Continue`.

.. thumbnail:: gcp-bucket-07.png
   :alt: The last step of service account creation

Press the `Create Key` button and select `JSON` format, this will automatically download a JSON file that we'll be using later.

The resulting JSON file will look something like this:

.. code-block:: json

    {
      "type": "...",
      "project_id": "...",
      "private_key_id": "...",
      "private_key": "...",
      "client_email": "my-valohai-bucket-admin@chubby.iam.gserviceaccount.com",
      "client_id": "...",
      "auth_uri": "...",
      "token_uri": "...",
      "auth_provider_x509_cert_url": "...",
      "client_x509_cert_url": "..."
    }

Also, take a note of the ``client_email`` value, we'll be using that later.

You can later find the service account email in the `Service Accounts` listing:

.. thumbnail:: gcp-bucket-08.png
   :alt: GCP console service account listing including emails

4. Allow access for the new service account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next, we permit the new service account to access files in the bucket.

.. thumbnail:: gcp-bucket-09.png
   :alt: Path to bucket member management

Navigate to *Storage > Browse > "your-bucket" > Permissions > Add member*

.. thumbnail:: gcp-bucket-10.png
   :alt: Adding members to a GCP bucket

1. **New members:** Copy-and-paste the service account email to the field, it will validate it. We got the service account email in the previous section.
2. **Role:** Select `Storage Object Admin`, this allows download and uploading files.
3. Press the `Save` button.

5. Set CORS settings for your bucket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click on "Activate Google Cloud Shell" in the upper right corner.

* Create a new CORS configuration file
   * ``echo '[{"origin": ["*"],"responseHeader": ["Content-Type", "x-ms-*"],"method": ["GET", "HEAD", "OPTIONS"],"maxAgeSeconds": 3600}, {"origin": ["https://app.valohai.com"],"responseHeader": ["Content-Type", "x-ms-*"],"method": ["POST", "PUT"],"maxAgeSeconds": 3600}]' > cors-config.json``

* Update the CORS settings for your bucket 
   * ``gsutil cors set cors-config.json gs://<your-bucket-name>``

* Check the CORS settings
   * ``gsutil cors get gs://<your-bucket-name>``

6. Link the store to Valohai
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: gcp-bucket-valohai-01.png
   :alt: Path to Google Cloud Storage link page

Navigate to `Project > Settings > Data Stores > Add Google Storage`

.. thumbnail:: gcp-bucket-valohai-02.png
   :alt: How to fill fields when creating a Google Cloud Storage on Valohai

1. **Name:** usually makes sense to use the same name as the bucket name.
2. **Bucket:** the bucket name; ``my-valohai-bucket`` in this example.
3. **Service Account JSON:** copy-and-paste the contents of the JSON file we downloaded earlier.

.. thumbnail:: gcp-bucket-valohai-03.png
   :alt: Completed linking of a Google Cloud bucket

When you create the store, the credentials provided will be checked by creating a small test file in the bucket.
If the creation succeeds, you are good to go.

.. thumbnail:: gcp-bucket-valohai-04.png
   :alt: How to set the bucket as default upload store on Valohai

Once the data store is linked, you can set it as your project's default upload store under `Settings > General > Default upload store`.
This ensures that uploaded outputs will be stored in this particular GCP bucket by default.
