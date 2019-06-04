``step``
~~~~~~~~

Every ``step`` defines a separate type of execution such as training or evaluation.

Here is an overview of the valid ``step`` properties:

* ``name``: name of the step such as "feature-extraction" or "model-training"
* ``image``: default Docker image that will be used as the runtime environment
* ``command``: one or more commands that are ran during execution
* ``parameters``: **(optional)** valid parameters that can be passed to the commands
* ``inputs``: **(optional)** files available during execution
* ``environment``: **(optional)** default environment slug that specifies hardware and location e.g. "aws-eu-west-1-g3s-xlarge"
