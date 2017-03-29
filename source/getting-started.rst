Getting started
---------------

After signing up for the Valohai platform, the rough steps for running
an experiment are as follows:

1. Create a new project
2. Define version control repository
3. Fetch the latest commit
4. Create a new execution
5. Run the execution and view results as they come in

1. Create a new project
~~~~~~~~~~~~~~~~~~~~~~~

From the front page of the Valohai platform, select *Create Project...*

``Name``: Letters, numbers, hyphens and underscores are allowed.

``Description``: Optional.

2. Define version control repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to the *Repository* tab to define your where your machine learning
code is.

``URL``: Version control repository that contains your machine learning
code. Currently supported protocols are ``git+https`` and ``git+ssh``.

``Fetch reference``: Which branch and/or commit from the repository you
want to use.

``SSH private key``: If the repository is private, use ``git+ssh`` and
define a private SSH key here. Otherwise optional.

3. Fetch the latest commit
~~~~~~~~~~~~~~~~~~~~~~~~~~

Fetch the latest commit using the *Fetch repository* button.

4. Create a new execution
~~~~~~~~~~~~~~~~~~~~~~~~~

From the project page press *Create execution*.

The default values, inputs and parameters of the create execution form
are loaded from the ``valohai.yaml`` configuration file.

An execution runs one of the defined steps at once.

``Environment``: The AWS environment you want to run the step in.

``Commit``: A list of all the fetched commits. By default the latest
fetched commit is selected.

``Step``: A list of all the steps in the configuration while. By default
the first one is selected.

``Image``: The Docker image under which the step is executed.

``Command``: One or more commands which define what will be executed in
this step.

Inputs:
^^^^^^^

Inputs are data that is available during step execution.

``URL``: Where the input will be loaded from. Currently valid sources
are HTTP and HTTPS URLs. For these basic access authentication is
supported.

Optional inputs are have (optional) after the input name. Their ``URL``
can be empty.

Parameters:
^^^^^^^^^^^

Parameters can be accessed from the code and used to modify the
execution at runtime.

``Value``: Value for the parameter.

Optional parameters are have (optional) after the parameter name. Their
``Value`` can be empty.

5. Run the execution and view results as they come in
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you start the execution, you are forwarded to the execution page.
This page has several tabs with execution details.

The *Information* tab shows the basic information about the execution,
which came from the ``valohai.yaml`` configuration file and which you
might've modified in the create execution form.

The *Log* tab shows a live log output from the execution is shown.

The *Metadata* tab shows all the metadata output from the execution. You
can also plot the metadata on a simple two-axis chart. Metadata is any
data your execution writes to the standard output in JSON which we can
parse.

The *Output* tab contains a list and download links for all the output
artifacts created by the execution. The execution creates these
artifacts by writing them into ``/valohai/output``. The artifacts are
store in AWS S3.
