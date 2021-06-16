.. meta::
    :description: This how to guide shows you how to create aliases for your data files and use them in your executions.

.. _howto-datum-alias:

Data aliases
################################################

You can create a data alias in your project and use the alias as the input for your executions.

There are many different use cases for data aliases. For example:

* Create an alias ``model-prod`` and point it to the version of a model that should be used for batch inference in production
* Create an alias for ``train-images`` that points to the latest preprocessed dataset of a specific use case. The rest of the team can then point their inputs to this alias, instead of always searching for the latest version of the preprocessed data.

Valohai keeps track of the change history of each alias, so you can understand when did the latest changes happen.

Datum aliases are resolved during execution/task creation, which means copying executions will not change the data if the alias had been changed meanwhile.

Create and update an alias
-----------------------------------

You can create or update an existing alias using the web UI, programatically when you create a new output, or using the Valohai APIs.

In the Web UI
^^^^^^^^^^^^^^^

* Open your project on `app.valohai.com <https://app.valohai.com>`_
* Open the **Data** tab
* Open the **Aliases** tab
* Select **Create new datum alias**
* Give the alias a name and select which file should the alias point to

On the same page you can also modify existing aliases and view the change history of that datum.

.. video:: /_static/videos/create-datum-alias.mp4
    :autoplay:
    :width: 700

Automatically when a file is created
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also automatically create or update an existing alias when you save a file in your executions.

Read more about the ``.metadata.json``-file: `Store arbitrary metadata with your file <howto/data/tag-files/#store-arbitrary-metadata-with-your-files>`_


Use an alias as an input
------------------------------

Datum aliases are resolved during execution/task creation, which means copying executions will not change the data if the alias had been changed meanwhile.

In the Web UI
^^^^^^^^^^^^^^^

You can select an alias as the input for your execution by searching for the alias name in the inputs data browser.

.. video:: /_static/videos/use-datum-alias.mp4
    :autoplay:
    :width: 700


In ``valohai.yaml``
^^^^^^^^^^^^^^^^^^^^^^^^^

You can set the default input of an step as a datum alias. Every time you run that step Valohai will fetch the data file that the alias is pointing to and use it to run the execution.

.. code-block:: yaml

  - step:
      name: Train Model
      image: tensorflow/tensorflow:1.13.1
      command: python myfile.py
      inputs:
        - name: myinput
          default: datum://train-images

..
