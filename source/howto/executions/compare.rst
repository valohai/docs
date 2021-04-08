
.. meta::
    :description: Easily compare execution metadata and performance in Valohai

.. _executions-compare:

Compare executions
################################

Valohai allows you to easily compare key metrics from executions.

.. admonition:: Prerequirements
  :class: attention

  * A Valohai project that is connected to a Git-repository.
  * Multiple completed executions which print out metadata. Follow our :ref:`quickstart-metadata` tutorial to learn how to use metadata.

..

* **Open a project**
* **Select multiple executions using the checkbox** in the Executions table
* **Click Compare** to open the metadata view with selected executions
* **Click Table** to output a table with all the values from each execution
* **Click Latest** to show only the latest value in the table
* **Click on the best performing line** to open the execution that generated these results

.. video:: /_static/videos/executions_compare.mp4
    :autoplay:
    :nocontrols:
    :width: 500


.. seealso::

    * Download metadata for offline analysis from a `single execution <https://app.valohai.com/api/docs/#operation/ExecutionMetadata>`_ or `multiple executions <https://app.valohai.com/api/docs/#operation/ExecutionMultiEvents>`_ using the Valohai API.
