:hide-toc:


.. meta::
    :description: How to manually deploy Valohai resources in your AWS environment

.. _aws-hybrid-manual:


Deploy to AWS manually
######################

.. include:: _intro.rst

.. warning::

    Before running the template you'll need the following information from Valohai:

    * ``valohai_assume_user`` is the ARN of the user Valohai will use to assume a role in your AWS subscription to manage EC2 instances.
    * ``queue_address`` will be assigned for the queue in your subscription.

Configure the IAM roles
^^^^^^^^^^^^^^^^^^^^^^^

The 4 roles listed below are required for a Valohai installation.

* ``ValohaiQueueRole`` will be attached to the Valohai Queue instance, and allows it to fetch the generated password from your AWS Secrets Manager. Access is restricted to secrets that are tagged valohai:1.
* ``ValohaiWorkerRole`` is attached to all autoscaled EC2 instances that are launched for machine learning jobs.
* ``ValohaiS3MultipartRole`` will be used to upload files larger than 5GB.
* ``ValohaiMaster`` is the role that the Valohai service will use to manage autoscaling and EC2 resources. The role is also used to manage the newly provisioned valohai-data-* S3 Bucket.

Create the 4 policies listed below by going to your `AWS Console > IAM > Policies <https://console.aws.amazon.com/iamv2/home#/policies>`_.

.. warning::

  Update the following placeholders in ``ValohaiMaster`` and ``ValohaiS3MultipartPolicy`` before you save the policies:
  
  * ``valohai-data-<my-company-name>`` with your company name (``valohai-data-companya``).
  * ``<AWS-ACCOUNT-ID>`` with your AWS Account ID.


.. details:: ValohaiQueuePolicy

  .. code-block:: json

    {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Sid": "0",
              "Effect": "Allow",
              "Action": [
                  "secretsmanager:GetResourcePolicy",
                  "secretsmanager:GetSecretValue",
                  "secretsmanager:DescribeSecret",
                  "secretsmanager:ListSecretVersionIds"
              ],
              "Resource": "*",
              "Condition": {
                  "StringEquals": {
                      "secretsmanager:ResourceTag/valohai": "1"
                  }
              }
          },
          {
              "Sid": "1",
              "Effect": "Allow",
              "Action": "secretsmanager:GetRandomPassword",
              "Resource": "*"
          }
      ]
    }

  .. 

.. details:: ValohaiWorkerPolicy

  .. code-block:: json

    {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Action": "autoscaling:SetInstanceProtection",
              "Resource": "*",
              "Effect": "Allow",
              "Sid": "1"
          },
          {
              "Action": "ec2:DescribeInstances",
              "Resource": "*",
              "Effect": "Allow",
              "Sid": "2"
          }
      ]
    }

  .. 


.. details:: ValohaiS3MultipartPolicy

  .. code-block:: json

    {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Sid": "MultipartAccess",
              "Effect": "Allow",
              "Action": [
                  "s3:AbortMultipartUpload",
                  "s3:GetBucketLocation",
                  "s3:GetObject",
                  "s3:ListBucket",
                  "s3:ListBucketMultipartUploads",
                  "s3:ListBucketVersions",
                  "s3:ListMultipartUploadParts",
                  "s3:PutObject"
              ],
              "Resource": [
                  "arn:aws:s3:::valohai-data-<my-company-name>",
                  "arn:aws:s3:::valohai-data-<my-company-name>/*"
              ]
          }
      ]
    }

  .. 


.. details:: ValohaiMasterPolicy

  .. code-block:: json

     {
        "Version" : "2012-10-17",
        "Statement" : [
          {
            "Sid" : "2",
            "Effect" : "Allow",
            "Action" : [
              "ec2:DescribeInstances",
              "ec2:DescribeVpcs",
              "ec2:DescribeKeyPairs",
              "ec2:DescribeImages",
              "ec2:DescribeSecurityGroups",
              "ec2:DescribeSubnets",
              "ec2:DescribeInstanceTypes",
              "ec2:DescribeLaunchTemplates",
              "ec2:DescribeLaunchTemplateVersions",
              "ec2:CreateTags",
              "autoscaling:DescribeAutoScalingGroups",
              "autoscaling:DescribeScalingActivities"
            ],
            "Resource" : "*"
          },
          {
            "Sid" : "AllowUpdatingSpotLaunchTemplates",
            "Effect" : "Allow",
            "Action" : [
              "ec2:CreateLaunchTemplate",
              "ec2:CreateLaunchTemplateVersion",
              "ec2:ModifyLaunchTemplate",
              "ec2:RunInstances",
              "ec2:RebootInstances",
              "autoscaling:UpdateAutoScalingGroup",
              "autoscaling:CreateOrUpdateTags",
              "autoscaling:SetDesiredCapacity",
              "autoscaling:CreateAutoScalingGroup"
            ],
            "Resource" : "*",
            "Condition" : {
              "ForAllValues:StringEquals" : {
                "aws:ResourceTag/valohai" : "1"
              }
            }
          },
          {
            "Sid" : "ServiceLinkedRole",
            "Effect" : "Allow",
            "Action" : "iam:CreateServiceLinkedRole",
            "Resource" : "arn:aws:iam::*:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling"
          },
          {
            "Sid" : "4",
            "Effect" : "Allow",
            "Action" : [
              "iam:PassRole",
              "iam:GetRole"
            ],
            "Resource" : "arn:aws:iam::<ACCOUNT-ID>:role/ValohaiWorkerRole"
          },
          {
            "Sid" : "0",
            "Effect" : "Allow",
            "Condition" : {
              "StringEquals" : {
                "secretsmanager:ResourceTag/valohai" : "1"
              }
            },
            "Action" : [
              "secretsmanager:GetResourcePolicy",
              "secretsmanager:GetSecretValue",
              "secretsmanager:DescribeSecret",
              "secretsmanager:ListSecretVersionIds"
            ],
            "Resource" : "*"
          },
          {
            "Action" : "secretsmanager:GetRandomPassword",
            "Resource" : "*",
            "Effect" : "Allow",
            "Sid" : "1"
          },
          {
            "Effect" : "Allow",
            "Action" : "s3:*",
            "Resource" : [
              "arn:aws:s3:::valohai-data-<my-company-name>",
              "arn:aws:s3:::valohai-data-<my-company-name>/*"
            ]
          }
        ]
      }

Next create the roles listed below by going to your `AWS Console > IAM > Roles <https://console.aws.amazon.com/iamv2/home#/roles>`_.

.. list-table::
   :widths: 33 33 33
   :header-rows: 1
   :stub-columns: 1

   * - Name
     - Use Case
     - Policy
   * - ValohaiQueueRole
     - EC2
     - ``ValohaiQueuePolicy``
   * - ValohaiWorkerRole
     - EC2
     - ``ValohaiWorkerPolicy``
   * - ValohaiS3MultipartRole
     - Another AWS Account.
       
       * **Account ID:** ``<YOUR-AWS-ACCOUNT-ID>``

     - ``ValohaiS3MultipartPolicy``
  
   * - ValohaiMaster
     - Another AWS Account
       
       * **Account ID:** ``905675611115``
     
     - ``ValohaiMasterPolicy``

.. important::

    Note ``ValohaiQueueRole`` and ``ValohaiWorkerRole`` need to also have instance profiles They will get automatically created when you create a role through the console.
    
    If you're creating the resources with the AWS CLI, follow the `AWS documentation <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html>`_ to learn how to create and attach an instance profile to a role.

Deploying resources
^^^^^^^^^^^^^^^^^^^^

We recommend setting up the Valohai resources in a fresh AWS Account. If you prefer to use an existing account and VPC, you'll need to adopt the instructions below to your environment.

Reach out to support@valohai.com if you have any questions.

.. warning::

  Before deploying your resources, you'll need to get the following information from Valohai:

  * ``valohai_assume_user`` is the ARN of the user Valohai will use to assume a role in your AWS subscription to manage EC2 instances.
  * ``queue_address`` will be assigned for your job queue.


.. list-table::
   :widths: 20 25 55
   :header-rows: 1
   :stub-columns: 1

   * - Resource
     - Name
     - Details
   * - VPC
     - ``valohai-vpc``
     - 
       * **CIDR:** 10.0.0.0/16
       * **Tag:** Key=valohai,Value=1
   * - Subnets
     - ``valohai-subnet-x``
     - 
       * **Create one subnet per zone** in your AWS Region
       * **Example CIDR ranges:** 

         * valohai-subnet-1, 10.0.0.0/20, Availability Zone: a
         * valohai-subnet-2, 10.0.16.0/20, Availability Zone: b
         * valohai-subnet-3, 10.0.32.0/20, Availability Zone: c
         * valohai-subnet-4, 10.0.48.0/20, Availability Zone: d

       * **Tag:** Key=valohai,Value=1
   * - Internet Gateway
     - ``valohai-igw``
     - 
       * **Attach** the gateway to ``valohai-vpc``
       * **Tag:** Key=valohai,Value=1
   * - Routing Table
     - Rename the default route table of ``valohai-vpc`` to ``valohai-rt``
     - 
       * Edit Routes:
  
         * ``10.0.0.0/16 => local``
         * ``0.0.0.0/0 => <ID of valohai-igw>``
  
       * **Tag:** Key=valohai,Value=1
   * - Security Group
     - ``valohai-sg-workers``
     - 
       * ``Inbound Rules``

       * ``Outbound Rules``
  
         * Keep default settings. All outbound traffic is allowed.
  
       * **Tag:** Key=valohai,Value=1
   * - Security Group
     - ``valohai-sg-queue``
     - 
       * ``Inbound Rules``
  
         * Port ``80`` on ``0.0.0.0/0`` for ACME tooling and LetsEncrypt challenge
         * Port ``63790`` on ``34.248.245.191/32`` for Redis over SSL from app.valohai.com
         * Port ``63790`` on ``<ID of valohai-sg-workers>`` for Redis over SSL from Valohai workers

       * ``Outbound Rules``
  
         * Keep default settings. All outbound traffic is allowed.
  
       * **Tag:** Key=valohai,Value=1
   * - Secrets Manager Secret
     - ``ValohaiRedisSecret``
     - 
       * **Type:** "Other type of secrets"
       * **Plaintext secret:** Generate a random password, that includes lowercase and capital letters and numbers.
       * **Tag:** Key=valohai,Value=1
       * **Automatic rotation:** Keep the default setting (Disable automatic rotation)
   * - Elastic IP
     - ``valohai-ip-queue``
     - 
       * Allocate a new Elastic IP adddress from the Amazon's pool of IPv4 addresses
       * **Tag:** Key=valohai,Value=1
   * - EC2 Instance
     - ``valohai-sg-queue``
     
       **IMPORTANT:** Replace the ``<queue_address>`` with the correct value!
     - 
       * **OS:** Ubuntu 20.04 LTS
       * **Machine type:** t3.medium (2 vCPU, 4GB RAM)
       * **Instance Details:**
       
         * **VPC:** ``valohai-vpc``
         * **IAM role:** ValohaiQueueRole
         * **User data:** 
         
           .. code-block:: bash
             
              #!/bin/bash
              sudo apt-get update && sudo apt-get install awscli -y
              export REGION=`curl -s http://169.254.169.254/latest/meta-data/placement/region/`
              export PASSWORD=`aws secretsmanager get-secret-value --secret-id ValohaiRedisSecret --region $REGION | sed -n 's|.*"SecretString": *"\([^"]*\)".*|\1|p'`
              export QUEUE=<queue_address>
              curl https://raw.githubusercontent.com/valohai/worker-queue/main/host/setup.sh | sudo QUEUE_ADDRESS=$QUEUE REDIS_PASSWORD=$PASSWORD bash
              unset PASSWORD
         
       * **Storage:**
         
         * **Standard persistent disk:** 16GB

       * **Tag:** Key=valohai,Value=1
       * **Security Group:** ``valohai-sg-queue``
       * **Key Pair:** Generate a new Key Pair for Valohai
       * After the instance has been creating
   * - S3 Bucket
     - ``valohai-data-<my-company-name>``
     - 
       * Turn on **Block all public access**
       * **Tag:** Key=valohai,Value=1
       * After you've created the bucket go to the bucket ``Permissions`` tab and set the CORS policy as below:
       
         .. code-block:: json

           [
            {
                "AllowedHeaders": ["Authorization"],
                "AllowedMethods": ["GET"],
                "AllowedOrigins": ["*"],
                "ExposeHeaders": [],
                "MaxAgeSeconds": 3000
            },
            {
                "AllowedHeaders": ["Authorization"],
                "AllowedMethods": ["POST"],
                "AllowedOrigins": ["https://app.valohai.com"],
                "ExposeHeaders": [],
                "MaxAgeSeconds": 3000
            }
          ]
         ..

Next steps
-----------

You'll need to share the ``ARN of the ValohaiMaster Role`` with your Valohai contact, so they can finish the setup on app.valohai.com and enable your organization's environments on the platform.

