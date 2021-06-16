
.. meta::
    :description: Tag files

.. _howto-data-tag-files:

Attach tags and metadata to your files
#########################################

.. admonition:: Quick recap
    :class: tip

    * Tagging files allows you to easily find and sort data files
    * Use can use tag names when searcing for an execution input file, or any data from your outputs
    * In addition to tags, you can send arbitrary JSON metadata to be stored with your files.

..

Tag a file
--------------

You can add tags to the files either in the UI or during an execution.

.. tab:: Web UI

    Add tags in the **Data** tab of the project, or in executions outputs.

    .. video:: /_static/videos/datum-tags.mp4
        :autoplay:
        :width: 600

.. tab:: Programatically

    You can save tags to your outputs by saving an additional JSON file ``<filename.ext>.metadata.json`` for each of your execution's output files.

    Everything that you store in the ``valohai.tags`` section will be used as the file's tags in Valohai.

    .. code-block:: python
        :linenos:
        :emphasize-lines: 3,4,5,6,11,12,13

        import valohai
        import json

        metadata = {
            "valohai.tags": ["production", "lemonade"]
        }

        save_path = valohai.outputs().path('model.h5')
        model.save(save_path)

        metadata_path = valohai.outputs().path('model.h5.metadata.json')
        with open(metadata_path, 'w') as outfile:
            json.dump(metadata, outfile)


    ..


Find a file using tags
--------------------------

Once a file has been tagged you can easily find it in the UI.

1. Create a new execution
2. Add a new data file
3. Search by tag name

.. video:: /_static/videos/datum-tag-find.mp4
    :autoplay:
    :width: 600


.. tip:: 

    You can also search for files by tags using the Valohai APIs (e.g. ``https://app.valohai.com/api/v0/data/?project=<project-id>&tag=production``)

    Learn more about the `DatumList API <https://app.valohai.com/api/docs/#operation/DatumList>`_.

Store arbitrary metadata with your files
------------------------------------------

You can attach additional metadata to each file you output from an execution by saving a ``.metadata.json``-file. The file should contain, in JSON format, all the metadata you're looking to save with the file.

Valohai will store the contents of the ``<filename.ext>.metadata.json``-file with the output file.

You can access the files metadata using Valohai `DatumList API <https://app.valohai.com/api/docs/#operation/DatumList>`_ or `DatumRetrieve API <https://app.valohai.com/api/docs/#operation/DatumRetrieve>`_.

.. code-block:: python
    :linenos:
    :emphasize-lines: 4,5,6,7,8,13,14,15

    import valohai
    import json

    metadata = {
        "valohai.tags": ["prod", "lemonade"], # creates Valohai tags for the file
        "valohai.alias": ["model-prod"], # creates or updates a Valohai data alias to point to this output file
        "key": "value",
        "sample": "metadata"
    }

    save_path = valohai.outputs().path('model.h5')
    model.save(save_path)

    metadata_path = valohai.outputs().path('model.h5.metadata.json')
    with open(metadata_path, 'w') as outfile:
        json.dump(metadata, outfile)

Read a files metadata
------------------------------------------

You can access the metadata that you've attached to a file either through the Valohai API or during an execution.

Access files metadata during an execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Any metadata created with datums is available during runtime under the `/valohai/config/inputs.json` file.

.. code-block:: python

    import json

    with open('/valohai/config/inputs.json') as json_file:
        vh_inputs_config = json.load(json_file)
        
    # Print metadata from each file that is in the input named "myinput"
    for data in vh_inputs_config['myinput']['files']:
        print(data["metadata"])

..

.. seealso::

    * `File-based configuration </topic-guides/executions/file-config/#valohai-config-inputs-json>`_ 
    * `Fetch Datum with Valohai APIs <https://app.valohai.com/api/docs/#operation/DatumRetrieve>`_ 

