.. meta::
    :description: What is Valohai and how do machine learning systems work?

What is Valohai?
================

This section discusses the following topics:

.. contents::
   :backlinks: none
   :local:

"So, what *is* Valohai?"
------------------------

From a theoretical point-of-view, Valohai is **a predictive model lifecycle management platform** for building
*machine learning systems*. Valohai governs statistical models all the way
from birth (preprocess + train + deploy) to termination (you stop using the model predictions).

*A machine learning system* is an end-to-end machine learning solution that `...`

1. `...extracts features from data (labeled or unlabeled)`
2. `...feeds those features to a training software to construct predictive models`
3. `...uses these models to make predictions on unseen data`

These three pieces are always part of any machine learning solution; be it a self-driving car,
a web store recommendation widget or your hobby project on your local machine.
**Valohai guides and supports you in building such systems** in numerous automated ways which we'll
be covering throughout this documentation.

From a technological point-of-view, Valohai is **a workload processing ecosystem** akin to a continuous
integration or build system. Valohai fetches your code, :doc:`configuration </valohai-yaml/index>`
and :doc:`data sources </core-concepts/data-stores>` and makes your pipelines work smoothly on top of
an automated infrastructure with a beautiful user interface. Valohai runs on top of all the major cloud-providers
as well as on-premises.

Valohai manages **executions**; you can think of them as "jobs" or "experiments".
These are covered in more detail in :doc:`the dedicated Executions page </core-concepts/executions>`.
Valohai includes additional bells-and-whistles for data science workflows,
like you can see by exploring the rest of the documentation.

"That is cool and all, but what do I *use* Valohai for?"
------------------------------------------------------

Here is a list of the most common use-cases of how people use Valohai in production and briefly explained how they can be implemented in the context of the Valohai ecosystem.

Your machine learning system won't be needing all of the following components but you can surely recognize some potential use-cases from the list below.

**Data Transformation:**
    An execution that takes input files, runs a bunch of transformation commands against the input producing outputs to the file system, external API, database or similar.

**Data Augmentation:**
    This works essentially in the same way as data transformation, just that the end goal and the program logic used are slightly different.

**Data Anonymization:**
    This is also the same as data transformation, except that your code is different.

**Data Synthetization:**
    Here the execution receives no inputs, just generates output according to provided parameters e.g. with Unity or other some synthetic generator software.

**Data Management:**
    Valohai keeps track of all files and pieces of data it sees. The data is always securely stored in your own managed data storage and only references are stored inside Valohai. You can easily search, download and delete any piece of data.

**Iterative Development:**
    :doc:`The Valohai command-line client </valohai-cli/index>` has an ``--adhoc`` feature which allows packaging local code and running it on a remote machine, usually with more power than your local laptop. The remote machine is usually also closer to your data sources, to reduce latency. Valohai also has a Jupyter notebooks addon for iterative development.

**Training:**
    An execution that takes training/validation data as inputs, runs your training code (using your ML framework of choice) on the data and saves a model as its output.

**Hyperparameter Optimization:**
    Valohai :doc:`tasks </core-concepts/tasks>` are essentially collections of executions that are aimed to solve one experiment or assignment. The most common task type is hyperparameter optimization which you can trigger using Valohai's web interface.

**Model Management:**
    Valohai manages all artifacts it produces, and naturally predictive models are first class citizens in this system. All models managed by the platform are stored in your own data store, ensuring your data, code and IPR always stays with you.

**Model Analysis:**
    While executing your code, Valohai lets you produce analysis results that you can view in real time while the model is trained under :doc:`metadata </executions/metadata/index>`. This metadata is produced by your code outputting JSON data to STDOUT or output files which can be read in real-time by e.g. tools such as TensorBoard.

**Model Interpretability:**
    Because Valohai version controls everything that goes into building a model (code, parameters, inputs, environment, etc.) its APIs offer vast explanations of how the model was build. The only requirement is that you did all the work on Valohai as any data that comes outside of Valohai ecosystem breaks the lineage.

**Simulation:**
    Running multiple processes (the agent and the simulator) inside a single execution. Handly for example in reinforcement learning cases. Instead of inter-worker communication, where you would run the agent and simulator on separate physical machines or Docker containers we recommend doing all on one machine to speed up time to results.

**Batch Inference:**
    An execution that takes samples and a model as inputs, runs the model against the samples and outputs predictions and any other analysis.

**Model Serving:**
    Valohai Deployments can be used to start managed REST HTTP endpoints on top of shared or private Kubernetes clusters.

**Online Experimentation:**
    Valohai deployments HTTP-endpoints can have "aliases" like "staging/production" or "aaa/bbb". These can be used to track differences between two competing predictive model versions or different end-points that the software uses to interact with the models.

.. note::

    And notice that **anything** you run on Valohai is automatically recorded, version controlled, secured, reproducible and shared between your team of data scientists.

"Wow, seems like Valohai can do anything!"
------------------------------------------

Yes, as you can run virtually any code on Valohai so it can do *almost* anything, with varying degrees of required effort.
We offer a lot of helpful tooling around data science workloads like data preprocessing, training, data management
and the rest of the use-cases mentioned above.

Here are some use-cases that Valohai *doesn't* automatically help you with:

**Building Your Actual Model Logic:**
  Valohai doesn't offer drag-n-drop interfaces to build predictive models. Valohai users must provide actual program logic in their programming language of choosing like Python, R or C++. Valohai supports all programming languages, frameworks and development tools.
**Interactive Big Data Exploration:**
  Valohai workers are ephemeral; they download/stream your data, do the instructed work and the runtime environment is destroyed along with the temporary data version. Depending on your data volume, you should use Jupyter Notebooks or something similar to interactively explore your dataset or a slice of it.
**Data Acquisition:**
  We integrate with all the major cloud-based binary data sources and you should use those to ingest your data. Valohai itself doesn't provide features to acquire new data samples. After the data is in AWS S3, Azure Store, Google Cloud Store, OpenStack Swift or on a local mount, you can begin using Valohai.
**Data Labeling:**
  Valohai workers do have Internet connection in all license levels above `the Free tier <https://valohai.com/pricing>`_, but workers cannot be used to reliably host web servers or other services. This is by design; they are meant to be ephemeral. Theoretically you could host a labeling service on top of Valohai Deployment but none of the tools are built with labeling in mind. There are other good labeling tools available, such as for example `Labelbox <https://labelbox.com/>`_.
