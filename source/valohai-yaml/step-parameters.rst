``step.parameters``
~~~~~~~~~~~~~~

Parameters are injected into the command by replacing the ``{parameters}`` placeholder.
Good examples of parameters would be "learning rate" number or "network layout" string.

A parameter in ``parameters`` has six potential properties:

* ``name``: the parameter name, shown on the user interface and used as the default name when passed to commands
* ``type``: the parameter type, valid values are **float**, **integer**, **string** and **flag**
* ``pass-as``: (optional) how the parameter is passed to the command e.g. ``-t {v}`` where ``{v}`` becomes the actual value.
  If not defined, the parameter is passed as  ``--{name}={value}``. Note: Type 'flag' defaults to '--{name}'.
* ``description``: (optional) more detailed human-readable description of the parameter
* ``default``: (optional) the default value of the parameter
* ``optional``: (optional) marks that this input is optional and the value can be left undefined. Note: has no effect for the type 'flag'.

.. tip::

    When a value is undefined, the parameter will appear with it's default value, except for the type ``flag``. Flags will only ever appear, if they are defined with value set to true.
