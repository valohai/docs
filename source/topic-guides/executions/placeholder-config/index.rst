.. meta::
    :description: You can use placeholder syntax in Valohai commands to inject custom parameters to your executions.

Placeholder-based configuration
===============================

Placeholder-based configuration is an alternative to file-based execution configuration.

After you define :doc:`parameters </reference-guides/valohai-yaml/step-parameters>` in your ``valohai.yaml``,
you can add various placeholders to your commands which get replaced with the actual values.

It is common to use these in the following manner:

.. code-block:: yaml

    - step:
        name: train-model
        image: tensorflow/tensorflow:0.12.1-devel-gpu
        command: python train.py {parameters}
        parameters:
          - name: max_steps
            pass-as: --max_steps={v}
            type: integer
            default: 300

This makes it easy to track used parameters for automated hyperparameter optimization and
following how different parameters affect your model accuracy.

``{parameters}`` placeholder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /_partials/_parameter-parameters-placeholder.rst

``{parameter:<NAME>}`` placeholder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /_partials/_parameter-parameter-placeholder.rst

``{parameter-value:<NAME>}`` placeholder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /_partials/_parameter-parameter-value-placeholder.rst
