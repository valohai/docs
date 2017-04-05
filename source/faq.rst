Frequently asked questions
==========================

I'm getting "Missing step configuration file valohai.yaml" error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your source code repository must contain a ``valohai.yaml`` file at the root of the repository
that defines how and in which kind of runtime environment your experiments are ran.

For instance, here is a ``valohai.yaml`` file that lists runtime contents of your repository for debugging purposes.

.. code-block:: yaml

   ---

   - step:
       name: Show contents of my repository
       image: busybox
       command: ls -la /valohai/repository

See :doc:`valohai.yaml documentation </valohai-yaml>` for more details.

How can I define that my execution failed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``command`` is considered to be successful if it returns error code 0. This is the default
convention for most programs and scripting languages.

The platform will mark execution as crashed if any of the commands returns any other error code.

The best approach to log what went wrong is to use stderr which is visible on the execution **Logs** tab.

I want to pass commands in ``Rscript myscript.r arg1 arg2`` format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

That's not a question! :)

You define how the parameters are passed in the ``parameters`` section in ``valohai.yaml``.

The default syntax is ``--{name}={value}`` so:

.. code-block:: yaml

   - name: dropout
     pass-as: --dropout={v}

To get the syntax mentioned in the question, add or modify the ``pass-as`` property:

.. code-block:: yaml

   - name: dropout
     pass-as: {v}

See :doc:`valohai.yaml documentation </valohai-yaml>` for more details.

How do I upload output files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Anything written to the ``/valohai/output`` directory will be uploaded and accessible after the execution.

The files will be uploaded to AWS S3, but we're working on providing other storage options.
