.. meta::
    :description: Selecting compute instances for Valohai

*********************************************
Selecting Compute Instances
*********************************************

Depending on what kind of models you are training you will need virtual machines with different CPU, memory, and GPU configurations. The list of environments available to your subscription can be updated at any time by our support team. You can enable/disable and change the (min/max) scaling rules of each environment type directly in your Valohai settings.

Note that Valohai will only be able to create these machine types, if they're available from the cloud provider in a selected region and your quota limit permits creating additional instances.

* `Amazon EC2 Instance Types <https://aws.amazon.com/ec2/instance-types/>`_
* `Google Compute Engine Instance Type <https://cloud.google.com/compute/docs/machine-types>`_
* `Azure Linux Virtual Machine Pricing <https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/>`_

If you haven't been using cloud instances for your training jobs previously, you can proceed with selecting the instance types from our example configurations below:

☁️  Amazon Web Services
###############################

Check out the full list at `Amazon EC2 Instance Types <https://aws.amazon.com/ec2/instance-types/>`_

* **C5 - Designed for compute-intensive workloads with cost-effective high performance**
    * c5.xlarge *- 4 vCPUs and 8GB memory*
    * c5.2xlarge *- 8 vCPUs and 16GB memory*
    * c5.4xlarge *- 16 vCPUs and 32GB memory*
* **Powerful, Scalable GPU instances**
    * p2.xlarge *- 4 vCPUs, 61GB memory and 1 x NVIDIA K80*
    * p3.2xlarge *- 8 vCPUs, 61GB memory and 1 x NVIDIA Tesla V100*
    * g3.4xlarge *- 16 vCPUs, 122GB memory and 1 x NVIDIA Tesla M60*
* **R4 - Memory optimized instances**
    * r4.4xlarge *- 16 vCPUs and 122GB memory*
    * r4.8xlarge *- 32 vCPUs and 244GB memory*
* **M5 - Balanced compute, memory, and networking resources for general purpose workload**
    * m5.2xlarge  *- 8 vCPUs and 32GB memory*

☁️ Google Cloud Platform
###############################

Valohai creates custom machine types in your Google Cloud Subscription. You can provision machines of any configration that Google Cloud supports.

Check out the full list at `Google Compute Engine Instance Type <https://cloud.google.com/compute/docs/machine-types>`_

* **Custom compute instances**

    * Custom machine with 4 vCPUs 15GB memory
    * Custom machine with 16 vCPUs 64GB memory

* **Powerful, Scalable GPU instances**

    * Custom machine with 4 vCPUs, 15GB memory, 1 x NVIDIA Tesla K80
    * Custom machine with 4 vCPUs, 15GB memory, 1 x NVIDIA Tesla T4
    * Custom machine with 12 vCPUs, 64GB memory and 1 x NVIDIA Tesla P100
    * Custom machine with  12 vCPUs, 64GB memory and 1 x NVIDIA Tesla V100.

Valohai also supports running executions on TPU machines in GCP.

☁️ Microsoft Azure
###############################

Check out the full list at `Azure Linux Virtual Machine Pricing <https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/>`_

* **The Fsv2-series** virtual machines are optimized for compute intensive workloads
    * F8s v2 *- 8 vCPUs and 16GB memory*
    * F16s v2  *- 16 vCPUs and 32GB memory*
* **Powerful, Scalable GPU instances**
    * NC6 *- 6 vCPUs, 56GB memory and 1 x NVIDIA Tesla K80*
    * NC12 *- 12 vCPUs, 112GB memory and 2 x NVIDIA Tesla K80*
    * NC6s v2  *- 6 vCPUs, 112GB memory and 1 x NVIDIA Tesla P100*
    * NC12s v2  *- 12 vCPUs, 224GB memory and 2 x NVIDIA Tesla P100*
    * NV6 *- 6 vCPUs, 56GB memory and 1 x NVIDIA Tesla M60*
    * NV12 *- 12 vCPUs, 112GB memory and 2 x NVIDIA Tesla M60*
* **The Dv3-series** sizes offer a combination of vCPU(s), memory, and local disk well suited for most production workloads.
    * D2 v3 *- 2 vCPUs and 8GB memory*
    * D4 v3 *- 4 vCPUs and 16GB memory*
    * D8 v3 *- 8 vCPUs and 32GB memory*
