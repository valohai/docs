Use a private S3 bucket for data storage
----------------------------------------

In this guide, we'll link a private AWS S3 bucket to a Valohai project.

.. contents::
   :backlinks: none
   :local:

1. Requirements
~~~~~~~~~~~~~~~

For this tutorial you will need:

* an Amazon Web Services (AWS) account you can administer
* a Valohai project which to link the bucket to

2. Create the S3 Bucket
~~~~~~~~~~~~~~~~~~~~~~~

Create an S3 bucket in the the Amazon AWS console ( https://s3.console.aws.amazon.com/s3/home ).

Throughout this guide, we will assume the name of the bucket is ``my-valohai-bucket``; *be sure to replace
this with the actual name of your bucket* when copying in any example configuration!


3. Configure CORS for the S3 Bucket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wish to be able to upload files to the store using the app.valohai.com web UI, you will need to
add a CORS Policy document to the S3 bucket.  The document should allow POST from https://app.valohai.com/ .
An example document follows.

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
       <CORSRule>
           <AllowedOrigin>*</AllowedOrigin>
           <AllowedMethod>GET</AllowedMethod>
           <MaxAgeSeconds>3000</MaxAgeSeconds>
           <AllowedHeader>Authorization</AllowedHeader>
       </CORSRule>
       <CORSRule>
           <AllowedOrigin>https://app.valohai.com</AllowedOrigin>
           <AllowedMethod>POST</AllowedMethod>
           <MaxAgeSeconds>3000</MaxAgeSeconds>
           <AllowedHeader>Authorization</AllowedHeader>
       </CORSRule>
   </CORSConfiguration>

4. Create and configure an IAM User
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the AWS console, create a new IAM user with programmatic access credentials (access key ID / secret access key).

The user needs to have full access to the S3 bucket; an example of a suitable access policy document is below.
Make sure to change the resource name `my-valohai-bucket`!

.. code-block:: json

   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "AllowBucketAccess",
               "Effect": "Allow",
               "Action": [
                   "s3:*"
               ],
               "Resource": [
                   "arn:aws:s3:::my-valohai-bucket",
                   "arn:aws:s3:::my-valohai-bucket/*"
               ]
           },
           {
               "Sid": "AllowListAccess",
               "Effect": "Allow",
               "Action": [
                   "s3:ListAllMyBuckets"
               ],
               "Resource": [
                   "arn:aws:s3:::*"
               ]
           }
       ]
   }

5. Large File Uploads (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If executions need to upload outputs larger than 5 GB, additional setup is needed.
This is **optional** and only required for large outputs.

To upload large outputs using Amazon's multi-part upload API,
a temporary AWS IAM role will be dispensed to the worker machines when required.

Be sure to replace the following placeholders in the following policy examples!

* `BUCKET` – the target S3 bucket
* `ACCOUNTNUMBER` – your AWS account number
* `USERNAME` – the username associated with the access keys that are being used with the store

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

Take note of the role's AWS ARN (``arn:aws:...``).

6. Set up the store in Valohai
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to your project's Settings and choose Data Stores. Then choose "Add S3 store".

Name your store and paste in the bucket name and the IAM credentials in the fields provided.

If you also created the IAM Role for large uploads, paste the ARN in in the "Multipart Upload IAM Role ARN" field.
If you did not create the role, you may leave this field empty.

When you create the store, the credentials provided will be checked by creating a small test file in the bucket.

Once set up, you can set the store as your project's default store in the Settings > Basic Information view.
This ensures outputs will be stored in your S3 bucket.

