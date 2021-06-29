.. meta::
    :description: Defining inputs with valohai-utils.

Inputs
======

To get some data for your :doc:`step </topic-guides/core-concepts/steps>`, you need :doc:`inputs </reference-guides/valohai-yaml/step-inputs>`.
Inputs are basically the required files that are expected to be there when the code is executed.

With ``valohai-utils``, you define the inputs in the call to the :doc:`prepare() </topic-guides/valohai-utils/prepare()>` method.
Feed the ``default_inputs`` argument with a key/value dictionary of the inputs.

* **key** is the name of the input in the configuration YAML and in the Valohai UI.
* **value** defines the default uri of the input and also the type.

Defining inputs with ``valohai-utils`` solves these problems:

* Handling different input variations (single file, multiple files, archived files)
* Uncompressing archived files on-demand
* Filtering a subset of the input
* Downloading the inputs for local runs
* Parsing the command-line overrides
* Managing the duplicate definitions between Python & YAML

train.py
--------

Here we define a :doc:`step </topic-guides/core-concepts/steps>` ``train``,
with an :doc:`input </topic-guides/core-concepts/parameters>` ``training-images``.

.. code-block:: python

    import valohai


    inputs = {
        "training-images": "https://example.com/images.zip",
    }

    valohai.prepare(
        step="train",
        default_inputs=inputs,
    )

This key/value pair...

.. code-block:: python

    inputs = {
        "training-images": "https://example.com/images.zip",
    }

...will be transpiled into the following YAML

.. code-block:: yaml

    - name: training-images
      default: https://example.com/images.zip
      optional: false

.. note::

    Empty default value signals an  **optional** input.

    .. code-block:: python

        inputs = {
            "extra-images": "",
        }


    .. code-block:: yaml

        - name: extra-images
          optional: true

Accessing input files
---------------------

Once you have defined an input using the :doc:`prepare() </topic-guides/valohai-utils/prepare()>` method, you can access
the files by referring to the input name.

In Valohai, input is not a single file. It can be multiple URIs. And it doesn't end there.
Each of those URIs may actually represent multiple files on multiple folders. And some of those files may actually
be zip archives with multiple files and folders in them!

In other words, handling a Valohai input robustly is not as simple as it sounds. Luckily ``valohai-utils``
handles most of this complexity for you.

Use the ``.path()``, ``.paths()``, ``.stream()``, ``.streams()`` methods to access files of a single input.

Single file
-----------

When you are always expecting a single file, use ``.path()``.

.. code-block:: python

    import json
    import valohai

    inputs = {
        "my-config": "",
    }

    valohai.prepare(
        step="train",
        default_inputs=inputs,
    )

    with open(valohai.inputs("my-config").path()) as f:
        data = json.load(f)


Alternatively you can also use ``.stream()``

.. code-block:: python

    data = json.load(valohai.inputs("my-config").stream())


Even when you are always expecting a single file, your colleagues might still accidentally feed your input with
several files!

In that case, ``.path()`` or ``.stream()`` returns the first file it encounters, which can be brittle.

To be more explicit about the input, you can do this:

.. code-block:: python

    with open(valohai.inputs("my-config").path("*.json")) as f:
        data = json.load(f)

Or to be fully explicit

.. code-block:: python

    with open(valohai.inputs("my-config").path("config.json")) as f:
        data = json.load(f)


Multiple files
--------------

When handling an input with multiple files, you want to use ``.paths()`` or ``.streams()``

.. code-block:: python

    import valohai

    inputs = {
        "images": "https://example.com/images.zip",
    }

    valohai.prepare(
        step="train",
        default_inputs=inputs,
    )

    for image_path in valohai.inputs("images").paths():
        # Do something per image

The beauty of ``.paths()`` or ``.streams()`` is that the code above will handle all of these different input scenarios:

* Single ``my-image.jpg``
* Multiple images ``my-image1.jpg``, ``my-image2.jpg``, ``myimage-3.jpg``
* ``my-images.zip`` containing multiple images
* Multiple archives ``my-images1.zip``, ``my-images2.zip``, ``my-images3.zip``
* Hybrid mix of all the above

There is no longer need to write separate handler for each scenario, as ``valohai-utils`` is taking care of everything.
All you need to do is iterate over paths of an input.


Archives
--------

Archive files are automatically uncompressed under the hood when you are using ``.paths()`` and friends. Currently supported archive types are ``tar`` and ``zip``.

It is worth pointing out that the archives are not prematurely uncompressed to the disk.

The library is smart and uncompresses files on-demand. When you iterate over the
contents of a huge archive, each file is uncompressed one-by-one and the potential errors are raised immediately.

Sometimes you might want to specifically handle or uncompress the archives yourself, though.

In that case, you can set the ``process_archives=false``
which signals ``valohai-utils`` to not automatically uncompress the contents of archives, but return paths to the actual archive
files instead.

.. code-block:: python


    for image_path in valohai.inputs("zipped_images").paths():
        print(image_path) # image1.jpg, image2.jpg, image3.jpeg...

    for archive_path in valohai.inputs("zipped_images").paths(process_archives=false):
        print(archive_path) # images.zip

Filtering
---------

When you have multiple files in multiple folders as an input, you sometimes need only a subset.

All the four methods ``path()``, ``stream()``, ``paths()``, ``streams()`` support a wildcard filter.

Here are some examples of how to use the filter:

.. code-block:: python

    valohai.inputs("images").paths()
    valohai.inputs("images").paths("*.jpg")
    valohai.inputs("images").paths("dog_*.jpg")
    valohai.inputs("images").paths("training-set/*.jpg")
    valohai.inputs("images").paths("images/**/dogs/*.jpg")

Downloading
-----------

When you run your code remotely as an execution in the Valohai platform, all the downloading of the inputs is done by the platform.

When you run your code locally, the platform is not there to help. Instead, ``valohai-utils`` downloads the files from
the input URIs for you.

The files are placed in the automatically generated ``.valohai/inputs/{step_name}/{input_name}`` subfolder.

When the code is re-executed, the library doesn't try to download the files again, but uses the cached ones from the disk.
You can force the re-downloading by simply deleting the folder from the disk.

You can also create the ``.valohai/inputs/{step_name}/{input_name}`` folder manually and place some files in it, if you
just want to use local files as an input instead downloading from an URI.

Another alternative is to temporarily use a local default for an input:

.. code-block:: python

    inputs = {
        "images": "/tmp/images.zip",
    }

You can also override the default with the command-line. See the next section.

Overriding input URIs
---------------------

Inputs defined by the :doc:`prepare() </topic-guides/valohai-utils/prepare()>` often have a default value.

There are two ways to override the default (or empty) value:

* Command-line parameter (local)
* Valohai UI or CLI (remote)

Example (local):

.. code-block:: bash

    python train.py --images==/tmp/images.zip

.. code-block:: bash

    python train.py --images==https://alternative.com/images.zip

Example (remote):

.. code-block:: bash

    vh yaml step train.py
    vh exec run -a train --images==https://alternative.com/images.zip
