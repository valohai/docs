:orphan: true

.. meta::
    :description: Documentation of Valohai machine learning platform guides through the core concepts of the platform and helps to get started in injecting best practices of machine learning development to everyday work.
    :orphan: true

.. vh_header::
    :title: Hello stranger 👋 How can we help you today? 

..

.. card_collection::
    :bgcolor: lightblue
    :name: quickstart-group
    :title: Run sample code on Valohai
    :subtitle: Import and run your quickstarts »
    :subtitle_link: /quickstarts

    .. card::
        :image: ../_images/tf_logo.png
        :image_alt: TensorFlow
        :box-style: center
        :cta_link: /quickstarts/quick-start-tensorflow

        Import and run our TensorFlow sample on Valohai.

    .. card::
        :image: ../_images/r_logo1.png
        :image_alt: R-language
        :box-style: center
        :cta_link: /quickstarts/quick-start-r

        Import and run our R sample on Valohai.

    .. card::
        :image: ../_images/jupyter_logo.png
        :image_alt: Jupyter Notebooks
        :box-style: center
        :cta_link: /quickstarts/quick-start-jupyter/

        Run experiments with Jupyter Notebooks.

    .. card::
        :image: ../_images/keras_logo.jpg
        :image_alt: Keras
        :box-style: center
        :cta_link: /quickstarts/quick-start-keras

        Import our Keras sample & run a deep mind transform on it.


.. card_collection::
    :bgcolor: lightblue
    :name: quickstart-group
    :title: Get started with these tutorials
    :subtitle: View all tutorials »
    :subtitle_link: /tutorials
    :class: no-padding

    .. card::
        :box-style: center
        :image: /_images/start_icon1.png
        :image_alt: Start
        :cta: 1. Learn the basics
        :cta_link:  /tutorials/valohai
        :button: red

        * Running experiments
        * Data inputs and outputs
        * Metadata and visualizations
        * Deployments

    ..

    .. card::
        :box-style: center
        :image: /_images/team_icon1.png
        :image_alt: Team
        :cta: 2. Onboard your team
        :cta_link: /tutorials/valohai/onboard-team
        :button: red

        * Connect your cloud storage
        * Configure environments
        * Reproducability and lineage
        * Manage organisation settings

    ..

    .. card::
        :box-style: center
        :image: /_images/advanced_icon1.png
        :image_alt: Advanced
        :cta: 3. Advanced topics
        :cta_link: /tutorials/valohai/advanced
        :button: red

        * Hyperparameter optimization
        * Automate a series of executions
        * Do more with Valohai APIs

    ..

..


.. card_collection::
    :bgcolor: lightblue
    :name: quickstart-group
    :title: Read about key Valohai features
    :subtitle: All core-concepts »
    :subtitle_link: /core-concepts

    
    .. card::
        :box-style: center
        :cta: Parameters »
        :cta_link:  /core-concepts/tasks
        :button: transparent

        Run hyperparameter optimization on Valohai.

    .. card::
        :box-style: center
        :cta: Metadata »
        :cta_link:  /executions/metadata
        :button: transparent

        Track additional metadata from your executions.

    .. card::
        :box-style: center
        :cta: Pipelines »
        :cta_link:  /core-concepts/pipelines
        :button: transparent

        Create a series of connected executions.
    
    .. card::
        :box-style: center
        :cta: Inference »
        :cta_link: /core-concepts/deployments
        :button: transparent

        Learn about real-time and batch inference.

.. vh_demo::
    :bg_color: lightblue
    :title: Looking to try out Valohai?
    
..

.. card_collection::
    :bgcolor: white
    :name: faq-executions-data
    :title: Frequently Asked Questions
    :subtitle: View all »
    :subtitle_link: /faq/

    .. card::
        :columns: 2
        :title: Executions »
        :title_link: /faq/#executions

        **How do I install additional libraries, tools and other dependencies to my execution?** 📦

        * You can define multiple commands under the ``step.command`` section in your valohai.yaml configuration. For example:
            
            .. code:: yaml

                - step:
                    name: train model
                    image: python:3.6
                    command:
                      - pip install mypackage1
                      - python train.py

            ..
            
            At some point, you might consider `building a custom Docker image </tutorials/build-docker-image/>`_ with all the dependencies and use it in your executions, instead of downloading and installing them at the start of every execution.
         
        **How do I change the default machine type for the executions in my project?**

        * Each project has a setting for "Default environment" that you can set in the web UI, valohai.yaml config as ``environment:`` or with the ``-e`` flag  when running CLI.

          You can set the default execution environment for each project in the projects' settings tab.


        **Why do some of my executions get queued?** 🕓

        * Each machine type on Valohai has a maximum scale setting that determines how many parallel executions can be ran per machine type. The setting can be configured from your organisations environment settings, if you're running Valohai workers in your own cloud environment or on-premises hardware.
    ..

    .. card::
        :columns: 2
        :title: Data »
        :title_link: /faq/#data

        **How do I access files from my cloud storage?** ☁️

        * Once you've defined the Data Stores under your execution settings, you can easily access the files by defining them as inputs in your valohai.yaml configuration file as HTTP, HTTPS or cloud provider specific data stores (s3://, gs:// etc.)
            
            .. code:: yaml

                - step:
                    name: train model
                    image: python:3.6
                    command: python train.py
                    inputs:
                      - name: myimages
                        default: s3://my-bucket/dataset/images/dataset.zip

            ..

            and then in your code ::

                import os

                # Get the path to the folder where Valohai inputs are
                input_path = os.getenv('VH_INPUTS_DIR')
                # Get the file path of the dataset you defined in the YAML
                myimages_file_path = os.path.join(input_path, 'myimages/dataset.zip')
        
        **How do I change where my output files are saved?**

        * In your projects settings you can define the 'Default upload store'. The options are a Valohai owned S3 storage and all the Data Stores you've configured for your project.

        **Can I get a list of all executions that are using a certain model or data set?**
        
        * Of course. Inside your project you'll find a Data-tab with all of your outputted data files. You can click *trace* on any of these to visualize how that file was created and where has it been used.
    ..

..

.. card_collection::
    :bgcolor: white
    :name: faq-dev-general
    :class: no-padding

    .. card::
        :columns: 2
        :title: Development »
        :title_link: /faq/#development

        **Do I need to commit and push after each code change?** 

        * Nope, you can use ``--adhoc`` runs to create one-off executions from local files. These ad-hoc executions allow quick iteration with the platform when you are still developing your whole pipeline. ``vh exec run --adhoc --watch name-of-your-step``

        **How do I use my own Docker images?** 🐳

        * Once you've published your Docker image, you can point your steps and deployments to it in your ``valohai.yaml``. 
        
          If you've published the image in a private container registry remember to `add your credentials under your organization settings </docker-images/#access-private-docker-repositories>`_.

        **How can I access files from my Git repository?** 

        * The contents of your repository's commit are available at ``/valohai/repository``, which is also the default working directory during executions.

    ..

    .. card::
        :columns: 2
        :title: Metadata »
        :title_link: /faq/#metadata

        **How do I collect metadata from my executions?** 📈

        * Valohai collects metadata from your executions by collecting JSON from the logs. Read our guide for details or try the Python sample below: ::

            import json

            def logMetadata(epoch, logs):
                print()
                print(json.dumps({
                    'epoch': epoch,
                    'loss': str(logs['loss']),
                    'acc': str(logs['accuracy']),
                }))

        **What can I do with metadata?** 🔎
        
        * Metadata is used to track key metrics from your executions. This can be visualized in a Times Seris or a Scatter Plot graph in the executions Metadata tab.

          Using the "Show Columns" button on the Execution view you can select to show each executions metadata in the table, for easy comparison.

          You can also export metadata using the Valohai APIs. `Follow our API quickstart <https://docs.valohai.com/quickstarts/quick-start-api/>`_ and make a request to /executions/{id}/metadata/

    ..

..

.. vh_row::
    :bg_color: dark
    :element_id: frontpageToC
    :title: Full Table of Contents

    .. toctree::
        :maxdepth: 2
        :titlesonly:

        core-concepts/index
        executions/index
        valohai-yaml/index
        valohai-cli/index
        jupyter/index
        valohai-api/index
        docker-images
        on-premises/index
        architecture/index
        faq/index
        tutorials/index

    ..
    
..