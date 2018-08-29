.. meta::
    :description: Frequently asked questions about the Valohai machine learning platform. Contact us if you can’t find an answer to your question.

Frequently Asked Questions
==========================

How to fix "Missing step configuration file valohai.yaml"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your source code repository must contain a ``valohai.yaml`` file at the root of the repository
that defines how and in which kind of runtime environment your experiments are run.

For instance, here is a ``valohai.yaml`` file that lists runtime contents of your repository for debugging purposes.

.. code-block:: yaml

   ---

   - step:
       name: Show contents of my repository
       image: busybox
       command: ls -la /valohai/repository

See :doc:`valohai.yaml documentation </valohai-yaml>` for more details.

How to define that my execution failed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``command`` is considered to be successful if it returns error code 0. This is the default
convention for most programs and scripting languages.

The platform will mark an execution as crashed if any of the commands returns any other error code.

The best approach to log what went wrong is to use stderr which is visible on the execution **Logs** tab.

How to pass command parameters in ``Rscript myscript.r arg1 arg2`` format?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You define how the parameters are passed in the ``parameters`` section in ``valohai.yaml``.

The default syntax is ``--{name}={value}`` so:

.. code-block:: yaml

   - name: dropout
     pass-as: '--dropout={v}'

To achieve the syntax mentioned in the question, add or modify the ``pass-as`` property:

.. code-block:: yaml

   - name: dropout
     pass-as: '{v}'

See the :doc:`valohai.yaml documentation </valohai-yaml>` for more details.

How do I upload files from my executions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Anything written to the ``/valohai/outputs`` directory will be uploaded and accessible after the execution.

The files are uploaded into a user-specific section of our AWS S3 bucket by default, but you can customize this.

.. seealso:: :doc:`guides/private-s3-bucket`
