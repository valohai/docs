.. meta::
    :description: In this guide you'll learn to connect your projects to your own code repository.

Connect to a code repository
----------------------------

You can easily connect all of your projects to either a public or a private Git repository. Having a repository linked to a project will allow you to easily reproduce your experiments with the exact code and configuration files used in your commit.

.. toctree::
    :titlesonly:


    private-github-repository/index
    private-bitbucket-repository/index
    private-gitlab-repository/index

..

.. note:: 

    The commit’s contents will be available at **/valohai/repository**, which is also the default working directory during executions.

..

.. note::

    You don't necessarily need to commit and push after each code change. The Valohai command-line client allows creating one-off executions from local files. These ad-hoc executions allow quick iteration with the platform when you are still developing your whole pipeline.

    .. code:: bash

        $ vh exec run --adhoc --watch name-of-your-step
        #sends project source code to a worker and runs commands in valohai.yaml

    ..
..

.. seealso::

    * `valohai-cli - command line client <https://docs.valohai.com/valohai-cli/>`_ 
    * `valohai.yaml - Config file <https://docs.valohai.com/valohai-yaml/>`_ 

..