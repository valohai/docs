Configure settings
~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/settings.gif
   :alt: Valohai execution settings

Press the Valohai button in the toolbar and go to settings window.

Select the following:

- **Project**: Valohai project where the executions will be version controlled
- **Environment**: Environment type for the cloud executions (E.g. AWS p2.xlarge)
- **Docker Image**: Docker image that provides the required libraries (E.g. TensorFlow)

These are the same settings you would choose when using Valohai website, CLI or `valohai.yaml`.

Once you are happy with your selections. Press save.

Create an execution
~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/execution.gif
   :alt: Running Valohai execution

Press the Valohai button in the toolbar and select *Create execution*.

The gizmo for the new execution will appear to the right.

.. container:: alert alert-warning

   **Open a Notebook from a previous execution**

   Each of the colored gizmos on the right side of the page signify a single Valohai execution. You can click on any of the completed executions and select ``Notebook`` to launch the Notebook version that was used to run the execution.

..

Watch the results
~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/download.gif
   :alt: Get results back from Valohai

You can click the `#1 > Notebook` button to download the finished notebook back to your local machine.

Parameterize the notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/parameterize.gif
   :alt: Adding hyperparameter

Parameterizing a notebook happens through cell tags. Tags are a standard Jupyter feature.

Here we mark the first cell with a ``parameters`` tag, which means all variables are considered to be
Valohai parameters, just like you would define in the `valohai.yaml`.

Download the inputs
~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/inputs.png
   :alt: Adding parameterized input

Here we marked the first cell with ``inputs`` tag and ran it in Valohai.

All the variables in this cell will be considered as Valohai input URIs for the execution, just like in the `valohai.yaml`.

Reusing the parameterized notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: ../shared/parameter2.gif
   :alt: Adding hyperparameter

Now you can run notebook based experiments without a notebook!

Because the ``learning_rate`` is parameterized, you can change it via Valohai web interface and run
additional experiments without even opening the notebook.

