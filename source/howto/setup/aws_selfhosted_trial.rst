:orphan:

.. meta::
    :description: How to prepare your AWS environment for a Valohai self-hosted trial


Preparing your AWS for Valohai self-hosted trial
#################################################

This document prepares your AWS account for a Valohai self-hosted trial.

Select the correct region
--------------------------

Select the appropriate region for the resources:

* Consider using the same region where your data is located to reduce data transfer times.
* Consider using the regions where you've already acquired GPU quota from Amazon.
* When selecting your region, note that regions have different collections of available GPU types.
    * For US customers, we recommend **US West 2 (Oregon)** as they have the widest array of GPU machine types in the United States.
    * For EU customers, we recommend **EU West 1 (Ireland)** as it has the widest array of GPU machine types in the Europe.


.. admonition:: Setting up a sub account (optional)
    :class: ip

    You can create a dedicated sub account in AWS for all the Valohai resources. This sub account separates the Valohai resources from all other AWS services you might be using.

    Create all the following IAM access control entities in this sub account.

Create a S3 Bucket
---------------------------------

Create an S3 bucket through AWS console (https://s3.console.aws.amazon.com/s3/home).

Select bucket name and region
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Throughout this guide, we will assume the name of the bucket is ``valohai-bucket``; *be sure to replace this with the actual name of your bucket* when copying in any example configuration!
2. Create the bucket in the region you'll be running your training to minimize data transfer costs. If you don't have a preference, we recommend using Ireland (`eu-west-1`) as most of our computation resides there.

Use default bucket properties & permissions
---------------------------------------------------------------

Default bucket properties are fine, but double check that your bucket is not public.
You can of course edit the default settings based on your needs.

Create a new bucket.

Configure CORS for the S3 bucket
------------------------------------

If you wish to be able to upload files to the store using the app.valohai.com web UI, you will need to
add a CORS policy document to the S3 bucket.

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


Creating IAM Entities
------------------------------------

As we want to avoid having access to your AWS authentication and authorization, do a couple of configurations under IAM.

IAM Role "ValohaiWorkerRole"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This role is assigned to the individual EC2 instances (machine learning job workers) to query information about themselves and set instance protection to prevent inadvertent termination when processing workloads.

**Create a IAM policy**
Start by creating a policy that we'll attach to the role:

* Open the AWS Console and navigate to `IAM -> Policies <https://console.aws.amazon.com/iam/home#/policies>`_
* Click on **create policy**
* Paste the JSON from below as the new policy
* Add a tag `valohai` with value `1`
* Give the policy a name `ValohaiWorkerPolicy`

.. code-block:: json

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "1",
                "Effect": "Allow",
                "Action": "autoscaling:SetInstanceProtection",
                "Resource": "*"
            },
            {
                "Sid": "2",
                "Effect": "Allow",
                "Action": "ec2:DescribeInstances",
                "Resource": "*"
            }
        ]
    }

..

**Create a IAM role**

* Open the AWS Console and navigate to `IAM -> Roles <https://console.aws.amazon.com/iam/home#/roles>`_
* Create a new role called `ValohaiWorkerRole` 
* Create role
* Choose EC2 as the use case
* Find and attach the `ValohaiWorkerPolicy` policy
* Add a tag `valohai` with value `1`

Copy the `Role ARN` shown for the newly created role. You'll need this in the next step.

.. admonition:: Note: Instance profile
    :class: info
    
    If you use the AWS Management Console to create the `ValohaiWorkerRole`, the console will automatically create an instance profile and gives it the same name as the role. If you're using the AWS CLI or APIs to create this role, you'll need to manually create an instance profile and add the role to it. Read more at [AWS: Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)


IAM User for ValohaiMaster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are credentials for the Valohai web application at https://app.valohai.com/ and scaling services to: 

1. be able to see how many Valohai-related instances are running 
2. allow scaling worker clusters up and down
3. add various launch configurations and auto scaling groups, one for each instance type.
4. allow the organization admin to adjust max price for spot instances through app.valohai.com

**Create a IAM policy**

Start by creating a policy that defines permissions for the role that Valohai can assume:

* Open the AWS Console and navigate to `IAM -> Policies <https://console.aws.amazon.com/iam/home#/policies>`_
* Click on **Create policy**
* Paste the JSON from below as the new policy
* Add a tag `valohai` with value `1`
* Give the policy a name `ValohaiMasterPolicy`

.. admonition:: Important
    :class: warning
    
    Make sure you paste your own ValohaiWorkerRole ARN to the last line.

..

.. code-block:: json 

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "2",
                "Effect": "Allow",
                "Action": [
                    "ec2:DescribeInstances",
                    "ec2:DescribeVpcs",
                    "ec2:DescribeKeyPairs",
                    "ec2:DescribeImages",
                    "ec2:DescribeSecurityGroups",
                    "ec2:DescribeSubnets",
                    "ec2:DescribeInstanceTypes",
                    "ec2:DescribeLaunchTemplates",
                    "ec2:CreateTags",
                    "autoscaling:DescribeAutoScalingGroups",
                    "autoscaling:DescribeScalingActivities"
                ],
                "Resource": "*"
            },
            {
                "Sid": "AllowUpdatingSpotLaunchTemplates",
                "Effect": "Allow",
                "Action": [
                    "ec2:CreateLaunchTemplate",
                    "ec2:CreateLaunchTemplateVersion",
                    "ec2:ModifyLaunchTemplate",
                    "ec2:RunInstances",
                    "autoscaling:UpdateAutoScalingGroup",
                    "autoscaling:CreateOrUpdateTags",
                    "autoscaling:SetDesiredCapacity",
                    "autoscaling:CreateAutoScalingGroup"
                ],
                "Resource": "*",
                "Condition": {
                    "ForAllValues:StringEquals": {
                        "aws:ResourceTag/Valohai": "1"
                    }
                }
            },
            {
                "Sid": "ServiceLinkedRole",
                "Effect": "Allow",
                "Action": "iam:CreateServiceLinkedRole",
                "Resource": "arn:aws:iam::*:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling"
            },
            {
                "Sid": "4",
                "Effect": "Allow",
                "Action": [
                    "iam:PassRole",
                    "iam:GetRole"
                ],
                "Resource": "arn:aws:iam::<YOUR-AWS-ACCOUNT-ID>:role/ValohaiWorkerRole"
            },
            {
                "Sid": "4",
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": [
                    "arn:aws:s3:::valohai-bucket",
                    "arn:aws:s3:::valohai-bucket/*"
                ]
            }
        ]
    }

..

**Create the IAM role**

* Open the AWS Console and navigate to `IAM -> Users <https://console.aws.amazon.com/iam/home#/users>`_
* Create a new user called `ValohaiMaster` 
* Choose EC2 as the use case
* Find and attach the `ValohaiMasterPolicy` policy
* Add a tag `valohai` with value `1`

You'll need the access key and secret key during the installation to allow the Valohai application to scale IAM resources in your subscription.

Setting up Valohai resources
------------------------------

Below is a list of the AWS resources that are required for the self-hosted Valohai installation.

Optional: VPC and subnets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use your existing VPC or create a new VPC and subnets per each availability zone you want to use. For example:

* VPC
    * **Name:** valohai-vpc
    * **CIDR:** 10.0.0.0/16
* One subnet per zone. For example
    * Subnet: valohai-subnet-1, 10.0.0.0/20, -
    * Subnet: valohai-subnet-2, 10.0.16.0/20, -
    * Subnet: valohai-subnet-3, 10.0.32.0/20, -
    * Subnet: valohai-subnet-4, 10.0.48.0/20, -
* Internet Gateway
    * **Name:** valohai-igw
    * **Attach** this Internet Gatway to valohai-vpc


* **Routing Table** rename the default table to valohai-rt
    * **Edit Routes:**
        * 10.0.0.0/16 -> local
        * 0.0.0.0/0 => valohai-igw

Security groups
^^^^^^^^^^^^^^^^^^^^

Create a new security group named **valohai-sg-workers** and set the Inbound rules listed below:

.. list-table::
    :header-rows: 1
    :widths: 15 15 20 50

    * - Protocol
      - Port
      - Source
      - Description
    * - TCP
      - 22
      - 3.251.38.215/32 (during installation)
      - for SSH management from Valohai

Create a new security group named **valohai-sg-master** and set the Inbound rules listed below:

.. list-table::
    :header-rows: 1
    :widths: 15 15 20 50

    * - Protocol
      - Port
      - Source
      - Description
    * - TCP
      - 6379
      - valohai-sg-workers
      - for plain Redis connection from workers
    * - TCP
      - 22
      - 3.251.38.215/32 (during installation)
      - for SSH management from Valohai

EC2 Instance for Valohai master
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Provision an Elastic IP and a EC2 instance for storing the job quue and short term logs.

* Elastic IP from the Amazon pool
    * **Name:** valohai-ip-master
* EC2 instance works as the master instace for Valohai and will host all the core Valohai services.
    * **Name:** valohai-i-master
    * **OS:** Ubuntu 20.04 LTS
    * **Machine type:** t3.xlarge (4 vCPU, 16GB RAM)
    * **Standard persistent disk:** 200GB
    * **Security Group:** valohai-sg-master
    * **Key Pair**: You'll receive the key pair from your Valohai contact
    * **Tag:** Valohai

Attach the Elastic IP to the new VM instance.

Conclusion
-------------

You should now have the following details:

* Region
* S3 Bucket for Valohai
* IAM User for ValohaiMaster (inc. Access Key and Secret)
* IAM Role for ValohaiWorkerRole
* Name of VPC for Valohai workers
* Security groups for valohai-sg-master and valohai-sg-workers
* Names of subnets that can be used for Valohai workers
* Public IP of the EC2 instance for Valohai
* Private IP of the EC2 instance for Valohai


.. seealso:: 

    Each Valohai project has one or more data stores. A data store is a secure place to keep your files; you download training data from there and upload files from your executions there (e.g. models, weights, images).

    It's good practice to setup one S3 Bucket to work as the default bucket for all projects in your organization. Each project owner can then change the bucket if needed, but this way you can ensure that all data ends up in your S3 bucket, instead of the shared Valohai storage.

    `Add AWS S3 to Valohai </tutorials/cloud-storage/private-s3-bucket/>`_
