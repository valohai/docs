.. meta::
    :description: Adding a valohai.yaml configuration file to an existing project

.. _new-user-guide-yaml:

Add a ``valohai.yaml`` configuration file
##########################################

.. raw:: html

    <div style="position: relative; padding-bottom: 53.25443786982249%; height: 0;"><iframe src="https://www.loom.com/embed/d9fb29af8cdd48348e1db4712d54478a" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


Valohai is completely technology agnostic. You can develop in notebooks or scripts in a language and framework of your choice.

.. admonition:: valohai.yaml
  :class: important

  Valohai expects that you have a :ref:`yaml` in the root of your repository. The file defines what kind of jobs can be executed inside your project, and the different properties of each job type (these are called steps in Valohai). 

  You can either write the ``valohai.yaml`` by hand or if you're using Python you can use the :ref:`valohai-utils` to define the configuration file in your code.


Let's start by bringing just a single job type to Valohai.

  
.. tab:: valohai-utils (Python)

  Open your existing Python file and define a Valohai step inside it:

  .. code-block:: python

    import valohai

    # Prepares a new step called train in valohai.yaml
    # Execute this Python file to run every time the train step is launched in Valohai
    valohai.prepare(step="train")

  You can now generate a ``valohai.yaml`` configuration file that includes the ``train`` step by running:

  .. code-block:: bash

    vh yaml step myfilename.py

  This will create:

  * A ``valohai.yaml`` file with the ``train`` step that will run:

    * ``pip install -r requirements.txt``
    *  your Python script.

  * A ``requirements.txt`` with ``valohai-utils``
    
    * If you have an existing ``requirements.txt`` file the ``valohai-utils`` line will be just added there.

  By default, your step will use a standard Python Docker image and install everything from ``requirements.txt`` during runtime.

  You could also specify a different Docker image by passing the image name to ``prepare``.

  .. code-block:: python

    import valohai

    # Prepares a new step called train in valohai.yaml
    # Execute this Python file to run every time the train step is launched in Valohai
    # inside a GPU enabled Tensorflow 2.6.1 image.
    valohai.prepare(step="train", image="tensorflow/tensorflow:2.6.1-gpu")

  and then rerun ``vh yaml step`` to update your ``valohai.yaml``.

  .. code-block:: bash

    vh yaml step myfilename.py


.. tab:: Other

    Create a new file called ``valohai.yaml`` and define a :ref:`step` inside it.

    In our example below we're defining two commands to be ran every time the step called ``train`` is ran. You can remove the pip install command, if you don't have a need for it.

    .. code-block:: yaml

        - step:
            name: train
            image: tensorflow/tensorflow:2.6.1-gpu
            command:
              - pip install -r requirements.txt
              - python myfilename.py

    ..

You can now upload your local code to Valohai and run the ``train`` step inside the Docker container you just defined.

.. code-block:: bash

  vh execution run --adhoc train


.. admonition:: Using --adhoc
  :class: tip

  The ``--adhoc`` flag allows you to easily upload your local changes to Valohai without going through Git.
  Ideally, you'd always upload your changes to Git but sometimes it's just easier to test small changes using ``--adhoc``

  The other option would be to go through git:

  .. code-block:: bash

    git add .
    git commit -m "Added Valohai valohai.yaml"
    git push
    
    # Fetch new commits to Valohai
    vh project fetch
    # Run a new execution based on the latest Git commit
    vh exec run train