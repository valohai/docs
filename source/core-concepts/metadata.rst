.. meta::
    :description: What is Valohai execution metadata? Keep track of your experiments.

Metadata
========

Execution **metadata** is output by writing lines of JSON to the standard output stream.

For instance, in Python,

.. code-block:: python

   import json

   print(json.dumps({"step": 190, "accuracy": 0.9247000813484192}))
   print(json.dumps({"step": 200, "accuracy": 0.9262000918388367}))
   print(json.dumps(({"model_layout": "ReLU8x-3xELUx32-softmax8"}))

.. code-block:: json

   {"step": 190, "accuracy": 0.9247000813484192}
   {"step": 200, "accuracy": 0.9262000918388367}
   {"model_layout": "ReLU8x-3xELUx32-softmax8"}

Each metadata point also has an implicit value ``_time`` which tells the metadata line was output.
The ``_time`` value is in UTC, formatted as an ISO-8601 datetime (e.g. ``2017-04-04T15:03:39.321000``).

You can generate real-time charts based on metadata which helps with
monitoring long runs so you can stop them if training doesn't converge well.

You can sort executions by metadata values in the web interface which is useful for e.g. finding training
executions with the highest prediction accuracy.

The latest or last value of each key such as ``accuracy`` can be used for the sorting hyperparameter optimization results.
