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
* **Bayesian Optimization** - Configure a max count of executions, an execution batch size, a target metric and a target value for that metric and iteratively optimise the target metric towards the target value.

For each parameter you can set the value as a defined single value or use:

* **Multiple values** - a comma seperated list of all the values to try for a specific hyperparameter.
* **Linear** - a search with start and end values, and the step size.
* **Logspace** - a search with values inside a specific range in logarithmic space
* **Random** - search randomly within a specified range and distribution.

.. container:: alert alert-warning

    **Bayesian optimization**

    Valohai uses the open source Hyperopt-library's Tree Parzen Estimator algorithm to use the hyperparameters and outputs of the previous executions to suggest future execution hyperparameters.
    
    Under the hood, Bayesian optimization (of which TPE is an implementation) works in the following steps:

        * Create startup executions using random search
        * Based on these executions, create a simplified function to model the relationship between the hyperparameters and the target metric value (for example "loss")
        * Based on this simplification of their relationship, find the optimal values for the hyper parameter to make the target metric as close to the target value as possible
        * Run the next batch of executions and repeat the process from step 2.
    
    Using interactive hyperparameter optimisation can make hyperparameter tuning faster and more efficient than for example using a random search or an exhaustive grid search. 
..

.. seealso::

    * `Read more about parameters </docs/core-concepts/parameters/>`_
    * `Define parameters in valohai.yaml </docs/valohai-yaml/step-parameters/>`_

..


Create a sequence of operations with pipelines
-----------------------------------------------

.. include:: ../../../_shared/_pipelines.rst


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
      auth_token = 'bSoBrjudHterhjS1woonhSfeCDDFaXV330e1oXnX'
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
      auth_token = 'bSoBrjudHterhjS1woonhSfeCDDFaXV330e1oXnX'
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
      auth_token = 'bSoBrjudHterhjS1woonhSfeCDDFaXV330e1oXnX'
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

    You can define the maximum API token lifetime for all users in your organisation under the organisation settings.
..

.. seealso:: 

  * `Valohai API <https://app.valohai.com/api/v0/>`_
  * `Valohai API Docs <https://app.valohai.com/api/docs/>`_ 

..

