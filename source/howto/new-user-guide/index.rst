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
     - |metadata|
     - |parameters|
   * - Connect to a Git repository
     - Choose a Docker image
     - Add a ``valohai.yaml`` configuration
     - Use Valohai data inputs/outputs
     - Collect key metrics in JSON
     - Define parameters in ``valohai.yaml``



    
.. admonition:: Environments and Data Stores
    :class: warning

    This guide assumes that your organization has the environments and data stores configured already as a part of the Valohai installation.

    * How to :ref:`cloud-storage`
    * How to :ref:`setup`


Connect your Git repository to a Valohai project
-------------------------------------------------

Start by going to the Valohai application (`app.valohai.com <https://app.valohai.com>`_) creating a new project.

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

* :ref:`valohai-utils` is a Python utility library that helps with everyday boilerplate.
* :ref:`cli` allows you to easily run jobs, view logs, and create new projects directly from the cli.

Start by installing valohai-utils, logging in, and creating a project.

.. code-block:: bash

  pip3 install valohai-utils
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
    code/metadata
    code/parameters

Choose a Docker image
----------------------

Each Valohai execution is ran inside a Docker image. This makes it possible to run any code from C to Python as long as it can run inside a Docker container.

You can use any Docker images for your Valohai jobs, either from a public or a private Docker registry.

.. include:: /_partials/_image-list.rst

You can also any additional libraries inside the execution, by for example ``apt-get install`` or ``pip install -r requirements.txt``.

.. admonition:: Custom Docker images
    :class: tip

    Having a custom Docker image allows you to bake in all the libraries and other dependencies that your machine learning code has. This way you don't need to spend time running additional installation commands in the beginning of every execution to get everything you need.
    
    Valohai will download and cache the Docker images, so it isn't redownloaded for every single job.

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
       * In Valohai you always treat files from an object store as "local files". Valohai downloads your data to a local directory in ``/valohai/inputs/`` and it will pick up any files ``/valohai/outputs/`` and upload them to your private cloud storage.
     - :ref:`migrate-data`
   * - Metrics
     - 
       * Easily keep track, compare, and sort your jobs based on customer metrics that you collect.
       * Visualize and compare execution metrics in a time series graph, scatter plot, or a confusion matrix. 
     - :ref:`migrate-metadata`
   * - Parameters
     - 
       * Keep track of parameters used in your executions, and rerun any job with the same or changed parameter values.
       * Easily run parameter sweeps or hyperparameter optimization using Valohai Tasks.
     - :ref:`migrate-parameters`