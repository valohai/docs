.. meta::
    :description: How to manually deploy Valohai resources in your AWS environment

.. _aws-hybrid:


Deploy to AWS
##############

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    manual
    faq

.. include:: _intro.rst

Deploying resources
-----------------------

You can easily deploy a Valohai to a fresh AWS Account using the provided CloudFormation template, or by using Terraform.

.. image:: /_images/cloudformation_btn.png
    :width: 200
    :alt: Deploy with CloudFormation
    :target: https://github.com/valohai/aws-hybrid-workers-cloudformation

.. image:: /_images/terraform_btn.png
    :width: 200
    :alt: Deploy with Terraform
    :target: https://github.com/valohai/aws-hybrid-workers-terraform

* Deploy with `CloudFormation <https://github.com/valohai/aws-hybrid-workers-cloudformation>`_
* Deploy with `Terraform  <https://github.com/valohai/aws-hybrid-workers-terraform>`_


You can also follow our manual step-by-step guide, if you don't want to use the templates: :ref:`aws-hybrid-manual`

.. seealso::

    Need to run Valohai completely inside your own network? See the guide `Deploy a self-hosted Valohai </howto/setup/self-hosted/>`_ 

Architecture
--------------

Below is an example of a possible Valohai deployment:

* The example below contains RDS and RedShift as example data storages. Valohai doesn't require 
* By default Valohai will use only a single S3 Bucket (``valohai-data-1234``) but organization admins can configure additional data stores in-app, for example different data stores for different projects.
* The example below shows only two types of workers (``p2.xlarge`` and ``g4dn.4xlarge``) as examples. You will be able to use any instance types that you have AWS quota for.
* Each Valohai execution is ran inside a Docker container. The base image for the execution can be fetched either from a public repository, or a private repository like ECR.

.. thumbnail:: /_images/valohai_aws_hybrid.jpeg
    :width: 700
    :alt: Valohai Hybrid Deployment on AWS
