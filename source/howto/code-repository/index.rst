.. meta::
    :description: In this guide you'll learn to connect your projects to your own code repository.

.. _repository:

Connect to a Git-repository
----------------------------

You can easily connect all of your projects to either a public or a private Git-repository.

.. toctree::
    :titlesonly:
  
    private-github-repository/index
    private-bitbucket-repository/index
    private-gitlab-repository/index

..

.. admonition:: --adhoc executions
    :class: tip

    `valohai-cli </tutorials/valohai-cli/quick-start-cli/>`_ allows you to launch new executions based on your local changes, without having to commit & push the changes to your repository.

    .. code:: bash

        vh exec run --adhoc --watch name-of-your-step

    ..
..
