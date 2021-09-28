:orphan:

.. meta::
    :description: How to prepare your AWS environment for a Valohai Private Workers installation


Preparing your AWS for Valohai Hybrid Implementation
######################################################

This document prepares your AWS account for Valohai private worker installation.

📝 From your Valohai contact, ask and record the AssumeRole ARN.

Select the correct region
-------------------------

Select the appropriate region for the resources:

* Consider selecting the same region where your data is located. This way data is transferred quickly and there are no transfer fees.
* Consider selecting a region where you've already acquired GPU quota from Amazon.
* When selecting your region, note that different regions have different GPUs available:
    * For US customers, we recommend **US West 2 (Oregon)** as they have the widest array of GPU instance types in the United States.
    * For EU customers, we recommend **EU West 1 (Ireland)** as it has the widest array of GPU instance types in Europe.

📝 Record the region you have selected.

.. admonition:: Setting up a sub account (optional)
    :class: ip

    You can create a dedicated sub account in AWS for all the Valohai resources. This sub account separates the Valohai resources from all other AWS services you might be using.

    Create all the following IAM access control entities in this sub account.


Create IAM Entities
-------------------

These IAM entities are required to create autoscaling groups for the Valohai workers.

IAM Role "ValohaiWorkerRole"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This role is assigned to the individual EC2 instances to query information about themselves and set instance protection to prevent unwanted termination when processing workloads.

**Create an IAM Policy**

Start by creating a policy that we'll attach to the role:

* Open the AWS Console and navigate to `IAM -> Policies <https://console.aws.amazon.com/iam/home#/policies>`_
* Create policy
* Paste the JSON from below as the new policy
* Add a tag `valohai` with value `1`
* Name the policy `ValohaiWorkerPolicy`

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

**Create an IAM Role**

* Open the AWS Console and navigate to `IAM -> Roles <https://console.aws.amazon.com/iam/home#/roles>`_ 
* Create role
* Choose EC2 as the use case
* Find and attach the `ValohaiWorkerPolicy` policy
* Add a tag `valohai` with value `1`
* Name the role `ValohaiWorkerRole`

📝 Record the `ValohaiWorkerRole` ARN.

.. admonition:: Note: Instance profile
    :class: info
    
    If you use the AWS Management Console to create the `ValohaiWorkerRole`, the console will automatically create an instance profile and gives it the same name as the role. If you're using the AWS CLI or APIs to create this role, you'll need to manually create an instance profile and add the role to it. Read more at `AWS: Using instance profiles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html>`_


IAM Role "ValohaiMaster"
^^^^^^^^^^^^^^^^^^^^^^^^

These are credentials allowing the Valohai web application at https://app.valohai.com/ and autoscaling services to: 

1. See how many instances related to Valohai are running
2. Scale workers up and down
3. Add launch configurations and autoscaling groups, one for each instance type
4. Enable the organization admin to adjust the maximum price for spot instances in the Valohai web app

**Create an IAM Policy**

Start by creating a policy that defines permissions for the role that Valohai can assume:

* Open the AWS Console and navigate to `IAM -> Policies <https://console.aws.amazon.com/iam/home#/policies>`_
* Create policy
* Paste the JSON from below as the new policy
* Add a tag `valohai` with value `1`
* Name the policy `ValohaiMasterPolicy`

.. admonition:: Important
    :class: warning
    
    📝 Replace the template on the last line in the policy with the recorded `ValohaiWorkerRole` ARN.

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
                    "ec2:DescribeLaunchTemplateVersions",
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
                "Resource": "RECORDED ValohaiWorkerRole ARN HERE"
            }
        ]
    }

**Create an IAM Role**

* Open the AWS Console and navigate to `IAM -> Roles <https://console.aws.amazon.com/iam/home#/roles>`_
* Create role
* Choose EC2 as the use case
* Find and attach the `ValohaiMasterPolicy` policy
* Add a tag `valohai` with value `1`
* Name the role `ValohaiMaster`

Once the role is created open the role's **Trust relationships** tab and click **Edit trust relationship**

Paste in the below trust relationship to give Valohai access to this role.

.. admonition:: Important
    :class: warning
    
    📝 Replace the template "AWS" in the policy with the recorded AssumeRole ARN.

.. code-block:: json

    {
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Principal": {
                "AWS": "RECORDED AssumeRole ARN HERE"
            },
            "Action": "sts:AssumeRole",
            "Condition": {}
            }
        ]
    }

Create Network Resources and the Worker Queue Instance
------------------------------------------------------

Below is a list of the AWS resources that the Valohai Private Worker installation requires.

You can either create these resources yourself, or give the ValohaiMaster role elevated permissions for the duration of the setup.

Option 1) Provision the Resources Yourself
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**VPC and Subnets**

Create a VPC and subnets per each availability zone you want to use. For example:

* VPC
    * Name: `valohai-vpc`
    * CIDR: 10.0.0.0/16
    * Tag: Key=valohai Value=1

📝 Record the VPC ID.

* One subnet per zone. For example
    * Subnet: `valohai-subnet-1`, 10.0.0.0/20, Tag: Key=valohai Value=1
    * Subnet: `valohai-subnet-2`, 10.0.16.0/20, Tag: Key=valohai Value=1
    * Subnet: `valohai-subnet-3`, 10.0.32.0/20, Tag: Key=valohai Value=1
    * Subnet: `valohai-subnet-4`, 10.0.48.0/20, Tag: Key=valohai Value=1

📝 Record the subnet names.

Create an internet gateway:

* Internet Gateway
    * Name: `valohai-igw`
    * Tag: Key=valohai Value=1
    * **Attach** this Internet Gateway to `valohai-vpc`

Rename the default routing table of `valohai-vpc`:

* Routing Table
    * **Rename** to `valohai-rt`
    * Tag: Key=valohai Value=1
    * **Edit** the routes:
        * 10.0.0.0/16 => local
        * 0.0.0.0/0 => `valohai-igw`

**Security Groups**

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
      - 3.251.38.215/32 (optional)
      - for SSH management from Valohai

Make sure the workers have access to **outbound internet** (default settings in AWS)

.. list-table::
    :header-rows: 1
    :widths: 15 15 70

    * - Protocol
      - Port
      - Destination
    * - All
      - All
      - 0.0.0.0/0

We recommend allowing all outbound traffic from your workers, so you can easily access various resources and install additional libraries from your ML executions.

At the very least, you'll need to allow outbound access on ports 80 and 443 to 0.0.0.0/0 and 63790 to the ``valohai-sg-queue`` which is created below.

Tag the security group with Key=valohai Value=1.

Create a new security group named **valohai-sg-queue** and set the Inbound rules listed below:

.. list-table::
    :header-rows: 1
    :widths: 15 15 20 50

    * - Protocol
      - Port
      - Source
      - Description
    * - TCP
      - 80
      - 0.0.0.0/0
      - for acme tooling (certificate for machine)
    * - TCP
      - 63790
      - 34.248.245.191/32
      - for Redis over TLS from app.valohai.com
    * - TCP
      - 63790
      - valohai-sg-workers
      - for Redis over TLS connection from workers
    * - TCP
      - 22
      - your IP (if you install the worker queue)
      - for SSH management
    * - TCP
      - 22
      - 3.251.38.215/32 (if Valohai installs the worker queue)
      - for SSH management from Valohai

Tag the security group with Key=valohai Value=1.

**EC2 Instance for the Worker Queue**

Next provision an Elastic IP and an EC2 instance for running the worker queue. The worker queue hosts a Redis server for passing jobs to workers and storing short-term logs.

* EC2 instance
    * Name: `valohai-i-queue`
    * OS: Ubuntu 20.04 LTS
    * Machine type: t3.medium (2 vCPU, 4GB RAM)
    * Standard persistent disk: 16GB
    * Security Group: `valohai-sg-queue`
    * Key Pair: Create a new key pair
    * Tag: Key=valohai Value=1

📝 Record the name of the Key Pair and the key itself.

* Elastic IP from the Amazon pool
    * Name: `valohai-ip-queue`
    * Tag: Key=valohai Value=1
    * **Attach** this Elastic IP to the `valohai-i-queue` instance

📝 Record the public and private IP addresses of the EC2 instance.

Option 2) Give Valohai Permission to Provision the Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the following policies to the `ValohaiMaster` role to give Valohai permission to create the queue instance and setup the networking resources.

* **AmazonEC2FullAccess**
* **AmazonVPCFullAccess**

Conclusion
----------

Share the recorded information with your Valohai contact using the Vault credentials provided to you:

📝 You should now have the following information recorded:

* Region (where your workers will run)
* ValohaiMaster role ARN (that Valohai can assume to setup workers)

📝 If you provisioned the resources yourself, you should also have the following recorded:

* VPC ID
* Subnet names
* Public IP of the `valohai-i-queue` instance
* Private IP of the `valohai-i-queue` instance
* Name of the EC2 Key Pair

📝 If you provisioned the resources and Valohai will setup the worker queue for you, then you need to share the recorded key. If you setup the worker queue, you will need this key yourself:

* The EC2 Key Pair key

.. seealso:: 

    Each Valohai project has one or more data stores. A data store is a secure place to keep your files; you download training data from there and upload files from your executions there (e.g. models, weights, images).

    It's good practice to setup one S3 Bucket to work as the default bucket for all projects in your organization. Each project owner can then change the bucket if needed, but this way you can ensure that all data ends up in your S3 bucket, instead of the shared Valohai storage.

    `Add AWS S3 to Valohai </tutorials/cloud-storage/private-s3-bucket/>`_
