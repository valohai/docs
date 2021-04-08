.. meta::
    :description: What are Valohai projects? Create a context where to work and collaborate on deep learning problems.

Projects
#########

You work and collaborate on **projects**; a project is a space for tackling a specific machine learning problem or domain.
If you have used GitHub, projects in Valohai are a lot like code repositories.

A project is linked to a remote git repository. You can use any git hosting service, not just GitHub but also e.g. BitBucket and GitLab.

Each of these linked repositories include a :doc:`valohai.yaml configuration file </reference-guides/valohai-yaml/index>` that defines what kind of "runs" can be executed in the context of that project.

Here are more in-depth example repositories which have ``valohai.yaml`` defined:

* https://github.com/valohai/tensorflow-example
* https://github.com/valohai/keras-example
* https://github.com/valohai/darknet-example
* https://github.com/valohai/cntk-example
* https://github.com/valohai/r-example
* https://github.com/valohai/mxnet-example
* https://github.com/valohai/integration-example

We also have `quick start tutorials </howto/example-project/index>`_ to get you started right away.


.. admonition:: See also
    :class: tip

    Iterative experimentation is also supported using our ``vh`` command-line client, try out :doc:`our quick start command-line client tutorial </tutorials/valohai-cli/index>` to get a taste how it works.

Project ownership
------------------

Projects can be owner by a individual user, an organization or by a team inside an organize. The project ownership defines who has access to the project, data outputs etc.

You can easily add new `Collaborators` to a project, to invite individual users who are not part of the original ownership scope. For example an external partner, end-customer or someone from the organization who is not part of the team that owns the project.
