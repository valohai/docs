.. meta::
    :description: Checklist for new users and organizations on Valohai

.. _new-user-guide:

Bring your existing projects to Valohai
#################################################

This guide will cover the common tasks that you need to perform to bring your existing machine learning projects to Valohai.

.. |git| image:: /_icons/git.png 
   :align: middle
   :target: #connect-your-git-repository-to-a-valohai-project
   :width: 48
.. |docker| image:: /_icons/docker.png 
   :align: middle
   :target: #choose-a-docker-image
   :width: 48
.. |yaml| image:: /_icons/yaml.png 
   :align: middle
   :target: /howto/new-user-guide/yaml/
   :width: 48
.. |data| image:: /_icons/data.png 
   :align: middle
   :target: /howto/new-user-guide/code/data/
   :width: 48
.. |metadata| image:: /_icons/metadata.png 
   :align: middle
   :target: /howto/new-user-guide/code/metadata/
   :width: 48
.. |parameters| image:: /_icons/parameters.png 
   :align: middle
   :target: /howto/new-user-guide/code/parameters/
   :width: 48

.. list-table::
   :align: center

   * - |git|
     - |docker|
     - |yaml|
     - |data|
     - |parameters|
     - |metadata|
   * - `Connect to a Git repository <#connect-your-git-repository-to-a-valohai-project>`_
     - `Choose a Docker image <#choose-a-docker-image>`_
     - `Add a valohai.yaml configuration </howto/new-user-guide/yaml/>`_
     - `Use Valohai data inputs/outputs </howto/new-user-guide/code/data/>`_
     - `Define parameters in valohai.yaml </howto/new-user-guide/code/parameters/>`_
     - `Collect key metrics in JSON </howto/new-user-guide/code/metadata/>`_ 

    
.. admonition:: Environments and Data Stores
    :class: warning

    This guide assumes that your organization has the environments and data stores configured already as a part of the Valohai installation.

    * How to :ref:`cloud-storage`
    * How to :ref:`setup`


.. raw:: html

    <div style="position: relative; padding-bottom: 53.57142857142857%; height: 0;"><iframe src="https://www.loom.com/embed/bd2ec4766f7e43e89d4533f6023564b2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>



Connect your Git repository to a Valohai project
-------------------------------------------------

Start by going to the Valohai application (`app.valohai.com <https://app.valohai.com>`_) and creating a new project.

The owner of the project should be your organization or team, so that you can access your organizations cloud resources like virtual machines, data stores, and private Docker registries.

After you've created the project you'll need to connect it to a Git repository through the Repository tab in your project's settings.


.. list-table::

   * - :ref:`repository-github`
     - :ref:`repository-bitbucket`
     - :ref:`repository-gitlab`

.. admonition:: Are you new to Git?
    :class: tip

    Get started with these resources:

    * `Videos to help you get started with Git <https://git-scm.com/videos>`_ 
    * `Git Handbook by GitHub <https://guides.github.com/introduction/git-handbook/>`_ 
    * `Learn Git with the Bitbucket Cloud <https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud>`_ 
    * You can also get the entire `Pro Git <https://git-scm.com/book/en/v2>`_ book


Install Valohai tools
----------------------

Valohai offers command-line tools and a Python helper library to make it easier to interact with the platform.

* :ref:`cli` allows you to easily run jobs, view logs, and create new projects directly from the cli.
* :ref:`valohai-utils` is a Python utility library that helps with everyday boilerplate.

Start by installing the Valohai tools, logging in, and linking your local directory to a Valohai project.

.. code-block:: bash

  pip3 install valohai-utils valohai-cli
  vh login
  
  # Navigate to your project
  cd myproject

  # Links your current working directory to a existing Valohai project
  vh project link


.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    yaml
    code/data
    code/parameters
    code/metadata

Choose a Docker image
----------------------

Each Valohai execution is ran inside a Docker container. This makes it possible to execute any code from C to Python as long as it can run inside the chosen container.

You can use any Docker images for your Valohai jobs, either from a public or a private Docker registry.

.. include:: /_partials/_image-list.rst

You can also install any additional libraries inside the execution with for example ``apt-get install`` or ``pip install -r requirements.txt``.

.. admonition:: Custom Docker images
    :class: tip

    Having a custom Docker image allows you to bake in all the libraries and other dependencies that your machine learning code has. This way you don't need to spend time running additional installation commands in the beginning of every execution to get everything you need.
    
    Valohai will download and cache the Docker images on the worker virtual machine, so they don't hae to be redownloaded for every job.

.. seealso::

    * `Access a private Docker repository </howto/docker-private-registry/>`_ 
    * `Build a custom Docker image </howto/docker-build-image/>`_ 

Next
----

To get the most out of Valohai features you should integrate with Valohai input/output data, parameters, and metadata system. Follow the guides below for details:

.. list-table::
   :widths: 15 65 20
   :stub-columns: 1
   :header-rows: 1

   * - Topic
     - Why
     - Guide
   * - Configuration file
     - 
       * Valohai expects that you have a ``valohai.yaml`` configuration file in the root of your repository. The file defines what kind of jobs can be executed inside your project, and the different properties of each job type (= :ref:`step`). 
     - :ref:`new-user-guide-yaml`
   * - Files
     - 
       * Data scientists don't need to worry about authenticating with your cloud object store, downloading/uploading files, and caching data.
       * In Valohai you always treat files from an object store as "local files". Valohai downloads your data to a local directory in ``/valohai/inputs/``. It will pick up any files from ``/valohai/outputs/`` and upload them to your private cloud storage.
     - :ref:`migrate-data`
   * - Parameters
     - 
       * Keep track of parameters used in your executions, and rerun any job with the same or changed parameter values.
       * Easily run parameter sweeps or hyperparameter optimization by using Valohai Tasks.
     - :ref:`migrate-parameters`
   * - Metrics
     - 
       * Easily keep track, compare, and sort your jobs based on custom metrics that you collect.
       * Visualize and compare execution metrics in a time series graph, a scatter plot, or a confusion matrix. 
     - :ref:`migrate-metadata`