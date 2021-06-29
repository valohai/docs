
.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`learning-paths-fundamentals` series.
..

During execution the outputs are stored in ``/valohai/outputs`` directory. After the execution is finished, they will be automatically uploaded to the user configured data store. This will happen regardless of whether the execution was terminated as intended or stopped or crashed.

In this section you will learn:

- What is a datum identifier
- Where do you find datums
- How to set aliases for datums

.. admonition:: A short introduction to outputs
    :class: tip

    * At the end of each execution, outputs are stored in the default data store that is defined in your project settings
    * Valohai will handle authenticating with your cloud data store and uploading the data. You just have to save the file locally to ``/valohai/outputs/``
    * Uploading data never overwrites existing files. It is possible to upload multiple files with the same name. 
    * Each uploaded file will get a unique identifier called datum.
    * For easily accessing specific output files, it is possible to set aliases to datums. 

..
