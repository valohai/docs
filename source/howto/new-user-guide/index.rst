.. meta::
    :description: Checklist for new users and organizations on Valohai

.. _new-user-guide:

Bring your existing projects to Valohai
#################################################

This document helps you get started with bringing your team and projects to Valohai.


1. Configure Valohai resources
----------------------------------

#. `Configure your own data store </howto/data/cloud-storage/>`_
#. `Configure your execution environments and scaling rules </howto/organization/environments/>`_
#. `Invite colleagues to Valohai </howto/organization/user-management/>`_

2. Connect your project to Git
----------------------------------

#. Create a Git repository and add your code to Git 
#. Create a new project in Valohai
#. Connect your Git repository to Valohai (`how to </howto/code-repository/>`_)

.. seealso::

    Are you new to Git? Get started with these resources:

    * `Videos to help you get started with Git <https://git-scm.com/videos>`_ 
    * `Git Handbook by GitHub <https://guides.github.com/introduction/git-handbook/>`_ 
    * `Learn Git with the Bitbucket Cloud <https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud>`_ 
    * You can also get the entire `Pro Git <https://git-scm.com/book/en/v2>`_ book


3. Get your code ready for Valohai
-------------------------------------

Valohai is completely technology agnostic. You can develop in notebooks, scripts or shared git projects in any language or framework of your choice.

Valohai requires a :ref:`yaml` at the root of your Git-repository.

.. toctree::
    :titlesonly:
    :maxdepth: 1

    code/data
    code/metadata
    code/parameters


.. seealso::

    * `Access a private Docker repository </howto/docker-private-registry/>`_ 
    * `Define pipelines </reference-guides/valohai-yaml/pipeline/>`_ 
    * `Schedule pipelines </howto/pipelines/triggers/>`_ 
    * `Set notifications with webhooks </howto/notifications/webhook/>`_ 
