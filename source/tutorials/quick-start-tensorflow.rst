Quick start - TensorFlow
------------------------

In this guide we will create a TensorFlow machine learning project based on our
`MNIST TensorFlow example on GitHub <https://github.com/valohai/tensorflow-example>`_
and run a simple training with it.

.. contents::
   :backlinks: none
   :local:

1. Sign in
~~~~~~~~~~

Sign up and sign in to `the Valohai platform <https://app.valohai.com/>`_.

2. Create a project
~~~~~~~~~~~~~~~~~~~

1. Go to the Valohai platform `front page <https://app.valohai.com/>`_ after signing in

.. container:: tips

   If you haven't created any projects before, you'll be greeted by message
   "Get started by importing a tutorial project based on our TensorFlow example.".
   You can optionally select **Import TensorFlow tutorial project** and skip straight to
   :ref:`create-tensorflow-execution`.

2. Press the **Create Project...** button
3. Set a ``Name`` for your project, e.g. *test-tensorflow*
4. You can leave ``Description`` blank, that is more in detail definition of your project
5. Press the **Create** button

3. Define version control repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A valid source repository must contain a ``valohai.yaml`` configuration file that defines
how your machine learning code is run.

Let's setup a repository for your project:

#. Go to the example repository page on GitHub: https://github.com/valohai/tensorflow-example

   #. If you want to modify the training code, you can fork the repository first.

#. Copy the **HTTPS** URL of the repository e.g. `https://github.com/valohai/tensorflow-example.git`
#. Go to the **Repository** tab inside your new project to set your source repository
#. Paste the URL above to the ``URL`` field on the **Repository** tab
#. Leave ``Fetch reference`` as the default value `master`
#. ``SSH private key`` is only required if your Git repository is private
#. Press the **Save** button

4. Fetch the latest code
~~~~~~~~~~~~~~~~~~~~~~~~

Fetch the latest code commit using the **Fetch repository** button at the top right.

.. _create-tensorflow-execution:

5. Create an execution
~~~~~~~~~~~~~~~~~~~~~~

1. Go to the **Executions** tab inside your project
2. Press the **Create execution** button
3. The ``Step`` field lists all available types of executions. Make sure **Train model** is selected.
4. You don't need to worry about the rest of the configuration for now.
   The default inputs and parameters of the form are loaded from the ``valohai.yaml`` configuration file
   and should be good for this example execution.
5. Press **Submit** to start the execution.

6. View the results
~~~~~~~~~~~~~~~~~~~

After you start the execution, you are forwarded to the execution page.

This page has several tabs with execution details:

The **Information** tab shows the basic information about the execution, most of which could've been modified in
the previous execution creation step.

The **Log** tab shows real-time log output from the execution.
Anything that your code prints to the standard output (stdout) or standard error (stderr) streams is shown here.

The **Metadata** tab shows all the metadata output from the execution.
You can also plot the metadata on a line chart.
Metadata is any data your execution writes to the standard output stream in JSON which we can parse.
If no plottable metadata has been output, this tab is not visible.

The **Output** tab contains download links for all the output artifacts created by the execution.
The execution defines these outputs by writing them into ``/valohai/outputs`` directory.
The artifacts are stored in AWS S3.
If the execution has not finished, or did not output any files, this tab will not be visible.
