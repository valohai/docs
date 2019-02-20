``step``
~~~~~~~~

Every ``step`` defines a separate type of execution such as training or evaluation.

Here is an overview of the five valid ``step`` properties:

* ``name``: the name of the step such as "feature-extraction" or "model-training"
* ``image``: the Docker image that will be used as the base of the execution
* ``command``: one or more commands that are ran during execution
* ``inputs``: **(optional)** files available during execution
* ``parameters``: **(optional)** valid parameters that can be passed to the commands
