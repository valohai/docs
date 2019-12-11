.. meta::
    :description: Step sections define separate types of executions.

``step``
~~~~~~~~

Every ``step`` defines a separate type of execution such as training or evaluation.

You run a step by creating an execution that implements that step.

Here is an overview of the valid ``step`` properties:

* ``name``: name of the step such as "feature-extraction" or "model-training"
* ``image``: Docker image that will be used as the runtime environment
* ``command``: one or more commands that are ran during execution
* ``parameters``: **(optional)** valid parameters that can be passed to the commands
* ``inputs``: **(optional)** files available during execution
* ``environment``: **(optional)** environment slug that specifies hardware and geolocation
* ``environment-variables``: **(optional)** define runtime environment variables
