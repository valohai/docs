
Finally run a new Valohai execution.

.. code:: bash

    vh exec run train-model --adhoc

..

Rerun an execution with different input data
-------------------------------------------------------

* **Open your project** on `app.valohai.com <https://app.valohai.com>`_
* **Open the latest execution**
* Click **Copy**
* Scroll down to the **Inputs** section and remove the current input.
* You can now either pass in a new URI or select an input from the Data list (for example, if you've uploaded a file)
* Click **Create execution**


.. video:: /_static/videos/execution_inputs.mp4
    :autoplay:
    :width: 600

.. tip::

    You can also run a new execution with different input value from the command line:

    ``vh exec run train-model --adhoc --mnist=https://mmyurl.com/differentfile.npz``


.. seealso::

    * :ref:`howto-data-upload-files`
    * `step.inputs reference </reference-guides/valohai-yaml/step-inputs/>`_

..
