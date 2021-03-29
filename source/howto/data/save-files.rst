
.. meta::
    :description: Save files from executions

.. _howto-data-save-files:

Save files from executions
#############################


This guide shows you how to save files from an execution.


* Login to `app.valohai.com <https://app.valohai.com>`_ 
* Open your project
* Click on your Project's **Data** tab
* Click on the **Upload** tab
* Choose the right data store from the dropdown on the right side
* Select files from your local machine
* Click **Upload** 

Navigate back to the **Browse** tab when upload has completed. You should see your uploaded file on the top of the list.

Click on ``...`` at the end of the row to get the link to the data file.

.. image:: _images/data_copyurl.png
  :alt: Get a link to data file

.. tip::

  If you uploaded your file to a Valohai owned data store you'll see only a ``datum://`` link. Datum links are unique links that point to specific files in the Valohai platform.

  If you upload files to your own data store you'll also see a link that your cloud provider understands (e.g. ``s3://``, ``azure://``, or ``gs://``).

  You can use either link in your Valohai executions.

.. seealso::

  * :ref:`cloud-storage`
  * `Uploading files from executions </topic-guides/executions/outputs/>`_

