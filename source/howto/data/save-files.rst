
.. meta::
    :description: Save files from Valohai

.. _howto-data-save-files:

Save files from trainings
################################################

.. admonition:: A short recap on outputs
    :class: tip

    * You can output any type of files from Valohai. For example trained models, csv-files, images, or something else.
    * Valohai outputs will be save to projects default data store (AWS S3, Azure Storage, GCP Cloud Storage, OpenStack Swift).
    * By default all outputs will be saved to your data store at the end of an execution. You can use :ref:`live-outputs` to save files mid-execution.
    * Each output will receive a unique ``datum://`` link that you can use to download the file to another execution. If you're using your own data store, you'll also receive a link specific to that data store.

..

Write your files to the ``/valohai/outputs/`` folder to save and upload them to your cloud storage. The saved files will appear under the Outputs tab of your execution and in the projects Data tab.

You can then use the copied ``datum://`` link as an input in another execution. For example use a link to a trained model file in a new Batch Inference execution.

.. video:: /_static/videos/output-files.mp4
    :autoplay:
    :width: 700

.. admonition:: What's the difference between datum:// and my cloud storage link?
    :class: tip

    * Once a file is uploaded to Valohai, or saved through an execution, you'll receive a ``datum://`` link for the execution. 
    * You'll also get a link to your own data store, if you've configured a new default data store in your project.

    We suggest using the ``datum://`` link when you're in the same project. This way Valohai will keep track of how the file is being used and knows where the data originated from.

.. seealso::

    * :ref:`live-outputs`
    * :ref:`howto-data-tag-files`
