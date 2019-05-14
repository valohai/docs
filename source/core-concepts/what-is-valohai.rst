.. meta::
    :description: What is Valohai and how do machine learning systems work?

What is Valohai?
================

From the theoretical point-of-view, Valohai is **a predictive model life-cycle management platform** for building machine learning systems.

Machine learning system is an end-to-end machine learning solution that `...`

1. `...extracts features from data.`
2. `...feeds features to a training to produce models.`
3. `...uses these models to make predictions.`

These three pieces are always part of any machine learning solution; be it a self-driving car, a web store recommendation widget or your hobby project. **Valohai guides and supports you in building such systems** in various automated ways which we'll be covering in this documentation. All :doc:`projects </core-concepts/projects>` won't be needing each of the following use-cases but you should be able to recognize your individual requirements from the list below.

From the technical point-of-view, Valohai is **a workload processing ecosystem** akin to continuous integration or build systems. We receive your code, :doc:`configuration </valohai-yaml/index>` and :doc:`data sources </core-concepts/data-stores>` and make your pipelines work smoothly on top of an automated infrastructure with a beautiful interface. We run on all the major cloud-providers and custom hardware.

Valohai manages **executions**; you can think of them as "jobs" or "experiments" and they are covered in more detail on :doc:`a dedicated Executions page </core-concepts/executions>`. Of course we have a lot of additional bells-and-whistles for data science workflows like you can see by exploring the rest of the documentation.

Here is a list of the most common use-cases how people use Valohai in production and briefly explained how they can be implemented in the context of our platform:

* **Data Transformation:** An execution that takes input files, runs a bunch of transformation commands against the input producing the outputs.
* **Data Augmentation:** This works essentially the same as data transformation, just that the end goal and program logic used are different.
* **Data Anonymization:** This is also the same as data transformation, you just redefine the program logic and you are good to go.
* **Data Synthetization:** Here the execution receives no inputs, just generates output according to provided parameters e.g. with Unity or other generator software.
* **Data Management:** Valohai keeps track of all files and pieces of data it sees. You can easily search, download and delete any piece of data.
* **Iterative Development:** Our command-line client has ``--adhoc`` feature which allows packaging local code and run it on a remote, usually more power, machine that is closer to your data sources to reduce latency.
* **Training:** An execution that takes training/validation data as inputs, runs training framework on the data and uploads a model as an output.
* **Hyperparameter Optimization:** Valohai :doc:`tasks </core-concepts/tasks>` are essentially collections of executions that are aimed to solve one experiment or assignment. The most common task type is hyperparameter optimization which you can trigger using Valohai web interface.
* **Model Management:** Valohai manages all artifacts it produces, and naturally predictive models are first class citizens in this system.
* **Model Analysis:** An execution takes model as an input and produces analysis results as :doc:`metadata </core-concepts/metadata>` (JSON) or output files.
* **Model Interpretability:** As we version control everything that goes into building a model (code, parameters, inputs, environment, etc.) our APIs offer vast explanations how the model was build. Only requirement is that you did all the work on Valohai as any data that comes outside of Valohai ecosystem breaks the lineage.
* **Simulation:** Running multiple processes (the agent and the simulator) inside a single execution. Inter-worker communication is not possible at the moment.
* **Batch Inference:** An execution that takes samples and a model as inputs, runs the model against the samples and outputs predictions and any other analysis.
* **Model Serving:** Valohai Deployments can be used to start managed REST HTTP endpoints on top of shared or private Kubernetes clusters.
* **Online Experimentation:** Valohai Deployments have "aliases" like "staging/production" or "aaa/bbb". These can be used to track differences between two competing predictive model versions.

What Valohai `doesn't` automatically help with:

* **Building Your Actual Model Logic:**
  Valohai doesn't offer drag-n-drop interfaces to build predictive models. Valohai users must provide actual program logic in their programming language of choosing like Python, R or C++.
* **Interactive Big Data Exploration:**
  Valohai workers are ephemeral; they download/stream your data, do the instructed work and the runtime environment is destroyed along with the temporary data version. Depending on your data volume, you should use Jupyter Notebooks or something similar to interactive explore your dataset or a slice of it.
* **Data Acquisition:**
  We integrate with all the major cloud-based binary data sources and you should those to ingest your data. Valohai itself doesn't provide features to acquire new data samples. After the data is in AWS S3, Azure Store, Google Cloud Store, OpenStack Swift or on a local mount, you can begin using Valohai.
* **Data Labeling:**
  Valohai workers do have Internet connection in all license levels above `the Free tier <https://valohai.com/pricing>`_, but workers cannot be used to reliably host web servers or other services. This is by design; they are meant to be ephemeral. Theoretically you could host a labeling service on top of Valohai Deployment but none of the tools are built labeling in mind.
