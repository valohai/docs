.. meta::
    :description: Defining outputs with valohai-utils.

Outputs
=======

Once your code has trained a model or preprocessed a dataset, it is time to output something.

An output is a collection of files, which is you consider worth saving and are sent back to the
data store by the Valohai platform.

You choose your output files by putting them in a special folder ``/valohai/outputs/{output_name}``.
Luckily ``valohai-utils`` makes this a bit easier.

Saving outputs with ``valohai-utils`` helps with these problems:

* Differences between local and remote execution
* Compressing outputs to a single archive
* Live upload

Saving an Output
----------------

Saving an output with ``valohai-utils`` is easy. You ask for a correct path from the library and save the file there.
The library creates the output folder automatically for you, if it already doesn't exists.

For example a step that resizes a single image, would look like this:

.. code-block:: python

    import valohai

    # Open the image
    image = Image.open(valohai.inputs('image').path())

    # Resize the image
    new_image = image.resize((width, height))

    # Query an output path for the filename "resized_image.png"
    out_path = valohai.outputs().path('resized_image.png')

    # Save the file to the output path
    new_image.save(out_path)

Outputs can also have names, which are basically subfolders. It is a good idea to use naming and not output everything
into the output root folder.

.. code-block:: python

    out_path = valohai.outputs("my-output").path('resized_image.png')
    print(out_path)  # my-output/resized_image.png

When building pipelines, you feed output(s) of one step as the input(s) of another, so
clearly naming your outputs will make your pipelines more explicit and robust.

Compressing Outputs
-------------------

It is often desired to archive the outputs. Not only do you save some space and get a quicker upload, but simply having a single
archive instead of 200,000 separate files is a lot easier to manage.

Let's say we have a step that resizes every ``.png`` file in the ``images`` input.

Here is an example of saving the resized images as a single archived output file (``resized/images.zip``).

.. code-block:: python

    import valohai

    for image_path in valohai.inputs('images').paths("*.png"):
        image = Image.open(image_path)
        new_image = image.resize((width, height))
        out_path = valohai.outputs("resized").path(f"resized_{os.path.basename(image_path)}")
        new_image.save(out_path)

    valohai.outputs('resized').compress("*.png", "images.zip")

By default, the original ``.png`` files are removed and just the archive is saved.
If you want to save **both** the original files and the archive, you can set the ``remove_originals`` to ``false``.

.. code-block:: python

    valohai.outputs('resized').compress("*.png", "images.zip", remove_originals=false)


Live Outputs
------------

During a remote execution, Valohai waits for the execution to finish and only uploads the outputs afterwards.

That said, you often want to upload your outputs right away and not wait for the entire step
to finish. In this case you can use the live uploading feature.

The way to request for a live upload is to call the ``live_upload()`` method. It sets
the file as read-only, which signals to the Valohai platform that this file can be uploaded immediately.

.. code-block:: python

    # Query an output path for the filename "resized_image.png"
    out_path = valohai.outputs().path("resized_image.png")

    # Save the file to the output path
    new_image.save(out_path)

    # Request for an immediate upload
    valohai.outputs().live_upload("resized_image.png")

    # Carry on doing something else...

Local and Remote
----------------

When your code is executed remotely in the Valohai platform, the outputs are put into a special
folder, which Valohai then sends them onward to the data store.

When your code is executed and debugged locally, you don't want things to be sent anywhere, but you
do want them to be saved to the hard disk.

When you call ``valohai.outputs("my-output")``, the library knows whether the code is running locally or remotely
and chooses the correct folder.

This is where the file will end up under the hood:

* Local execution: ``.valohai/outputs/{hash}/my-output``
* Remote execution: ``/valohai/outputs/my-output``

For each local run, a new ``{hash}`` is generated. The hash starts with a timestamp to make the latest outputs easier to find.

.. note::

    If you want to override the target folder for local or remote execution, set the ``VH_OUTPUTS_DIR`` environment variable.
