:orphan:

.. meta::
    :description: Overview of how you'll read and write data in Valohai


.. _migrate-parameters:

Define Valohai parameters
#################################################

.. seealso::

    This how-to is a part of our :ref:`new-user-guide` series.

.. raw:: html

    <div style="position: relative; padding-bottom: 50.2092050209205%; height: 0;"><iframe src="https://www.loom.com/embed/b2893913fdbe4d3a90e341a3f3c7d208" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


.. include:: /_partials/_recap-parameters.rst

.. tab:: valohai-utils (Python)

    .. code-block:: python
        :linenos:
        :emphasize-lines: 9,10,11,12,19,21,22,23

        import valohai

        # Define inputs available for this step and their default location
        # The default location can be overriden when you create a new execution (UI, API or CLI)
        default_inputs = {
            'myinput': 's3://bucket/mydata.csv'
        }

        # Define parameters in a dictionary
        default_parameters = {
            'iterations': 10,
        }

        # Open the CSV file from Valohai inputs
        with open(valohai.inputs("myinput").path()) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
        
        # Create a step 'train' in valohai.yaml with a set of parameters
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