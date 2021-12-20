:orphan:

.. meta::
    :description: Overview of how you'll read and write data in Valohai


.. _migrate-parameters:

Define Valohai parameters
#################################################

.. seealso::

    This how-to is a part of our :ref:`new-user-guide` series.

.. include:: /_partials/_recap-parameters.rst

.. tab:: valohai-utils (Python)

    .. code-block:: python

        import valohai

        # Define parameters in a dictionary
        default_parameters = {
            'iterations': 10,
        }
        
        # Create a step 'Train Model' in valohai.yaml with a set of parameters
        valohai.prepare(step="train", image="tensorflow/tensorflow:2.6.1-gpu", default_inputs=default_inputs, default_parameters=default_parameters)
        
        # Access the parameters in your code
        for i in range(valohai.parameters('iterations').value):
            print("Iteration %s" % i)
    

    ..

    Generate or update your existing YAML file by running

    .. code-block:: bash

        vh yaml step myfile.py

    ..

    The generated ``valohai.yaml`` configuration file looks like:

.. tab:: Python

    .. code-block:: python

        import argparse

        def parse_args():
            parser = argparse.ArgumentParser()
            parser.add_argument('--iterations', type=int, default=10)
            return parser.parse_args()

        args = parse_args()
        
        print(args.iterations)

    ..

    Create a ``valohai.yaml`` configuration file and define your step in it:


.. tab:: R

    .. code-block:: r

        library(optparse)

        option_list <- list(
            make_option("--iterations", default = 10),
        )
        
        parser <- OptionParser(option_list = option_list)
        args <- parse_args(parser)

        iterations <- args$iterations
        write(iterations, stdout())

    ..

    Create a ``valohai.yaml`` configuration file and define your step in it:

.. code-block:: yaml

   - step:
       name: Train model
       image: tensorflow/tensorflow:1.13.1
       command: python myfile.py {parameters}
       parameters:
         - name: iterations
           type: integer
           default: 100

.. seealso::

    * `More about parameters </topic-guides/core-concepts/parameters/>`_

.. hint:: 

    `Read more about valohai-utils </topic-guides/valohai-utils/>`_