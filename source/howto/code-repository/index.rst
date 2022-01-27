.. meta::
    :description: In this guide you'll learn to connect your projects to your own code repository.

.. _repository:

Connect to a Git repository
----------------------------

You can easily connect all of your projects to either a public or a private Git-repository.

.. toctree::
    :titlesonly:

    private-github-repository/index
    private-bitbucket-repository/index
    private-gitlab-repository/index
    private-azure-devops-repository/index
    use-multiple-repositories-in-a-project/index

..

.. seealso::

    Are you new to Git? Get started with these resources:

    * `Git for Data Science: What every data scientist should know about Git <https://valohai.com/blog/git-for-data-science/>`_ 
    * `What every data scientist should know about Python dependencies <https://valohai.com/blog/dependency-management-for-data-science/>`_

.. admonition:: --adhoc executions
    :class: tip

    `valohai-cli </tutorials/valohai-cli/quick-start-cli/>`_ allows you to launch new executions based on your local changes, without having to commit & push the changes to your repository.

    .. code:: bash

        vh exec run --adhoc --watch name-of-your-step

    ..
..
