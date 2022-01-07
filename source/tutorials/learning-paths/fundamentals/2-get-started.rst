.. meta::
    :description: Valohai Fundamentals learning path - Running your first Valohai execution

Getting started
###############

.. include:: _shared/_2-get-started.rst

.. raw:: html
    
    <div style="position: relative; padding-bottom: 52.94117647058824%; height: 0;"><iframe src="https://www.loom.com/embed/cd8d03fec53a4b3f9f83d2b23e4d70c1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Create a configuration file
---------------------------

Add a new file called ``valohai.yaml`` to define a new Valohai step called ``train``. Whenever we launch this step in Valohai we want to run the ``train.py`` script inside a TensorFlow 2.6.0 Docker image.

.. code-block:: yaml

    - step:
        name: train-model
        command: python train.py
        image: tensorflow/tensorflow:2.6.0

Run in Valohai
--------------

Finally, we can start a new Valohai job directly from your command-line.

.. code:: bash

    vh exec run train-model --adhoc

..

.. include:: _shared/_2-get-started-end.rst