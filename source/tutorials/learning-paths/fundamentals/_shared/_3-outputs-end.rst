
Datums
--------

Datums are unique identifiers that can be used to point to specific output files. You can use them as inputs in your executions in order to reuse the output data. You can view and copy datums from the web UI. 

- **Open your project** on `app.valohai.com <https://app.valohai.com>`_
- **Go to the Data tab under your project**
- Click the three dots at the end of the row for the execution you
- Click **Copy datum:// URL**

.. note:: 

    You'll also have the option to copy your cloud data store's URL (e.g. ``s3://``, ``gs://``, or ``azure://``. You can use either the datum URL or the cloud provider URL for your Valohai executions.


    The advantage of using ``datum://`` is that it allows Valohai keep track of that exact file and version. This allows you to later on trace back files and understand where different files are used, or for example to keep track of which pipeline was ran to generate a trained model file.

Setting datum aliases
--------------------------------

In some cases you might want to set an alias that for example always points to the latest execution and its datum. 

- **Open your project** on `app.valohai.com <https://app.valohai.com>`_
- **Go to the Project Data view** (Data tab under your project)
- **Choose Aliases tab**
- Click **Create new datum alias**
- Write **Name** for the alias and choose **datum** from the list.
- Click **Save**
- You can edit saved aliases by choosing **Edit** from the **Actions dropdown menu**. The change history of aliases is tracked.

.. seealso::

  * :ref:`outputs`
  * :ref:`live-outputs`
  * :ref:`cloud-storage`
  * :ref:`howto-datum-alias`
  * `step.inputs reference </reference-guides/valohai-yaml/step-inputs/>`_

..
