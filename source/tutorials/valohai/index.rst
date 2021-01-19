.. meta::
    :description: In this quickstart you'll learn about the key Valohai features like executions, downloading data from your cloud storage, tracking and visualizing your metadata, saving experiment files and models to a cloud storage, and finally deploying a model for online inference.

Valohai Quickstart 🦈✨
============================

This tutorial is aimed to help you get a fast-start with key Valohai features.


.. container:: alert alert-warning

    **Before you start**

    * Make sure you have Python 3 and pip installed on your machine
    * You should have an active account on Valohai
    * This tutorial is heavily relying on the valohai command line tools. Check out our `Jupyter Quickstart </quickstarts/quick-start-jupyter/>`_ or `Tensorflow Quickstart </quickstarts/quick-start-tensorflow>`_ if cli isn't your thing.

..

⚙️ Setup your environment
--------------------------

* Create an empty folder where we'll store all the tutorial files.
* Create ``train.py`` inside the folder. We'll write model training code in this file.
* Add ``print("Hello Valohai!")`` to ``train.py`` so we have a simple execution to test with.

* Create a virtual environment for Python 3, where we'll install all the libraries needed.
    * ``python3 -m virtualenv .venv``
    * ``source .venv/bin/activate``


📄 Create a new project
------------------------------

.. container:: collapse.show cli-example

    Next we'll initialize a wizard to create our Valohai project and our ``valohai.yaml`` configuration file. This is the main configuration file for Valohai. It will describe the commands Valohai should run, which Docker image to use, the inputs, parameters etc.

    * Install Valohai CLI tools ``pip install valohai-cli``
    * Login to valohai-cli with ``vh login``
    * Initialize a new Valohai project with ``vh init``
        * Choose ``python train.py`` as the command
        * Write ``tensorflow/tensorflow:2.0.1-py3`` as the Docker image. The wizard will list some popular options that you can choose from but for the purpose of this tutorial we'll use the newest TensorFlow image from `Docker Hub <http://hub.docker.com>`_.
    * Based on your answers the wizard generated a ``valohai.yaml`` configuration file. We'll get familiar with the file in this quickstart, but for now you can just approve it as is.
    * Next you'll need to connect your working directory and configuration file to a Valohai project. Select to create a new project with ``C`` and name it valohai-quickstart.
    * You can now login to `app.valohai.com <https://app.valohai.com>`_ where you'll see your new project.
    * 🔥 To start an execution through your command line run ``vh execution run --adhoc execute``. This will launch a new execution in your project and run through our highly complex Hello World sample 😅
        * You can see the execution logs in the browser: *Project -> Executions -> Execution #1 -> Logs*

    .. note ::

        * ``--adhoc`` uploads your working directory to Valohai to run the execution, instead of having to push changes to your source control every single time.
        * The last parameter (*execute*) determines which step of your project should be executed on Valohai. The steps are defined in ``valohai.yaml`` and instead of making us write the whole step name ``Execute python train.py``, Valohai accepts *execute* as there is only one step starting with that word.
        * You don't have to always go to the browser to see your execution logs. You can just include the ``--watch`` flag to receive the logs back in your command line.

    ..

    * Let's edit our configuration file and change the step name to be more descriptive of what we'll be doing. Open ``valohai.yaml file`` in your favorite editor and change the step name to *Train MNIST model*. Once you've saved the file you can create a new execution with ``vh execution run --adhoc train --watch``

    Now pat yourself on the back, you just created a project and ran your first execution on Valohai! 🦈🎉
..


💻 Write your code
----------------------

Now that we've gotten our first executions running on Valohai, we can focus on writing our classifier that we'll train on Valohai. 

.. container:: alert alert-warning

    **Our sample code**

    To keep things simple we'll use the `TensorFlow 2 quickstart for beginners <https://www.tensorflow.org/tutorials/quickstart/beginner>`_ which trains a simple MNIST digit prediction model. The below code is directly from the TensorFlow quickstart and doesn't have anything Valohai specific lines in it.

..

* Replace ``train.py`` with the code from the quickstart --- or just copy it from below 🤷‍♂️🤷‍♀️
    .. code:: python

        import tensorflow as tf

        mnist = tf.keras.datasets.mnist

        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0

        model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
        ])

        predictions = model(x_train[:1]).numpy()
        predictions

        tf.nn.softmax(predictions).numpy()

        loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

        loss_fn(y_train[:1], predictions).numpy()

        model.compile(optimizer='adam',
                    loss=loss_fn,
                    metrics=['accuracy'])

        model.fit(x_train, y_train, epochs=5)

    ..

* Lets now train our MNIST model on Valohai. You'll just need to the familiar ``vh execution run --adhoc train`` and check the logs to ensure everything is executing as expected.

Look at you go.. already trained your first model on Valohai 👏👏

.. seealso::

    * `valohai.yaml - config file </valohai-yaml>`_
    * `What are executions? </core-concepts/executions>`_
    * ``vh exec`` `command details </valohai-cli/reference/execution>`_
    * `Docker Images </docker-images>`_
..

☁️ Saving execution outputs to cloud storage
------------------------------------------------

So you just ran your model, trained a beautiful handwritten digit classifier but the model is nowhere to be found 😲

To output your model file, or any other file, you'll need to save it to the Valohai machine's output directory. All files from the output directory will get uploaded to your cloud storage at the end of an execution, regardless if it succeeded or failed.

* First ``import os`` in your ``train.py``, so we can access the OS environment variables.
* Then create a new variable to store the Valohai output file
    .. code:: python

        # Get the output path from the Valohai machines environment variables
        output_path = os.getenv('VH_OUTPUTS_DIR')

    ..
* At the bottom of your file call model.save to save the model's architecture, weights and training in a single file, as described in the TensorFlow documentation.
    .. code:: python

        # Save our model to that the output as model.h5
        # /valohai/outputs/model.h5
        model.save(os.path.join(output_path, 'model.h5'))

    ..

* 🔥 Now lets run a new execution to output and upload our mode file to the cloud. Run ``vh exec run --adhoc train`` to start another execution. You'll see that the model appears in the outputs tab from where you can download it, trace it and get a link for it.


.. container:: alert alert-warning

    **Remember:**

    * You can output any files from your executions (JSON, .csv, images, etc.) and they'll get uploaded to the cloud storage once the executions ends.
    * The files that you've saved to outputs will be uploaded to the cloud storage even if an executions fails on an error.
    * By default these files will be uploaded to a Valohai owned AWS S3 Bucket from where only your account can access it.

..

.. seealso::

    * `Connect your cloud storage </tutorials/cloud-storage/>`_ to have files upload to your own storage.
    * `Live Outputs </executions/live-outputs/>`_ to upload files during the execution run, instead of waiting till the end.

..

📈 Tracking and visualizing metadata
-------------------------------------------

Valohai will keep track of the input data used, the commands, the code version, the environment you ran it on and other key information. You might have additional metrics you want to keep track of in your executions, and use to compare your models. That's where Valohai metadata comes in.

* For our training, we want to write a function that outputs loss and accuracy at the end of each epoch 📈
* Everything that you output as JSON will get picked up by Valohai as potential metadata.
    * So start by adding ``import json`` to ``train.py``
* Create a new function ``logMetadata`` in which we'll output the metadata values we want to track (epoch, loss, accuracy). 
    .. code:: python

        # A function to write JSON to our output logs
        # with the epoch number with the loss and accuracy from each run.
        def logMetadata(epoch, logs):
            print()
            print(json.dumps({
                'epoch': epoch,
                'loss': str(logs['loss']),
                'acc': str(logs['accuracy']),
            }))
    ..
* The TensorFlow documentation describes the `LambdaCallback <https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/LambdaCallback>`_, which allows us to create simple, custom callbacks once each epoch end.
    * Add ``metadataCallback = tf.keras.callbacks.LambdaCallback(on_epoch_end=logMetadata)`` after the function definition, so the function is called at the end of every epoch.
* Finally use metadataCallback in model.fit as described `in the TensorFlow documentation <https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/LambdaCallback#example>`_.
    * ``model.fit(x_train, y_train, epochs=5, callbacks=[metadataCallback])``
* 🔥Ready to be amazed? Run ``vh exec run train --adhoc`` to start a new execution. Head over to the Metadata-tab of the execution to see your metadata collected and visualized.

**BOOM!** You did it again! 🙌 This is a good moment to take a break and celebrate your great achievements 🎉

.. image:: /_images/metadata_graph.png
   :alt: Metadata on time series

.. container:: alert alert-warning
    
    **Remember**
    
        * You're not limited to just accuracy and loss. You can output whatever you want as metadata. As long as you can output it as JSON, we'll save it for you.
        * JSON will want all the values in string format. That's why we casted ``logs['loss']`` and ``logs['accuracy']``, which TensorFlow returns as ``float``, to a string in the above sample.
..

.. seealso::

    * `Docs: Creating Visualizations </executions/metadata/>`_
    * `TensorBoard + Valohai Tutorial <https://blog.valohai.com/tensorboard-tutorial>`_

..

☁️ Download training data from a cloud storage
--------------------------------------------------

Currently we download our training data directly through TensorFlow with ``mnist.load_data()``. Instead of doing that we'll want to download our data from our own cloud storage.

* Let's start by **removing** these lines from our ``train.py``
    .. code:: python

        mnist = tf.keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
    ..
* Download the MNIST dataset to your computer from `https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz <https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz>`_
* Next we'll upload the file to our cloud storage. In your browser go to your project's Data-tab and upload your mnist.npz dataset. Then copy to the datum:// address from the Browse-tab.
    * By default your file will be uploaded to the ``Valohai Managed S3``. That's good enough for now.
* Now update the ``valohai.yaml`` configuration and define a new input with a default download location. Paste your datum url as the default address.
    .. code:: python

        - step:
          name: Train MNIST model
          image: tensorflow/tensorflow:2.0.1-py3
          environment: azure-westeurope-f2sv2
          command: python train.py
          inputs:
            - name: my-mnist-dataset
              default: {datum://id}
    ..

* Back in your ``train.py`` at the beginning of the document find the downloaded .npz file from the inputs folder.
    .. code:: python
    
        # Get the path to the folder where Valohai inputs are
        input_path = os.getenv('VH_INPUTS_DIR')
        # Get the file path of our MNIST dataset that we defined in our YAML
        mnist_file_path = os.path.join(input_path, 'my-mnist-dataset/mnist.npz')
    ..
* ``import numpy`` and use it to load the file and define the train and test datas.
    .. code:: python

        with numpy.load(mnist_file_path, allow_pickle=True) as f:
            x_train, y_train = f['x_train'], f['y_train']
            x_test, y_test = f['x_test'], f['y_test']
    ..
* Run a new execution with ``vh exec run --adhoc train`` to start a new execution that uses your downloaded data.

You'll noticed that on the surface it looks like nothing changed 😓 but on the details page you'll see the input we defined and if you look at the logs, you'll notice that it's downloading the dataset from a new location.

* Now that the input is defined in your YAML, you can easily change the input URL when you create executions from the UI. You can see this by going inside an execution and clicking *Copy* to create a new execution from the UI.

.. container:: alert alert-warning

    **Remember**
    
    * Valohai doesn't take a copy of your data and store it. We keep track of the input data name/location that you defined, so you can later on easily reproduce your steps, but it's up to you do data versioning and ensure that data source still exists.
    * You can define inputs through HTTP, HTTPS or cloud provider specific data stores (s3://, gs:// etc.)
    * Valohai will show an alert on the execution if the data behind the link has changed. For example if someone else has edited to file that you're getting your input data from.
..

.. seealso::
    * `Connect your own cloud storage </tutorials/cloud-storage>`_ 
    * `Prevent caching data <https://docs.valohai.com/valohai-yaml/step-environment-variables/#special-environment-variables>`_
..


🔮 Publish your model for online inference
---------------------------------------------

Valohai makes it easy to publish your model for online inference through a Kubernetes cluster. By default the cluster is hosted by Valohai but it can installed in your own environment.

In this tutorial we'll deploy our model and serve predictions through `WSGI <https://wsgi.readthedocs.io/en/latest/index.html>`_ using the `werkzeug <https://www.palletsprojects.com/p/werkzeug/>`_ utility library.

.. container:: alert alert-warning

    **Before you start**

    * Majority of the code below is related to reading an image from a HTTP POST request and using the TensorFlow model we created to predict a digit from an image.
    * The actual Valohai configuration is at the end, when we define the endpoint in the ``valohai.yaml`` configuration file.

..

* First download the ``model.h5`` file from your previous executions outputs. You might need to rename the downloaded file to ``model.h5``, so it's easier to find.

Create a function that will do the prediction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Create a new folder called ``.models`` and move the ``model.h5`` there
* Create a new file called ``predict.py`` where we'll store our prediction code. We'll base our sample on the `werkzeug sample from their site <https://www.palletsprojects.com/p/werkzeug/>`_.
    .. code:: python

        from werkzeug.wrappers import Request, Response

        # Location of our model
        model_path = 'model.h5'

        # Store our model
        mnistModel = None

        # Define the main function that Valohai will call to do the prediction
        def mypredictor(environ, start_response):
            # Create a new response object
            response = Response("Hello world!") 
            # Send back our response
            return response(environ, start_response)

        # When running locally
        if __name__ == "__main__":
            from werkzeug.serving import run_simple

            # Update model path to point to our downloaded model when testing locally
            model_path = '.models/model.h5'

            # Run a local server on port 5000.
            run_simple("localhost", 8000, mypredictor)

    ..
    
    * Install the werkzeug library with ``pip install werkzeug`` and then test your code by running the code locally ``python predict.py``. Navigate to `localhost:8000 <http://localhost:8000/>`_ to see the result.
* Our model will need an image sent to it to be able to predict the digit. So let's create a new function ``read_input`` that will read an image from the HTTP POST request sent to the prediction service.
    .. code:: python
        
        import io
        import numpy
        from PIL import Image

        def read_input(request):
            # Ensure that we've received a file named 'image' through POST
            # If we have a valid request proceed, otherwise return None
            if request.method != 'POST' and 'image' not in request.files:
                return None
            
            # Load the image that was sent
            imageFile = request.files.get('image')
            img = Image.open(imageFile.stream)
            img.load()

            # Resize image to 28x28 and convert to grayscale
            img = img.resize((28, 28)).convert('L')
            img_array = numpy.array(img)

            # We're reshaping the model as our model is expecting 3 dimensions
            # with the first one describing the number of images
            image_data = numpy.reshape(img_array, (1, 28, 28))

            return image_data

    ..
    
    * Take some time to read through the code to understand what is happening. You'll notice we're using a the Pillow (PIL) to open the Image, so let's install it with ``pip install pillow``
* You'll need to update your ``mypredictor`` to take in the request and check if there is an image in the request.
    .. code:: python

        def mypredictor(environ, start_response):
            # Get the request object from the environment
            request = Request(environ)

            # Get the image file from our request
            inputfile = read_input(request)
            
            # If read_input didn't find a valid file
            if (inputfile is None):
                response = Response("\nNo image", content_type='text/html')
                return response(environ, start_response)

            response = Response("\nWe got an image!") 
            return response(environ, start_response)
        
    ..
    
    * Now run your code locally again with ``python predict.py`` and send it an image as an example. You can use ``curl`` on the command line to test this.
        * Open a new command line window, navigate to the folder with your test image (7.png) and run ``curl -X POST -F "image=@7.png" localhost:8000/``
            .. image:: /_images/7.png
                :alt: Handwritten digit 7
                :width: 150px

* Next we'll load our ``model.h5`` file and use it to predict the class (7) of our sample image. We'll return the prediction results as json.
    * First ``import json`` and ``import tensorflow as tf`` at the top of your ``predict.py```
    * Update ``predict.py`` to take load the model, predict the class and return a json result
        .. code:: python
    
            def mypredictor(environ, start_response):
                # Get the request object from the environment
                request = Request(environ)

                global mnistModel
                if not mnistModel:
                    mnistModel = tf.keras.models.load_model(model_path)

                # Get the image file from our request
                image = read_input(request)

                # If read_input didn't find a valid file
                if (image is None):
                    response = Response("\nNo image", content_type='text/html')
                    return response(environ, start_response)


                # Use our model to predict the class of the file sent over a form.
                prediction = mnistModel.predict_classes(image)

                # Generate a JSON output with the prediction
                json_response = json.dumps("{Predicted_Digit: %s}" % prediction[0])

                # Send a response back with the prediction
                response = Response(json_response, content_type='application/json')
                return response(environ, start_response)
        ..
    * 🔥 Try your code locally by running ``python predict.py`` and then in another window run curl to get your JSON response: ``curl -X POST -F "image=@7.png" localhost:8000/``

Configure the deployment endpoint in ``valohai.yaml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* While we were developing our ``predict.py`` we installed werkzeug and Pillow using pip. We'll need to make sure these packages are available also on the Docker machine running the predictions on Valohai.
    * Create a new ``requirements.txt`` file and add the following requirements to it:
        * Pillow~=5.1.0
        * werkzeug~=0.14.0
    * Valohai will use pip to automatically install all the dependencies from ``requirements.txt`` when you create a new version of your deployment.
* Add a new endpoint in your ``valohai.yaml`` configuration. Take a note of the image, wsgi and files settings.
    * **image**: is the Docker image that should be used for this image. We're using ``tensorflow/tensorflow:2.0.1-py3`` without GPU support here.
    * **wsgi**: here we're prodiving the ``mypredictor`` function from ``predict.py``
    * **files**: we require a file to be uploaded as a part of this deployment. This will make it easy for you to publish new deployment versions with a new ``model.h5`` on Valohai, without having to go through the code.
        .. code:: yaml
            
            ---

            - step:
                name: Train MNIST model
                image: tensorflow/tensorflow:2.0.1-py3
                environment: azure-westeurope-f2sv2
                command: python train.py {parameters}
                inputs:
                    - name: my-mnist-dataset
                      default: {datum://id}
            - endpoint:
                name: digit-predict
                description: predict digits from image inputs
                image: tensorflow/tensorflow:2.0.1-py3
                environment: azure-westeurope-f2sv2
                wsgi: predict:mypredictor
                files:
                    - name: model
                      description: Model output file from TensorFlow
                      path: model.h5
        ..

* Run ``vh exec run --adhoc train`` to upload your new files to Valohai. 
* Now navigate the the *Deployment* tab of your project and create a new deployment.
* Create a version inside the deployment.
    * Enable the ``digit-predict`` endpoint
    * Choose the ``model.h5`` from your latest execution (this requirement is defined in the .yaml)
    * Create a new version and wait for the deployment to be 100% Available.
* Click the endpoint URL and you'll get a response that no image was provided.
* You can test the endpoint with an image using the **Test deployment** button on the Deployment Version page, or use ``curl`` to send a request to the URL with the image.
    * Remember to add a field ``image`` and upload an image before sending the request.
* Finally you can disable the endpoint **and** the version.

.. container:: alert alert-warning

    **Batch inference**

    If you're doing non-interactive batch predictions (taking a lot of samples as input and writing predictions into a file), you can just create an execution step to handle the predictions: take your model/samples as inputs and write your predictions to /valohai/outputs.

    Deployments are mainly required if one of the following is true:

    * You want to get fast predictions on per-sample basis
    * You want to give prediction endpoint access to application that outside of your organization e.g. a customer that doesn’t have a Valohai account

..

.. seealso:: 
    
    * `Deployments <https://docs.valohai.com/core-concepts/deployments/?highlight=deploy>`_ on Docs
    * `endpoint - from a WSGI definition <https://docs.valohai.com/valohai-yaml/endpoint/wsgi/>`_
    * `endpoint - from a command <https://docs.valohai.com/valohai-yaml/endpoint/server-command/>`_ if you'd like to use something else than WSGI.
    * `Deployment monitoring </core-concepts/deployments/#deployment-monitoring>`_
..

Congratulations! You now have trained your own model, learned to work with cloud storage, collect metadata and deploy your model for online inference! Phew! That was a lot - but you got through it.

Now is a good time to pat yourself on the back and celebrate 🎉🎉

.. seealso::

    Continue the tutorial with:

    * `Creating parameters and running Tasks for hyperoptimization </tutorials/valohai/advanced/#use-tasks-for-hyperparameter-optimization>`_
    * `Create a sequence of operations with pipelines </tutorials/valohai/advanced/#tutorial-run-multiple-steps-through-a-pipeline>`_
    * `Migrating existing Python projects to Valohai </tutorials/migrating_existing_projects>`_ 

..
