If you wish to ignore ``pass-as`` definition, you can use ``{parameter-value:<NAME>}`` to pass only the parameter value.
This is essentially the same as defining ``pass-as: "{v}"``.

For example:

.. code-block:: yaml

    - step:
        name: preprocess
        image: python:3.6
        command:
          - python preprocess.py {parameter-value:train-split} {parameter-value:style}
        parameters:
          - name: train-split
            type: integer
            default: 80
          - name: style
            pass-as: -s={v}
            type: string
            default: nested

The above would generate the following command by default:

.. code-block:: bash

    python preprocess.py 80 nested

.. note::

    There are no limits how many ``{parameters}``, ``{parameter:<NAME>}`` and ``{parameter-value:<NAME>}``
    placeholders you can have in a set of commands so use them to your heart's content!
