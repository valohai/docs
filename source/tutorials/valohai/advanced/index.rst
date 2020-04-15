.. meta::
    :description: Start using organization features on Valohai to enable collaboration and ensure compliance, tracability, and reproducability.

Advanced topics
==========================



☁️ Use Tasks for hyperparameter optimization
-----------------------------------------------

Valohai tasks are collections of executions that are aimed to solve one experiment or assignment. The most common task type is hyperparameter optimization which you can trigger using Valohai’s web interface.

It can be daunting to try different hyperparameters one-by-one. Valohai offers a mechanism to do hyperparameter searches using:

* **Grid search** - Search all permutations of multiple values for multiple hyperparameters.
    * For example, if we wanted to run with 6 different values for learning_rate and 6 different values for dropout we would get in total 6*6 = 36 executions
* **Random search** - Configure a max count of executions and find the corresponding amount of random parameters in a defined search space
* **Bayesian Optimization** - Using interactive hyperparameter optimisation can make hyperparameter tuning faster and more efficient than for example using a random search or an exhaustive grid search. Configure a max count of executions, an execution batch size, a target metric and a target value for that metric and iteratively optimise the target metric towards the target value.

For each parameter you can set the value as a defined single value or use:

* **Multiple values** - a comma seperated list of all the values to try for a specific hyperparameter.
* **Linear** - a search with start and end values, and the step size.
* **Logspace** - a search with values inside a specific range in logarithmic space
* **Random** - search randomly within a specified range and distribution.

.. seealso::

    * `Read more about parameters </core-concepts/parameters/>`_
    * `Define parameters in valohai.yaml </valohai-yaml/step-parameters/>`_

..

Tutorial: Add parameters
-------------------------

Let's continue our sample project from the `Valohai Quickstart </tutorials/valohai/>`_. If you haven't completed the tutorial, you can get the sample code from `GitHub <https://github.com/DrazenDodik/valohaiquickstart>`_.

As you start running your experiments and trying different combinations, you'll soon wish there is a way to pass values like the ``epochnum`` or ``learningrate`` to your code without changing the code. Allowing you quickly to experiment with different parameter values. Have no fear, we can do that!

* Edit your ``valohai.yaml`` to include additional parameters. Define parameters ``epochnum`` and ``learningrate``
* Update your command to ensure that the parameters get passed in
    .. code:: yaml

        - step:
            name: Train MNIST model
            image: tensorflow/tensorflow:2.0.1-gpu-py3
            command: python train.py {parameters}
            inputs:
              - name: my-mnist-dataset
                default: {datum://id}
            parameters:
              - name: epochnum
                type: integer
                default: 5
              - name: learningrate
                type: float
                default: 0.001
        - endpoint:
                name: digit-predict
                description: predict digits from image inputs
                image: tensorflow/tensorflow:2.0.1-py3
                wsgi: predict:mypredictor
                files:
                    - name: model
                      description: Model output file from TensorFlow
                      path: model.h5

    ..

Next update ``train.py`` and use these parameters in our code. We'll need to first parse the arguments passed to the code and then use these two new parameters. We'll use `argparse from the Python Standard Library <https://docs.python.org/3/library/argparse.html>`_ to parse the arguments.

* Add ``import argparse`` to your train.py
* Define a new function that will parse our arguments
    .. code:: python

        def getArgs():
            # Initialize the ArgumentParser
            parser = argparse.ArgumentParser()
            # Define two arguments that it should parse
            parser.add_argument('--epochnum', type=int, default=5)
            parser.add_argument('--learningrate', type=float, default=0.001)

            # Now run the parser that will return us the arguments and their values and store in our variable args
            args = parser.parse_args()

            # Return the parsed arguments
            return args
    ..
* Now call our new function in the beginning of our file, for example after defining the functions.
    .. code:: python

        # Call our newly created getArgs() function and store the parsed arguments in a variable args. We can later access the values through it, for example args.learningrate
        args = getArgs()
    ..
* Now that we've parsed our values, we can start using them. Lets first update the simpler one: epochnum by updating our model.fit to use the parameter value.
    .. code:: python

        model.fit(x_train, y_train, epochs=args.epochnum, callbacks=[metadataCallback])
    ..
* We'll also need to use the learning_rate parameter, which is passed to the Keras optimizer. According to the `Adam optimizer documentation <https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam>`_ we can pass the learning rate in the initialization of the optimizer.
    .. code:: python

        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=args.learningrate),
                loss=loss_fn,
                metrics=['accuracy'])
    ..
* Create a new execution and pass it parameter values ``vh exec run --adhoc train --learningrate=0.1 --epochnum=10``

.. container:: alert alert-warning

    **Connect your project to a repository to run Tasks**

    You might get an error when trying to create a Tasks: "No commits are available. Please set up and fetch the repository first."
    Valohai requires the project to be connected to a repository to be able to create Tasks and for us it's not available as we haven't connected our project to a repository but ran executions as ``--adhoc``.

    However, there is a way around this for the sake of testing this feature. Go into your latest completed Execution that used parameters. On the Details-tab you click the "Task"-button to create a Task based on this ``--adhoc`` commit. Now you can try the different optimization techniques and start multiple tasks.

..

Create a sequence of operations with pipelines
-----------------------------------------------

**Pipeline** is a version controlled collection of executions some of which rely on the results of the previous
executions thus creating a directed graph. These pipeline graphs consist of nodes and edges and we'll discuss
these further down.

For example, consider the following sequence of data science operations:

1. **preprocess** dataset on a memory-optimized machine
2. **train** multiple machine learning models on GPU machines using the preprocessed data (1)
3. **evaluate** all of the trained models (2) to find the best one

We could say that you have 3 separate operations or :doc:`steps </core-concepts/steps>`:
**preprocess**, **train**, **evaluate**.

This pipeline would have 3 or more **nodes**; at least one for each step mentioned above.
Training could have additional nodes if you are training in parallel but lets keep it simple:

.. thumbnail:: /core-concepts/pipelines.png
   :alt: You configure data stores per project-basis on Valohai.

.. seealso::

    * `Read more about pipelines </core-concepts/pipelines/>`_
    * `Define pipelines in valohai.yaml </valohai-yaml/pipeline/>`_

..

Tutorial: Create a sequence of operations with pipelines
-----------------------------------------------------------

Let's continue our sample project from the `Valohai Quickstart </tutorials/valohai/>`_. If you haven't completed the tutorial, you can get the sample code from `GitHub <https://github.com/DrazenDodik/valohaiquickstart>`_ and continue from there by adding pipelines functionality.

In our example we're not doing any heavy preprocessing work but we'll still use the MNIST example as the concept remains the same even for a larger project.

1. `Split your code to multiple steps <#id3>`_
2. `Define a pipeline <#id4>`_ 

.. container:: alert alert-warning

    You'll need to have your code in a code repository and connect the repository to a Valohai project to proceed. Pipelines do not work through ``--adhoc`` executions.
   
    * `Connect to GitHub </tutorials/code-repository/private-github-repository>`_
    * `Connect to GitLab </tutorials/code-repository/private-gitlab-repository>`_
    * `Connect to BitBucket </tutorials/code-repository/private-bitbucket-repository>`_
..

Split your code to multiple steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* In our ``train.py`` we have a simple transformation for our data ``x_train, x_test = x_train / 255.0, x_test / 255.0``. Remove it from ``train.py``. We'll want to move this to another step in Valohai, so we don't need to run it every time we want to train a model..
* Create a new file called ``preprocess.py`` and populate it the below:
    .. code:: python

        import os
        import numpy

        inputs_path = os.getenv('VH_INPUTS_DIR', './inputs')
        outputs_path = os.getenv('VH_OUTPUTS_DIR', './outputs')

        # Get path to raw MNIST dataset
        input_path = os.path.join(inputs_path, 'my-raw-mnist-dataset/mnist.npz')

        with np.load(input_path, allow_pickle=True) as file:
            x_train, y_train = file['x_train'], file['y_train']
            x_test, y_test = file['x_test'], file['y_test']

        # Preprocess dataset
        x_train, x_test = x_train / 255.0, x_test / 255.0

        # Output the preprocessed file
        processed_file_path = os.path.join(outputs_path, 'preprocessed_mnist.npz')

        numpy.savez(processed_file_path, x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)

    ..
* Now edit your ``valohai.yaml`` to edit the input name of the ``Train MNIST model`` step and include a new step for preprocessing.
* We'll run two commands there, one to install numpy on the ``python:3.6`` image we're using for the step and another to run ``preprocess.py``
    .. code:: yaml

        - step:
            name: Preprocess data
            image: python:3.6
            command:
            - pip install numpy==1.18.1
            - python preprocess.py
            inputs:
            - name: my-raw-mnist-dataset
                #default: {datum://id} 
                default: https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
        - step:
            name: Train MNIST model
            image: tensorflow/tensorflow:2.0.1-gpu-py3
            command: python train.py
            inputs:
                - name: my-processed-mnist-dataset
                  #default: {datum://id} 
                  default: https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz

        - step:
            name: Preprocess data
            image: python:3.6
            command:
            - pip install numpy==1.18.1
            - python preprocess.py
            inputs:
            - name: my-raw-mnist-dataset
                #default: {datum://unprocessed-data}
                default: https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz

    ..
* 🔥You can now test your step by running ``vh exec run --adhoc preprocess``
* You'll see a new output appear from your execution with the preprocessed data. Use that as the input for your train step.
    * In your ``valohai.yaml`` replace the default address of the ``my-processed-mnist-dataset`` input to point to the newly generated dataset (datum URI).

Define a pipeline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next we'll need to create the pipeline definition. We'll need to define the steps our pipeline has and how inputs/outputs flow through them.

* **Nodes** - In our case these will represent different steps (preprocess and train)
* **Edges** - How do we connect these steps? For example the output of preprocessing should be used as the input of our train step.

* In your ``valohai.yaml`` create a new pipeline as:
    .. code:: yaml

        - pipeline:
            name: Training pipeline
            nodes:
            - name: preprocess
                type: execution
                step: Preprocess data
            - name: train
                type: execution
                step: Train MNIST model
            edges:
            - [preprocess.output.*.npz, train.input.my-processed-mnist-dataset]

    ..
* The ``node.step`` is the name of the ``step`` in ``valohai.yaml`` and the ``edges`` are defining the output/input data of those steps (e.g. step.input.input-name)
* Now push a new commit to your code repository and fetch a new commit to Valohai.
* 🔥 You can now create a new pipeline from your project. This will automatically launch the right executions and pass the right inputs to our train step.
    * As per the ``edges`` definition of your pipeline, it will replace the default input of ``my-processed-mnist-dataset`` with the .npz file that was outputted from the preprocessing step.
    * You'll notice that the simple graph appears with familiar colors (blue for starting, green for completed)


Do more with Valohai APIs
--------------------------

The Valohai API exposes most of the functionality of the Valohai platform and used for complex automation and pipelining.

.. container:: alert alert-warning

    **Requirements**

    * Python 3 (3.4+ recommended), pip and ``pip install requests``

      * You can use any programming language to make the HTTP requests to Valohai APIs but in this tutorial we'll use Python.

..

Using the Valohai APIs is rather straightforward, you'll need to create an API token to authenticate your requests and then write your code to send & receive requests.

* Go to your profile setting and `create an authentication token <https://app.valohai.com/auth/tokens/>`_
    * You could save this token in a configuration file or database for easy and secure storage.
* Create a new folder on your computer and inside it create a new file ``fetchVHProjects.py``
    .. code:: Python

      import requests
      import json

      # Authenticate yourself with the token
      auth_token = '<your-auth-token>'
      headers = {'Authorization': 'Token %s' % auth_token}

      # Send a request (with the authentication headers) to fetch Valohai projects
      resp = requests.get('https://app.valohai.com/api/v0/projects/', headers=headers)
      resp.raise_for_status()

      # Print the response you've received back
      print('# API Response:\n')
      print(json.dumps(resp.json(), indent=4))

  ..
* 🔥 Save the code and run ``python3 fetchVHProject.py`` to get your results (ID, name, execution count, owner, queued executions etc.)

You'll notice that the response contains information about all your projects. It's as easy as this! Now you can do what ever you want with the results.

**You can read more about at:** `Valohai API Docs <https://app.valohai.com/api/docs/>`_

Example: Fetch all (failed) executions of a project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* You'll need the ID of a single project to fetch its executions, you can get it from the previous results (or query for a specific name)
* Create a new folder on your computer and inside it create a new file ``fetchExecutions.py``
    .. code:: Python

      import requests
      import json

      # Authenticate yourself with the token
      auth_token = '<your-auth-token>'
      headers = {'Authorization': 'Token %s' % auth_token}

      # Send a request (with the authentication headers) to fetch all executions in a project
      # You can get the project ID for example 
      resp = requests.get('https://app.valohai.com/api/v0/executions/?project={project_id}', headers=headers)

      # To fetch all failed executions you could run
      # https://app.valohai.com/api/v0/executions/?project={project_id}&status=error

      resp.raise_for_status()

      # Print the response you've received back
      print('# API Response:\n')
      print(json.dumps(resp.json(), indent=4))

  ..
* Save and run ``python3 fetchExecutions.py`` and you'll see a list of executions with their details.

Example: Fetch execution metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* You'll need the ID of a single execution to fetch its metadata. You can get an ID from the results of our previous sample, or by going to the browser and navigate inside an execution. You'll see the ID in the url.
* Create a new folder on your computer and inside it create a new file ``fetchMetadata.py``
    .. code:: Python

      import requests
      import json

      # Authenticate yourself with the token
      auth_token = '<your-auth-token>'
      headers = {'Authorization': 'Token %s' % auth_token}

      # Send a request (with the authentication headers) to fetch all executions in a project
      # You can get the project ID for example 
      resp = requests.get('https://app.valohai.com/api/v0/executions/{execution_id}/metadata/', headers=headers)

      resp.raise_for_status()

      # Print the response you've received back
      print('# API Response:\n')
      print(json.dumps(resp.json(), indent=4))
* 🔥 Save and run ``python3 fetchMetadata.py`` and you'll see the metadata stream of a single execution.

.. container:: alert alert-warning

    **Note**

    You can define the maximum API token lifetime for all users in your organization under the organization settings.
..

.. seealso:: 

  * `Valohai API <https://app.valohai.com/api/v0/>`_
  * `Valohai API Docs <https://app.valohai.com/api/docs/>`_ 

..

