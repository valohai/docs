.. meta::
    :description: A list of the most common images for notebook executions in Valohai


Popular Docker images for notebook executions
################################################

.. admonition:: A short recap on Docker images
    :class: tip

    * Each Valohai execution is ran inside a Docker container
    * Your Docker image should contain most, if not all, of the packages and libraries needed to run your code (e.g. specific TensorFlow version, matplotlib, xgboost or something else).
    * You can use public or private Docker images
    * All Valohai notebook executions are based on a custom image called ``valohai/pypermill``.
    * You can `build your own Docker images </tutorials/docker-build-image/>`_  on top of ``valohai/pypermill`` to include additional packages.

..

Below you'll find list of the most commonly used Notebook images and their Dockerfiles. You can use any of these images in your executions, or build your own image on top of them.

Each of the images contains the library marked in the tag and the following libraries: ``seaborn``, ``numpy``, ``pandas``, ``matplotlib``, ``valohai-utils``, and ``statsmodels``.

The Tensorflow images have a GPU enabled version. You'll recognize them by the ``-gpu`` extension.

* ``valohai/notebook:tensorflow-2.5.0`` | ``valohai/notebook:tensorflow-2.5.0-gpu``
* ``valohai/notebook:tensorflow-1.15.5`` | ``valohai/notebook:tensorflow-1.15.5-gpu``
* ``valohai/notebook:sklearn-0.24.2``
* ``valohai/notebook:sklearn-1.0``
* ``valohai/notebook:xgboost-1.4.2``

You can change the default Docker image for your Notebook by clicking on ``Settings`` inside your notebook.

.. image:: /_images/notebook-settings.png
    :alt: Change the default Docker image for your notebook


Dockerfile
--------------

Below you'll find the ``Dockerfile`` used to publish each of those images. You can `build your own Docker images </tutorials/docker-build-image/>`_ in a similar manner.

.. tab:: Tensorflow 2.5.0

    **Name:** ``valohai/notebook:tensorflow-2.5.0``

    **Dockerfile:** 

    .. code-block:: Dockerfile

        FROM valohai/pypermill

        RUN pip install --upgrade pip
        RUN pip install seaborn numpy pandas matplotlib valohai-utils statsmodels
        RUN pip install tensorflow==2.5.0

    ..

.. tab:: Tensorflow 1.15.5

    **Name:** ``valohai/notebook:tensorflow-1.15.5``

    **Dockerfile:** 

    .. code-block:: Dockerfile

        FROM valohai/pypermill

        RUN pip install --upgrade pip
        RUN pip install seaborn numpy pandas matplotlib valohai-utils statsmodels
        RUN pip install tensorflow==1.15.5
    

    ..

.. tab:: scikit-learn 0.24.2

    **Name:** ``valohai/notebook:sklearn-0.24.2``
    
    **Dockerfile:**

    .. code-block:: Dockerfile

        FROM valohai/pypermill

        RUN pip install --upgrade pip
        RUN pip install seaborn numpy pandas matplotlib valohai-utils statsmodels
        RUN pip install scikit-learn==0.24.2

    ..

.. tab:: xgboost 1.4.2

    **Name:** ``valohai/notebook:xgboost-1.4.2``
    
    **Dockerfile:**

    .. code-block:: Dockerfile

        FROM valohai/pypermill

        RUN apt-get update && apt-get -y install cmake
        
        RUN pip install --upgrade pip
        RUN pip install seaborn numpy pandas matplotlib valohai-utils statsmodels
        RUN pip install xgboost==1.4.2

    ..
    

Install additional packages during a notebook execution
------------------------------------------------------------------------------------------------------

You can also install additional package at the beginning of your Valohai execution.

#. Add a new cell at the top of your notebook
#. Add ``!pip install mylibrary mylibrary2 mylibrary3`` to the new cell to install 3 new packages during the execution

These packages will be installed every time you run the notebook on Valohai. You'll have to wait for them to download and install at the beginning of each execution.

Using a custom Docker image allows you to have these packages preinstalled in the Docker image you're using and avoid having to download them inside each execution.

