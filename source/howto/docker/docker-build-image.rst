.. meta::
    :description: Build your own Docker images to run custom machine learning code on scalable deep learning infrastructure.

.. _docker-build:

Build your own Docker image
################################

In this tutorial, we'll build a Docker image to be used as a runtime environment on Valohai.

Building images is frequently optional, but is recommended especially when...

1. ... your runtime setup takes longer than a couple of minutes (``apt-get install``, etc.)
2. ... you want to use Valohai backend for iterative machine learning development where you start an execution with ``vh exec run`` and it'll start running under a second

.. tip::

    If you don't wish to maintain your own Docker images, you can find images for the most popular machine learning frameworks on `Docker Hub <https://hub.docker.com/>`_.

.. admonition:: Prerequirements
    :class: attention

    For this tutorial you will need:

    * Docker CE (Community Edition)

    How to install Docker CE:

    * macOS: `Docker Desktop for Mac <https://docs.docker.com/docker-for-mac/install/>`_
    * Windows: `Docker Desktop for Windows <https://docs.docker.com/docker-for-windows/install/>`_
    * Other: use package management software of your choice e.g. `Get Docker for Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`_

Choose a base image
-----------------------

First, we need to choose a base image to build the Docker image upon.

.. important::

    Add the following environment variables to your custom Docker images to make sure the Valohai execution can access the GPU.
    
    ``ENV NVIDIA_VISIBLE_DEVICES all``
    
    ``ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility``

It's wise to choose a Docker image that contains the core libraries you are using; for example:

* `nvidia/cuda <https://hub.docker.com/r/nvidia/cuda>`_
* `tensorflow/tensorflow <https://hub.docker.com/r/tensorflow/tensorflow>`_
* `pytorch/pytorch <https://hub.docker.com/r/pytorch/pytorch>`_
* `microsoft/cntk <https://hub.docker.com/r/microsoft/cntk>`_
* `mxnet/python <https://hub.docker.com/r/mxnet/python>`_
* `ufoym/deepo <https://hub.docker.com/r/ufoym/deepo/>`_ (includes all common ML libraries)

Also make effort to check out what kind of image variants do the repository host under the ``Tags`` tab. For example, `nvidia/cuda tags <https://hub.docker.com/r/nvidia/cuda/tags>`_ include various CUDNN versions and Ubuntu versions. Docker Hub image repository ``Overview`` tab usually contains information what different tags mean.

If you choose a machine learning framework Docker base image such as ``tensorflow/tensorflow``, make sure that variant includes GPU support if you plan on using GPUs, like ``tensorflow/tensorflow:1.12.0-gpu-py3`` where the ``gpu`` part tells that it has been built on top of ``nvidia/cuda``, enabling GPU access.

**By the end of this step**, you should end up with a base Docker image that closest resembles your project stack e.g. ``nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04`` or ``tensorflow/tensorflow:1.12.0-gpu-py3``.

Write build instructions - Dockerfile
----------------------------------------------

As an example, we'll be creating a Docker image that utilizes GPUs with TensorFlow. In the real world, you would want to use ``tensorflow/tensorflow`` in a simple situation like this.

Docker images are build with Dockerfiles that specify the steps how to build the image. More information about Dockerfile syntax at `Dockerfile reference <https://docs.docker.com/engine/reference/builder/>`_.

Write the following into a file called ``Dockerfile`` (without extension). You can place this anywhere on your machine.

Below you'll see two examples of a Dockerfile.


Example 1) Custom image based on ``tensorflow/tensorflow``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example we'll create a new image based on the official Tensorflow image and add our own requirements.txt on top of that. This way our Docker image will already have our requirements inside it, and we don't have to install them seperately during the execution.

.. note::

    We're using ``tensorflow/tensorflow`` here but you can use any other image as a base image.


* Start by finding the right base image from hub.docker.com
* For our example, we'll use ``tensorflow/tensorflow:2.2.3-gpu`` as the base image. You can find all the TensorFlow images under the **Tags** page on https://hub.docker.com/r/tensorflow/tensorflow/tags
* The sample below assumes that there is a ``requirements.txt`` file in the same directory as the ``Dockerfile``

.. code-block:: Dockerfile

    # Our base image
    FROM tensorflow/tensorflow:2.2.3-gpu

    # Copy the requirements.txt file to our Docker image
    ADD requirements.txt .

    # Install the requirements.txt
    RUN pip install -r requirements.txt


Example 2) Custom image based on ``nvidia/cuda``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: Dockerfile

    # Our base image
    FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04

    # Some common environmenta variables that Python uses
    ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

    # Install lower level dependencies
    RUN apt-get update --fix-missing && \
        apt-get install -y curl python3 python3-pip && \
        update-alternatives --install /usr/bin/python python /usr/bin/python3 10 && \
        update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10 && \
        apt-get clean && \
        apt-get autoremove && \
        rm -rf /var/lib/apt/lists/*

    ENV NVIDIA_VISIBLE_DEVICES all
    ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility

    # Install a specific version of TensorFlow
    # You may also install anything else from pip like this
    RUN pip install --no-cache-dir tensorflow-gpu==1.12.0


Build the image
--------------------

The run the following commands to name and build the image.

.. code-block:: bash

    docker build -t my-name/my-image:1.12.0 .

    # now you can run commands in your brand new Docker image to try it out
    docker run --rm -i -t my-name/my-image:1.12.0 python --version  # => Python 3.5.2

.. note::

    If you are using ``nvidia/cuda`` base image, you might be required to use Linux with kernel version >3.10 to work with the images. You need to have `nvidia-docker <https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)>`_ installed.

Now you have your own Docker image! Next we'll host it somewhere for later use.


Host the image
-----------------------

We recommend hosting your images on `Docker Hub <https://hub.docker.com/>`_ if there is nothing secret about your dependencies. Just create an account and login using the ``Docker Desktop`` app or the command-line client.

On Docker Hub, create repository using the ``Create Repository`` button on the `dashboard <https://hub.docker.com/>`_. Give it a descriptive name like ``my-image`` like we have been using in this example ;)

.. code-block:: bash

    # in-case you need to rename your image at this point...
    docker tag my-name/my-image:1.12.0 actual-account/my-image:1.12.0
    docker rmi my-name/my-image:1.12.0

    # and finally push the Docker image to the repository
    docker push actual-account/my-image:1.12.0

And now you finally have a publicly available Docker image ``actual-account/my-image:1.12.0`` you can use on Valohai or anywhere else!
