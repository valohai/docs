.. meta::
    :description: Frequently asked questions about the Valohai machine learning platform. Contact us if you can’t find an answer to your question.

Frequently Asked Questions
==========================

Can you explain me your fees compared to AWS/GCP/Azure?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SaaS plan users are billed essentially the on-demand pricing of the chosen cloud provider, billed per-second, which varies by provider and region. You can follow this on the Valohai web app.

But you to pay less than you would normally because Valohai only bills you when your code has started running on the machine (in addition to the time it takes to download the Docker image and inputs). We don't bill for the instance boot time, if there is any, and of course, we shut down the servers automatically for you so they don't hang around.

Private installation users (Enterprise plan) are not billed extra of the resources they use as they already get billed by the respective cloud provider where we setup the installation.

If you are part of our non-free level plans, you get billed on monthly basis according to https://valohai.com/pricing/ or separately signed Enterprise contract.

How to pass parameters in ``Rscript myscript.r arg1 arg2`` format?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You define how the parameters are passed in the ``parameters`` section in ``valohai.yaml``.

The default syntax is ``--{name}={value}`` so:

.. code-block:: yaml

   - name: dropout
     pass-as: '--dropout={v}'

To achieve the syntax mentioned in the question, add or modify the ``pass-as`` property:

.. code-block:: yaml

   - name: dropout
     pass-as: '{v}'

See the :doc:`valohai.yaml documentation </valohai-yaml/index>` for more details.

How do I upload files from my executions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Anything written to the ``/valohai/outputs`` directory will be uploaded and accessible after the execution.

The files are uploaded into a user-specific section of our AWS S3 bucket by default, but you can customize this.

.. seealso::

    * :doc:`guides/private-azure-storage`
    * :doc:`guides/private-s3-bucket`
    * :doc:`guides/private-swift-container`

Do I need to commit and push after each code change?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not necessarily, Valohai command-line client allows creating one-off executions from local files.
These ad-hoc executions allow quick iteration with the platform when you are still developing your whole pipeline.

.. code-block:: bash

    $ vh exec run --adhoc --watch name-of-your-step
    # sends project source code to a worker and runs commands in valohai.yaml

Although, we do strongly recommend using all production code through version control.

.. seealso::

    :doc:`tutorials/quick-start-cli`

I should be able to ignore ``venv/``, ``datasets/`` or other specific files in the same folder structure as ``valohai.yaml`` when using the command-line client. It takes forever to launch adhoc executions!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can! Our command-line client ignores everything that git ignores so just add those to your ``.gitignore`` and you are good to go.

There is some redundancy between the command-line arguments defined on the ``train.py`` , on the ``valohai.yaml`` and the command-line client.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yup, we've noticed the same nuisance with redundant definitions in e.g. Python ``argparse`` definitions and what we define in the YAML file. As we support essentially any programming language or arbitrary command-line tool already installed on the Docker images it is hard to remove this redundancy, unfortunately.

What is the maximum number of trainings I can do at the same time?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a configurable setting per-instance-type with the default of 5 parallel executions on most environments. If you require more, let us know and we'll see what we can do.

If you launch more executions than you have quota for, we will properly queue everything so executions do get ran when the previous ones finish.

Of course, if you are running Valohai on your own infrastructure, there are no limits except the cloud provider quota on your account.

How to define that my execution failed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The individual command is considered to be successful if it returns error code 0. This is the standard
convention for most programs and operating systems.

Valohai will mark an execution as a failure if *the last* commands returns any other code than 0.

The best approach to communicate what went wrong is to use ``STDERR`` which is visible on the execution **Logs** tab.

Why Python output looks as errors on logs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Everything written to ``STDOUT`` should be white, and everything written to ``STDERR`` should be yellow. So if you see yellow text, then some library is writing to ``STDERR``. For example, TensorFlow ``tf.Print`` used to log to ``STDERR`` by default.

To fix this, you need to check the relevant framework that is producing the log and see how to make it log to ``STDOUT``.

How can I do so that there are multiple ``valohai.yaml`` for different folders in a repo so that I don't have to split my different models in different repos?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the time being, the easiest way to do this would be defining them all in the same ``valohai.yaml`` and just create more steps in there. We have currently no plans to change this behavior as it can get messy fast. We feel it is nicer to have all the Valohai specific configuration in one place.
