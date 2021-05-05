.. meta::
    :description: How to use access multiple Git repositories from a single Valohai project.

Access multiple Git repositories in a project
==================================================

.. admonition:: Prerequisites
    :class: warning

    This guide assumes that you're familiar with Git, generating SSH keys and connecting a Git repository to your Valohai project. If you're not familiar with these see our guide on :ref:`repository`

..

.. toctree::
    :hidden:

    clone-repository-during-execution

..

Each Valohai project can be connected to one Git repository at a time.

Sometimes you might need to access another repository from your Valohai project. This could be because you're developing a library seperately in another Git repository or have some other files that you need to access from another seperate repository, while keeping the two projects seperate.

.. seealso::

    * `What are Git submodules? <https://git-scm.com/book/en/v2/Git-Tools-Submodules>`_
    * **TL;DR** Submodules allow you to keep a Git repository as a subdirectory of another Git repository. This lets you clone another repository into your project and keep your commits separate.
    * In some cases submodules might not be the right choice for you. In this case you can `clone another Git repository to your Valohai execution inside an execution </howto/code-repository/use-multiple-repositories-in-a-project/clone-repository-during-execution>`_.


Add a submodule to your Git repository
#############################################

.. admonition:: Private submodules
    :class: warning

    Make sure the URL of the submodule is in the following format `git@mygitprovider.com:<username>/<repository>.git`.

    Valohai won't be able to fetch a private submodule using the HTTPS address.

..

You can add a new submodule with `git submodule add`.

.. code-block:: bash

    git submodule add git@mygitprovider.com:<username>/<repository>.git
    git add .
    git commit -m "Added submodule"
    git push

..

Configure access for Valohai
##################################

You'll need to provide Valohai access to both the main repository and all the submodule repositories.

You can provide only one SSH key in the Valohai project's settings. Make sure this key has access to all the required repositories.

GitHub
^^^^^^^^^

When using repositories that don't have a submodule you can generate a deploy key and add it to your Valohai project.

GitHub allows a deploy key to be used only in one project at a time. This means that you can't use the same deploy key in your main repository and in your submodule repositories.

To allow Valohai to fetch a repository with submodules you'll need to:

1. `Generate and add a new SSH key to your GitHub profile <https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account>`_
2. Go to your Valohai project settings link the main repository using the generated SSH Key.

You can now fetch the repository and it's submodules on Valohai.

GitLab
^^^^^^^^^^

GitLab allows you generate a deploy key and use it across multiple repositories.

1. If you haven't already, follow the :ref:`repository-gitlab` guide to create a deploy key for your main repository
2. On Gitlab open the repository of the submodules project
3. Open Project -> Settings -> Repository -> Deploy keys
4. Open the **Privately accessible deploy keys** tab
5. Enable the key you're using in your main repository

You can now fetch the repository and it's submodules on Valohai.

Bitbucket
^^^^^^^^^^

1. If you haven't already, follow the :ref:`repository-bitbucket` guide to create a deploy key for your main repository
2. Add the same deploy key to the other repository that you're using as a submodule

You can now fetch the repository and it's submodules on Valohai.