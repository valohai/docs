.. meta::
    :description: Valohai Pipelines learning path - Creating your first pipeline in Valohai

Advanced pipeline features
############################

.. include:: _intro-pl.rst

In this section you will
 * Learn how to create pipelines with multiple nodes
 * Learn how to use pipeline conditions
 * Learn how to set pipeline triggers


Pipeline with multiple nodes
----------------------------

For an example with multiple nodes, please see our :ref:`example-projects-quick-start-tensorflow`. 

* It is worth noting that when evaluating multiple trained models inside a pipeline, **the comparison for choosing the best model is not done automatically**. 
* The user needs to define the comparison programatically in a separate node and then output the results to the possible next node (see the ``yaml`` file and ``compare.py`` in the example project).


Pipeline conditions
-------------------

In some cases you might want to terminate the pipeline if for example a metadata value exceeds some set limit. This can be done by using a pipeline property called ``actions``.
The structure for ``actions`` is: ``when`` something happens, check ``if`` the condition is true, and if yes, ``then`` stop the pipeline.

The possible options for ``when`` are:

* ``node-starting``
* ``node-complete``
* ``node-error``

The ``if`` condition can be based either on metadata or a parameter. 

Currently, the availables option for ``then`` are:

* ``stop-pipeline`` to stop the complete pipeline.
* ``require-approval`` to pause the pipeline until a user goes to manually approve the previous results of the pipeline.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 7,8,9,10,14,15,16

    - pipeline:
        name: Action pipeline
        nodes:
          - name: train-model
            type: execution
            step: Train model
            actions:
              - when: node-complete
                if: metadata.foo >= 0.8
                then: stop-pipeline
          - name: test-model
            type: execution
            step: Test model
            actions:
              - when: node-starting
                then: require-approval
        edges:
          - [train-model.output.model*, test-model.input.model]

..


Pipeline triggers
-------------------

Triggers page goes here