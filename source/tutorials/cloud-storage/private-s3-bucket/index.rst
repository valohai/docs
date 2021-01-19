.. meta::
    :description: Link a private AWS S3 bucket containing the data for deep learning experiments to a Valohai project. Optionally create multiple buckets to keep track of different versions of deep learning models or projects.

Connecting to AWS S3
====================

In this guide, we'll link a private AWS S3 bucket to a Valohai project.

.. contents::
   :backlinks: none
   :local:

.. include:: ../_shared-data-store-warning.rst

1. Requirements
~~~~~~~~~~~~~~~

For this tutorial you will need:

* an Amazon Web Services (AWS) account you can administer
* a Valohai project which to link the S3 bucket to

2. Create the S3 bucket
~~~~~~~~~~~~~~~~~~~~~~~

Create an S3 bucket through AWS console (https://s3.console.aws.amazon.com/s3/home).

2.1 Select bucket name and region
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: bucket-01.png
   :alt: S3 bucket creation, page 1

1. Throughout this guide, we will assume the name of the bucket is ``my-valohai-bucket``; *be sure to replace this with the actual name of your bucket* when copying in any example configuration!
2. Create the bucket in the region you'll be running your training to minimize data transfer costs. If you don't have a preference, we recommend using Ireland (`eu-west-1`) as most of our computation resides there.

2.2 Use default bucket properties & permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: bucket-02.png
   :alt: S3 bucket creation, page 2

Default bucket properties are fine, but double check that your bucket is not public.
You can of course edit the default settings based on your needs.

Create a new bucket.

3. Configure CORS for the S3 bucket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wish to be able to upload files to the store using the app.valohai.com web UI, you will need to
add a CORS policy document to the S3 bucket.

.. thumbnail:: bucket-03.png
   :alt: S3 bucket with the CORS setting

First you navigate to the AWS S3 bucket you created.

Then you go to the *Permissions* tab and scroll down to *Cross-origin resource sharing (CORS)*.

Click *Edit* add the rules below.

.. code-block:: json

   [
      {
         "AllowedHeaders": [
               "Authorization"
         ],
         "AllowedMethods": [
               "GET"
         ],
         "AllowedOrigins": [
               "*"
         ],
         "ExposeHeaders": [],
         "MaxAgeSeconds": 3000
      },
      {
         "AllowedHeaders": [
               "Authorization"
         ],
         "AllowedMethods": [
               "POST"
         ],
         "AllowedOrigins": [
               "https://app.valohai.com"
         ],
         "ExposeHeaders": [],
         "MaxAgeSeconds": 3000
      }
   ]

..

Now your bucket allows POSTs for your user on `https://app.valohai.com` website

4. Create an IAM user
~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: s3-user-01.png
   :alt: IAM home page

Using the AWS console, start creating a new IAM user with programmatic access credentials (access key ID / secret access key).

4.1 Select name for your programmatic user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: s3-user-02.png
   :alt: IAM user creation, page 1

1. User name can be anything, try to be descriptive.
2. Double check that programmatic access is turned on.

4.2 Skip the permission configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will add permissions later, you can skip to the next step.

4.3 Save access key ID and secret for later usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: s3-user-03.png
   :alt: IAM user creation, page 3

Download the CSV or copy-paste the "Access key ID" and "Secret access key" somewhere safe.

.. tip:: If you lose these credentials, you can generate new ones though `IAM > Select user > Security credentials > Create access key`.

5. Allow the IAM user to access the bucket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we have a user without any permissions, let's allow the user to access our new bucket.

.. thumbnail:: s3-user-04.png
   :alt: IAM user listing

Find and open the user you created in the previous section.

.. thumbnail:: s3-user-05.png
   :alt: IAM user inline policy location

Add a new inline policy. You can use any other AWS IAM policy definition methods just as well. Inline policies are the easiest get started.

.. thumbnail:: s3-user-06.png
   :alt: IAM user inline policy definition

The user needs to have full access to the S3 bucket; an example of a suitable access policy document is below.
Make sure to change the resource name `my-valohai-bucket`!

.. code-block:: json

   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "s3:*",
               "Resource": [
                   "arn:aws:s3:::my-valohai-bucket",
                   "arn:aws:s3:::my-valohai-bucket/*"
               ]
           }
       ]
   }

.. thumbnail:: s3-user-07.png
   :alt: IAM user policy creation review page

Give your policy a descriptive name and we are done with the mandatory AWS setup!

5. Large file uploads (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If executions need to upload outputs larger than 5 GB, additional setup is needed.
This is **optional** and only required for large outputs.

To upload large outputs using Amazon's multi-part upload API,
a temporary AWS IAM role will be dispensed to the worker machines when required.

Be sure to replace the following placeholders in the following policy examples!

* `BUCKET` – the target S3 bucket
* `ACCOUNTNUMBER` – your AWS account number
* `USERNAME` – the username liked to the access keys that are being used with the store

Create a new AWS IAM **Role**. The role policy document should look like:

.. code-block:: json

   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "MultipartAccess",
               "Effect": "Allow",
               "Action": [
                   "s3:AbortMultipartUpload",
                   "s3:GetObject",
                   "s3:ListBucket",
                   "s3:ListBucketMultipartUploads",
                   "s3:ListBucketVersions",
                   "s3:ListMultipartUploadParts",
                   "s3:PutObject"
               ],
               "Resource": [
                   "arn:aws:s3:::BUCKET",
                   "arn:aws:s3:::BUCKET/*"
               ]
           }
       ]
   }

The trust relationship document should look like:

.. code-block:: json

   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::ACCOUNTNUMBER:user/USERNAME"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }

Take note of the role's AWS ARN (``arn:aws:...``), that will be configured to your Valohai project.

6. Link the store to Valohai
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: store-settings-01.png
   :alt: Valohai S3 store creation location

Navigate to `Project > Settings > Data Stores > Add S3 store`

.. thumbnail:: store-settings-02.png
   :alt: Valohai S3 store creation view

Name your store and paste in the bucket name and the IAM credentials in the fields provided.

If you also created the optional IAM Role for large uploads, paste the ARN in in the "Multipart Upload IAM Role ARN" field. You may leave this field empty.

When you create the store, the credentials provided will be checked by creating a small test file in the bucket.

.. thumbnail:: store-settings-03.png
   :alt: Valohai project settings with default store highlighted

Once set up, you can set the store as your project's default store in the `Settings > General` view. This ensures outputs will be stored in your S3 bucket.
