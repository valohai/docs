.. meta::
    :description: Valohai automatically keeps track of key information about your executions, making it easier to reproduce your experiments in the future and understand how they work.


Reproducibility and lineage 
#############################

Valohai automatically keeps track of key information about your executions, making it easier to reproduce your experiments in the future and understand how they work.

Details on all past executions
-------------------------------------------

* What code was ran to get the results of this execution?
    * For all executions that are based on a Git commit, Valohai will provide details of the commit and link back to it for details.
    * If the execution was ran as *--adhoc* or as a Notebook execution, you'll see ``adhoc`` under commit. Clicking the link will take you to details of the ``valohai.yaml`` configuration file, and allow you to download the code.
* Where the execution was ran (cloud or onprem) and what kind of hardware was used to run it?
* Which Docker image was used to run the execution?
* What was used as the input data for this execution? This could be for example training-data, labels, etc.
* Commands that were executed (for example if you executed a ``pip install`` to install additional dependencies that are not part of the original Docker image.
* Who, when and how much did it cost?

Trace models and data files
-------------------------------------------

In addition to seeing the outputs of each execution, you can trace files that you've connected to Valohai (inputs/outputs). This allows you to easily see which executions and deployments are relying on certain models, datasets, or output files.

Tracing a file will create a graph for you, that'll show:

* How was this file generated? Which executions resulted in this file?
* Which executions and deployments are relying on this file?

Go to your project's data tab to see all your files and trace them.

Metadata
-------------------------------------------

On top of all the data that Valohai is collecting about your executions, you can also easily create your metadata from your executions.

* Metadata can be anything: performance metrics, details about the libraries you're using, and anything else.
* This data is then visible on the Metadata tab inside each execution.

Use tags to easily identify certain executions
-------------------------------------------------------

Tags are useful when you for example want to highlight an execution that lead to an update in production. Or just want to make it easier for your team members to find certain executions, so they don't want to scroll through hundreds of experiments you ran in the project.

Set tags at the bottom of each execution's Details tab.