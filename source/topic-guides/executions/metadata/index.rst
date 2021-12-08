.. meta::
    :description: What is Valohai execution metadata? Create visualizations and keep track of your experiments.

Creating visualizations
=======================

If you wish to create visualizations, you can either:

1. save them as images to ``/valohai/outputs`` to be uploaded
2. use our metadata system to render interactive graphs on the web interface

Visualizations from Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Each metadata point also has an implicit value ``_time`` which tells when the metadata line was output.
The ``_time`` value is in UTC, formatted as an ISO-8601 datetime (e.g. ``2017-04-04T15:03:39.321000``).

You can generate real-time charts based on metadata which helps with
monitoring long runs so you can stop them if training doesn't converge well. Optionally, you can use any metadata value as the Horizontal axis value by selecting it in the corresponding dropdown menu. 

You can add and remove graphs for different metadata by clicking on "Add/remove". Once added, you can smooth the graph and choose the position of the vertical axis for each metadata. 

.. image:: /_images/compare_executions.png
   :alt: Metadata chart comparison

You can sort executions by metadata values in the web interface under the Executions tab which is useful for e.g. finding training
executions with the highest prediction accuracy.

The latest or last value of each key such as ``accuracy`` can be used for the sorting hyperparameter optimization results.

Visualizing a confusion matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can easily generate confusion matrices in Valohai.

The supported formats are:

* An array of ``[['x', 'y', v], ['x', 'y', v], ...]`` triples (i.e. x label, y label, value)
* A 2-dimensional array of the shape ``[[v, v, v], [v, v, v], ...]``
* A 2-dimensional array with a header for labels ``[['a', 'b', 'c'], [v, v, v], [v, v, v], ...]``


For example:

.. code-block:: python

   from sklearn.metrics import confusion_matrix
   import numpy as np
   import json

   y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
   y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]

   matrix = confusion_matrix(y_actu, y_pred)

   # Convert to list
   result = matrix.tolist()

   print(json.dumps({"data": result}))
   # {"data": [[3, 0, 0], [0, 1, 2], [2, 1, 3]]}

Would result in:

.. image:: /_images/confusion_matrix.png
   :alt: Confusion matrix


What else can I do with metadata?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Beyond creating the visuals, based on metadata values you can for example:
 
* Easily sort execution tables.
* Easily compare executions.
* Set early-stopping rules for executions and Tasks.
* Set pipeline condititions.
