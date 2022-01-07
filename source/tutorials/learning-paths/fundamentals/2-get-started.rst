.. meta::
    :description: Valohai Fundamentals learning path - Running your first Valohai execution

Getting started
###############

.. include:: _shared/_2-get-started.rst

Import Valohai
--------------

Now we'll ``import valohai`` and define a new :ref:`step` in the ``train.py`` file we just created..

* Create a new the step called ``train-model``
* Define a default Docker image for this step. The Docker image should contain the packages we need to run our code, like Tensorflow.

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,5,6,7,8

    import numpy as np
    import tensorflow as tf
    import valohai

    valohai.prepare(
        step='train-model',
        image='tensorflow/tensorflow:2.6.0',
    )

..

Run in Valohai
--------------

Finally, we run the following commands in the command line, on your own computer:

.. code:: bash

    vh yaml step train.py
    vh exec run train-model --adhoc

..

* ``vh yaml step`` uses the command-line tools to generate a :ref:`yaml` and a ``requirements.txt`` that contains ``valohai-utils`` (which is need to run the Python script).

.. include:: _shared/_2-get-started-end.rst