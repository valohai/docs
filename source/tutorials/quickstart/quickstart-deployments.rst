
.. meta::
    :description: Deploy your model for online inference

.. _quickstart-deployments:

Deploy a model for online inference
######################################

.. admonition:: Note
    :class: seealso

    This tutorial is a part of our :ref:`quickstart` series.
..

You can deploy a trained model for online inference using Valohai deployments.

.. admonition:: A short recap on online inference
    :class: tip

    * A deployment gives you an URL that you can use for online inference.
    * You can deploy either to a shared Valohai cluster, or your own private cluster.
    * Use a web framework like `FastAPI <https://fastapi.tiangolo.com/>`_ to handle the HTTP requests in your app.

..

.. admonition:: Prerequirements
    :class: attention

    * It's strongly recommended to :ref:`repository` before using deployments

..

Handle HTTP requests and return predictions
---------------------------------------------

Create a new file **predict.py** for your online inference code. This script will handle:

* Receive a HTTP POST request (on any path)
* Read an image from the POST request
* Load the trained model to memory
* Return the prediction

.. code-block:: python
    :linenos:
    :emphasize-lines: 9,14,16,26,27,32

    from fastapi import FastAPI, File, UploadFile

    import tensorflow as tf

    import numpy
    from PIL import Image
    from io import BytesIO

    app = FastAPI()

    model_path = 'model.h5'
    loaded_model = None

    @app.post("{full_path:path}")
    async def predict(image: UploadFile = File(...)):
        img = Image.open(BytesIO(await image.read()))

        # Resize image and convert to grayscale
        img = img.resize((28, 28)).convert('L')
        img_array = numpy.array(img)

        image_data = numpy.reshape(img_array, (1, 28, 28))

        global loaded_model
        # Check if model is already loaded
        if not loaded_model:
            loaded_model = tf.keras.models.load_model(model_path)

        # Predict with the model
        prediction = loaded_model.predict_classes(image_data)

        return f'Predicted_Digit: {prediction[0]}'

.. admonition:: Test the app locally
    :class: tip

    You can test the web application locally:

    * ``pip install tensorflow==2.4.1 fastapi Pillow python-multipart``
    * ``uvicorn --debug --reload predict:app``

Define a Valohai endpoint
----------------------------

Edit your ``valohai.yaml`` and add the following endpoint definition.

.. code-block:: yaml
    :linenos:

    - endpoint:
        name: digits
        description: predict digits from image inputs
        image: tiangolo/uvicorn-gunicorn-fastapi:python3.7
        server-command: uvicorn predict:app --host 0.0.0.0 --port 8000
        files:
            - name: model
              description: Model output file from TensorFlow
              path: model.h5

..

.. list-table::
   :widths: 10 90
   :stub-columns: 1

   * - ``name``
     - Name of the endpoint. This will be visible in the UI and the endpoint URL.
   * - ``image``
     - A Docker image that contains all (or most) of the packages needed to run the predict.py script
   * - ``server-command``
     - What command should Valohai run to start your webserver? You can also define the endpoint from a `WSGI definition </reference-guides/valohai-yaml/endpoint/wsgi/>`_
   * - ``files``
     - Define which files are needed to run the endpoint. The ``path`` defines where the file will be stored in your deployment. In our case, the model file will always be at ``model.h5``, regardless of what's the name of the uploaded file


You can add any packages that are not included in the Docker image to the ``requirements.txt``.

.. code-block::
    :linenos:
    :emphasize-lines: 2,3,4

    valohai-utils
    tensorflow==2.4.1
    Pillow
    python-multipart

..

Now either commit and push the changes to your code repository:

.. code-block::

    git add valohai.yaml
    git add predict.py
    git commit -m "digit prediction deployment endpoint"
    git push

..

Alternatively you can run ``vh exec run train-model --adhoc`` to send your local changes to Valohai, and skip pushing to a code repository.

Create a new deployment
----------------------------

* Login to `app.valohai.com <https://app.valohai.com>`_
* Open your project
* Click on the **Fetch repository** button to fetch a new commit, if you've connected your project to a Git-repository
* Click on your Project's **Deployment** tab
* Click on the **Create deployment** button
* Name your deployment **mydeployment** and select where the endpoint will be hosted (by default Valohai.Cloud)
* Click on **Create deployment**
* Choose the ``digits`` endpoint and select a ``model.h5`` you've trained previously.
* Click on **Create version**

.. note::

    When the status becomes ``100% - Available``, you can start using your endpoint.


.. video:: /_static/videos/create-deployment.mp4
    :autoplay:
    :width: 600


Test endpoint
-------------------------


You can test your deployment endpoints directly from the Valohai web app.

* Login to `app.valohai.com <https://app.valohai.com>`_
* Open your project
* Click on your Project's **Deployment** tab
* Select an existing deployment
* Click on the **Test deployment** button
* Select your endpoint from the drop-down
* Add a new called ``image`` and change the type to ``File``
* Choose an image from your machine (you can use the one below)
* Click on the **Send request** button

.. image:: /_images/7.png
    :alt: Test image 7

Depending on what your endpoint is expecting, you can send it either text or a file (e.g. image).

.. video:: /_static/videos/test-deployment.mp4
    :autoplay:
    :width: 600
