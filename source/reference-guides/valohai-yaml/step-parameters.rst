.. meta::
    :description: The parameters section declares dynamic parameters for your execution, and for hyperparameter optimization.


``step.parameters``
===================

Parameters are injected into the command by replacing any **Valohai parameter placeholders** defined further below.
Good examples of parameters would be "learning rate" number or "network layout" string.

A parameter in ``parameters`` has 2 required and 4 optional properties:

* ``name``: the parameter name, shown on the user interface
* ``type``: the parameter type, valid values are ``float``, ``integer``, ``string`` and ``flag``
* ``pass-as``: **(optional)** how the parameter is passed to the command
* ``description``: **(optional)** more detailed human-readable description of the parameter
* ``default``: **(optional)** the default value of the parameter
* ``optional``: **(optional)** marks that this input is optional and the value can be left undefined

.. note::

    ``optional`` has no effect for the ``flag`` type.
    It either exists or doesn't. If it's always on, you can type it into the command.

If ``pass-as`` is not defined, the parameter is passed as ``--<PARAMETER_NAME>={v}``, you can customize this by specifying ``{v}`` in the ``pass-as`` e.g. ``-t {v}`` where ``{v}`` becomes the actual value.

.. note::

    ``flag`` type defaults to just ``--<PARAMETER_NAME>`` when set to true. When set to false, nothing is passed. 

The note above implies that when you want to pass a flag with the value ``false``, you will need to use the ``pass-as`` property.    

.. code-block:: yaml

    pass-true-as: --<PARAMETER_NAME>=true
    pass-false-as: --<PARAMETER_NAME>=false

..



``{parameters}`` placeholder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /_partials/_parameter-parameters-placeholder.rst

``{parameter:<NAME>}`` placeholder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /_partials/_parameter-parameter-placeholder.rst

``{parameter-value:<NAME>}`` placeholder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /_partials/_parameter-parameter-value-placeholder.rst
