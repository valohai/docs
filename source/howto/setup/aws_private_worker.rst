:orphan:

.. meta::
    :description: How to prepare your AWS environment for a Valohai Private Workers installation


Preparing your AWS for Valohai Private Worker Setup
###################################################

This document prepares your AWS account for Valohai private worker installation. 

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


IAM Role for ValohaiMaster
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
            }
        ]
    }

..

**Create the IAM role**

* Open the AWS Console and navigate to `IAM -> Roles <https://console.aws.amazon.com/iam/home#/roles>`_
* Create a new role called `ValohaiMaster` 
* Choose EC2 as the use case
* Find and attach the `ValohaiMasterPolicy` policy
* Add a tag `valohai` with value `1`

Once the role is created open the role's **Trust relationships** tab and click **Edit trust relationship**

Paste in the below trust relationship to give Valohai access to this role.

You'll get the username from your Valohai contact.

.. code-block:: json

    {
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::905675611115:user/<USERNAME-FROM-VALOHAI>"
            },
            "Action": "sts:AssumeRole",
            "Condition": {}
            }
        ]
    }
..

Setting up Valohai resources
------------------------------

Below is a list of the AWS resources that are required for the Valohai Private Worker installation.

You can either create these resources yourself, or give `ValohaiMaster` elevated permissions for the duration of the setup.

Option 1) Give Valohai permission to provision the resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the following policies to the `ValohaiMaster` role to give Valohai permission to create the queue instance and setup the networking resources.

* **AmazonEC2FullAccess**
* **AmazonVPCFullAccess**

Option 2) Provision the resources yourself
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

VPC and subnets
^^^^^^^^^^^^^^^^

Create a VPC and subnets per each availability zone you want to use. For example:

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

**Security groups**

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
      - 6379
      - valohai-sg-workers
      - for plain Redis connection from workers
    * - TCP
      - 22
      - 3.251.38.215/32 (during installation)
      - for SSH management from Valohai

**EC2 Instance for queue machine**

Provision an Elastic IP and a EC2 instance for storing the job quue and short term logs.

* Elastic IP from the Amazon pool
    * **Name:** valohai-ip-queue
* EC2 instance works as the queue instace for Valohai. It hosts a Redis server to handle real-time logging and job queues.
    * **Name:** valohai-i-queue
    * **OS:** Ubuntu 20.04 LTS
    * **Machine type:** t3.medium (2 vCPU, 4GB RAM)
    * **Standard persistent disk:** 16GB
    * **Security Group:** valohai-sg-queue
    * **Key Pair**: You'll receive the key pair from your Valohai contact
    * **Tag:** Valohai

Attach the Elastic IP to the new VM instance.

Conclusion
-------------

You should now have the following details:

* Region
* ARN of the ValohaiMaster-role that Valohai can assume

If you created the above mentioned resources yourself, you should also have the following information:

* Name of VPC
* Names of subnets that can be used for Valohai workers
* Public IP of the queue instance
* Private IP of the queue instance


.. seealso:: 

    Each Valohai project has one or more data stores. A data store is a secure place to keep your files; you download training data from there and upload files from your executions there (e.g. models, weights, images).

    It's good practice to setup one S3 Bucket to work as the default bucket for all projects in your organization. Each project owner can then change the bucket if needed, but this way you can ensure that all data ends up in your S3 bucket, instead of the shared Valohai storage.

    `Add AWS S3 to Valohai </tutorials/cloud-storage/private-s3-bucket/>`_
