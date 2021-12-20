.. admonition:: A short introduction outputs
    :class: seealso

    * Defining parameters allows you to easily rerun, sort, and keep track of executions based on the parameter values used to run them.
    * You can easily create (or copy) an execution and change the parameters in the UI, without changing your code.
    * Defining parameters allows you to start creating Tasks where you run multiple parallel executions with different parameter combinations.
    * Each step has it's own parameter configuration in ``valohai.yaml``.
    * A parameter can be type of a ``string``, ``integer``, ``float``, and ``flag`` (=boolean).
    * Parameters are passed as command-line arguments to your code.
      
      * Edit parameters are passed to your code using `pass-as </reference-guides/valohai-yaml/step-parameters/>`_.
      * You can also parse parameter values from YAML and JSON files inside your execution. See `file-based configuration </topic-guides/executions/file-config/>`_.