.. seealso::

    For the technical specifications, go to :doc:`valohai.yaml pipeline section </valohai-yaml/pipeline/index>`.

**Pipeline** is a version controlled collection of executions some of which rely on the results of the previous
executions thus creating a directed graph. These pipeline graphs consist of nodes and edges and we'll discuss
these further down.

For example, consider the following sequence of data science operations:

1. **preprocess** dataset on a memory-optimized machine
2. **train** multiple machine learning models on GPU machines using the preprocessed data
3. **evaluate** all of the trained models
4. **find-best-model** compare the models to find the best model
5. **deploy** a new version of your trained model for online inference

Our pipeline would have 4 or more **nodes**; at least one for each :doc:`step </core-concepts/steps>` mentioned above and one for the deployment.

In the example below we'll train 3 different models in parallel and compare them to find the best performing model that we can deploy to an HTTP endpoint.

.. thumbnail:: /core-concepts/pipelines.png
   :alt: You configure data stores per project-basis on Valohai.
..

You can manage pipelines under the ``Pipelines`` tab on the web user interface if the feature has been enabled for your account. Your project will need to connected to a Git repository and have a pipelines section defined in your ``valohai.yaml``.

**Nodes** of the pipeline (the circles that receive something and/or produce something):

* Nodes can be either :doc:`executions </core-concepts/executions>` or :doc:`deployments </core-concepts/deployments>`
* Each node will start automatically when all of the requirements have been met.
* Each node has a list of "edges" (explained below)

**Edges** of the pipeline (the lines between nodes) are either
    * :doc:`output </executions/outputs/index>` files used as an input of an upcoming execution or deployment.
    * parameters that are passed from one node to another.


Triggers
############

Valohai triggers allow you to launch a copy of an existing pipeline on a time-based trigger. For example, running a pipeline weekly on Mondays at 09:00.

.. container:: alert alert-warning
    
    You need to run at least one successful pipeline before you can set a Trigger to run that pipeline on a schedule.

..

**Set a new pipeline trigger** 

1. Go to project settings
2. Navigate to the Triggers-tab
3. Set your trigger title (e.g. *Weekly re-training*)
4. Select *Scheduled (Cron)* as the condition, as click *Add*
5. Open the condition and set the schedule you want. For example, Weekly on Mondays at 09:00
6. On the *Actions* column select *Copy Pipeline* and click *Add*
7. Open the action and select the *Source Pipeline* that you want to run
8. Click on *Create trigger* 

.. thumbnail:: /core-concepts/trigger.png
   :alt: You configure triggers for pipelines
..

.. container:: alert alert-success

    **Note:** You can get notifications for completed and/or failed pipelines by setting your notification preferences on the home page (`app.valohai.com`) 

..



Pipelines in YAML
###################

Full documentation how to define pipelines can be found under :doc:`valohai.yaml pipeline </valohai-yaml/pipeline/index>`
section, but here is a brief overview what the above example pipeline could look like:

.. code-block:: yaml

    # define "preprocess", "train" and "evaluate" steps and the deployment endpoint in the YAML
    # full example at https://github.com/valohai/tensorflow-example/blob/master/valohai.yaml

    - pipeline:
        name: Three-Trainings Pipeline
        nodes:
        - name: preprocess-node
            type: execution
            step: Preprocess dataset (MNIST)
        - name: train1-node
            type: execution
            step: Train model (MNIST)
            override:
            inputs:
                - name: training-set-images
                - name: training-set-labels
                - name: test-set-images
                - name: test-set-labels
        - name: train2-node
            type: execution
            step: Train model (MNIST)
            override:
            inputs:
                - name: training-set-images
                - name: training-set-labels
                - name: test-set-images
                - name: test-set-labels
        - name: train3-node
            type: execution
            step: Train model (MNIST)
            override:
            inputs:
                - name: training-set-images
                - name: training-set-labels
                - name: test-set-images
                - name: test-set-labels
        - name: evaluate1-node
            type: execution
            step: Batch inference (MNIST)
        - name: evaluate2-node
            type: execution
            step: Batch inference (MNIST)
        - name: evaluate3-node
            type: execution
            step: Batch inference (MNIST)
        - name: find-best-model-node
            type: execution
            step: Compare predictions (MNIST)
        - name: deploy-node
            type: deployment
            deployment: MyDeployment
            endpoints:
              - predict-digit
        edges:
        - [preprocess-node.output.*train-images*, train1-node.input.training-set-images]
        - [preprocess-node.output.*train-labels*, train1-node.input.training-set-labels]
        - [preprocess-node.output.*test-images*, train1-node.input.test-set-images]
        - [preprocess-node.output.*test-labels*, train1-node.input.test-set-labels]
        - [preprocess-node.output.*train-images*, train2-node.input.training-set-images]
        - [preprocess-node.output.*train-labels*, train2-node.input.training-set-labels]
        - [preprocess-node.output.*test-images*, train2-node.input.test-set-images]
        - [preprocess-node.output.*test-labels*, train2-node.input.test-set-labels]
        - [preprocess-node.output.*train-images*, train3-node.input.training-set-images]
        - [preprocess-node.output.*train-labels*, train3-node.input.training-set-labels]
        - [preprocess-node.output.*test-images*, train3-node.input.test-set-images]
        - [preprocess-node.output.*test-labels*, train3-node.input.test-set-labels]
        - [train1-node.output.model*, evaluate1-node.input.model]
        - [train2-node.output.model*, evaluate2-node.input.model]
        - [train3-node.output.model*, evaluate3-node.input.model]
        - [evaluate1-node.output.*.json, find-best-model-node.input.predictions]
        - [evaluate2-node.output.*.json, find-best-model-node.input.predictions]
        - [evaluate3-node.output.*.json, find-best-model-node.input.predictions]
        - [evaluate1-node.output.model*, find-best-model-node.input.models]
        - [evaluate2-node.output.model*, find-best-model-node.input.models]
        - [evaluate3-node.output.model*, find-best-model-node.input.models]
        - [find-best-model-node.output.model*, deploy-node.file.predict-digit.model]
        - [find-best-model-node.parameter.my_param, find-best-model-node.parameter.my_param]
    
..

In the above example we have **several execution nodes** (i.e. preprocess, train, evaluate, find-best-model) and one **deployment node**.

The edges definitions define how data flows between different nodes. For example: ``[preprocess-node.output.*x-images*, train.input.x-images]`` equals to

* Complete the **preprocess-node**
* Search the outputs of **preprocess-node** for all files that match ``*x-images*`` (e.g. dataset-x-images-2020.tar.gz)
* Use those files as the input called ``x-images`` for the train node. This input "slot" is defined in the step definition of ``train``.

Valohai will automatically store the files from **preprocess-node** in your cloud storage and provide them as inputs for the **train-node**

You can find the full `valohai.yaml` sample in our `GitHub repo for the TensorFlow example <https://github.com/valohai/tensorflow-example/blob/master/valohai.yaml>`_.

Create a pipeline through an API call
######################################

You can also launch a pipeline using the Valohai APIs, without the need of going to the web app. The API works independently of the `valohai.yaml` definition.

Below an example of the API call based on our sample above. 

.. code:: python
    
    import requests

    resp = requests.request(
        url="https://app.valohai.com/api/v0/pipelines/",
        method="POST",
        headers={"Authorization": "<your-token>"},
        json={
            "edges": [
                {
                    "source_node": "preprocess-node",
                    "source_key": "*train-images*",
                    "source_type": "output",
                    "target_node": "train1-node",
                    "target_type": "input",
                    "target_key": "training-set-images"
                },
                {
                    "source_node": "preprocess-node",
                    "source_key": "*train-labels*",
                    "source_type": "output",
                    "target_node": "train1-node",
                    "target_type": "input",
                    "target_key": "training-set-labels"
                },
                {
                    "source_node": "preprocess-node",
                    "source_key": "*test-images*",
                    "source_type": "output",
                    "target_node": "train1-node",
                    "target_type": "input",
                    "target_key": "test-set-images"
                },
                {
                    "source_node": "preprocess-node",
                    "source_key": "*test-labels*",
                    "source_type": "output",
                    "target_node": "train1-node",
                    "target_type": "input",
                    "target_key": "test-set-labels"
                },
                {
                    "source_node": "preprocess-node",
                    "source_key": "*train-images*",
                    "source_type": "output",
                    "target_node": "train2-node",
                    "target_type": "input",
                    "target_key": "training-set-images"
                },
                {
                    "source_node": "preprocess-node",
                    "source_key": "*train-labels*",
                    "source_type": "output",
                    "target_node": "train2-node",
                    "target_type": "input",
                    "target_key": "training-set-labels"
                },
                {
                    "source_node": "preprocess-node",
                    "source_key": "*test-images*",
                    "source_type": "output",
                    "target_node": "train2-node",
                    "target_type": "input",
                    "target_key": "test-set-images"
                },
                {
                    "source_node": "preprocess-node",
                    "source_key": "*test-labels*",
                    "source_type": "output",
                    "target_node": "train2-node",
                    "target_type": "input",
                    "target_key": "test-set-labels"
                },
                {
                    "source_node": "preprocess-node",
                    "source_key": "*train-images*",
                    "source_type": "output",
                    "target_node": "train3-node",
                    "target_type": "input",
                    "target_key": "training-set-images"
                },
                {
                    "source_node": "preprocess-node",
                    "source_key": "*train-labels*",
                    "source_type": "output",
                    "target_node": "train3-node",
                    "target_type": "input",
                    "target_key": "training-set-labels"
                },
                {
                    "source_node": "preprocess-node",
                    "source_key": "*test-images*",
                    "source_type": "output",
                    "target_node": "train3-node",
                    "target_type": "input",
                    "target_key": "test-set-images"
                },
                {
                    "source_node": "preprocess-node",
                    "source_key": "*test-labels*",
                    "source_type": "output",
                    "target_node": "train3-node",
                    "target_type": "input",
                    "target_key": "test-set-labels"
                },
                {
                    "source_node": "train1-node",
                    "source_key": "model*",
                    "source_type": "output",
                    "target_node": "evaluate1-node",
                    "target_type": "input",
                    "target_key": "model"
                },
                {
                    "source_node": "train2-node",
                    "source_key": "model*",
                    "source_type": "output",
                    "target_node": "evaluate2-node",
                    "target_type": "input",
                    "target_key": "model"
                },
                {
                    "source_node": "train3-node",
                    "source_key": "model*",
                    "source_type": "output",
                    "target_node": "evaluate3-node",
                    "target_type": "input",
                    "target_key": "model"
                },
                {
                    "source_node": "evaluate1-node",
                    "source_key": "*.json",
                    "source_type": "output",
                    "target_node": "find-best-model-node",
                    "target_type": "input",
                    "target_key": "predictions"
                },
                {
                    "source_node": "evaluate2-node",
                    "source_key": "*.json",
                    "source_type": "output",
                    "target_node": "find-best-model-node",
                    "target_type": "input",
                    "target_key": "predictions"
                },
                {
                    "source_node": "evaluate3-node",
                    "source_key": "*.json",
                    "source_type": "output",
                    "target_node": "find-best-model-node",
                    "target_type": "input",
                    "target_key": "predictions"
                },
                {
                    "source_node": "evaluate1-node",
                    "source_key": "model*",
                    "source_type": "output",
                    "target_node": "find-best-model-node",
                    "target_type": "input",
                    "target_key": "models"
                },
                {
                    "source_node": "evaluate2-node",
                    "source_key": "model*",
                    "source_type": "output",
                    "target_node": "find-best-model-node",
                    "target_type": "input",
                    "target_key": "models"
                },
                {
                    "source_node": "evaluate3-node",
                    "source_key": "model*",
                    "source_type": "output",
                    "target_node": "find-best-model-node",
                    "target_type": "input",
                    "target_key": "models"
                },
                {
                    "source_node": "find-best-model-node",
                    "source_key": "model.pb",
                    "source_type": "output",
                    "target_node": "deploy-node",
                    "target_type": "file",
                    "target_key": "predict-digit.model"
                }
            ],
            "nodes": [
                {
                    "name": "preprocess-node",
                    "type": "execution",
                    "template": {
                        "commit": "8d5678c1624837a353648e4ba51e3d44feb59f67",
                        "step": "Preprocess dataset (MNIST)",
                        "inputs": {
                            "training-set-images": [
                                "https://valohaidemo.blob.core.windows.net/mnist/train-images-idx3-ubyte.gz"
                            ],
                            "training-set-labels": [
                                "https://valohaidemo.blob.core.windows.net/mnist/train-labels-idx1-ubyte.gz"
                            ],
                            "test-set-images": [
                                "https://valohaidemo.blob.core.windows.net/mnist/t10k-images-idx3-ubyte.gz"
                            ],
                            "test-set-labels": [
                                "https://valohaidemo.blob.core.windows.net/mnist/t10k-labels-idx1-ubyte.gz"
                            ]
                        },
                        "parameters": {},
                        "inherit_environment_variables": True,
                        "time_limit": 0,
                        "environment_variables": {}
                    }
                },
                {
                    "name": "train1-node",
                    "type": "execution",
                    "template": {
                        "commit": "8d5678c1624837a353648e4ba51e3d44feb59f67",
                        "step": "Train model (MNIST)",
                        "inputs": {
                            "training-set-images": [],
                            "training-set-labels": [],
                            "test-set-images": [],
                            "test-set-labels": []
                        },
                        "parameters": {
                            "max_steps": 300,
                            "learning_rate": 0.001,
                            "dropout": 0.9,
                            "batch_size": 200
                        },
                        "inherit_environment_variables": True,
                        "time_limit": 0,
                        "environment_variables": {}
                    }
                },
                {
                    "name": "train2-node",
                    "type": "execution",
                    "template": {
                        "commit": "8d5678c1624837a353648e4ba51e3d44feb59f67",
                        "step": "Train model (MNIST)",
                        "inputs": {
                            "training-set-images": [],
                            "training-set-labels": [],
                            "test-set-images": [],
                            "test-set-labels": []
                        },
                        "parameters": {
                            "max_steps": 300,
                            "learning_rate": 0.001,
                            "dropout": 0.9,
                            "batch_size": 200
                        }
                    }
                },
                {
                    "name": "train3-node",
                    "type": "execution",
                    "template": {
                        "commit": "8d5678c1624837a353648e4ba51e3d44feb59f67",
                        "step": "Train model (MNIST)",
                        "inputs": {
                            "training-set-images": [],
                            "training-set-labels": [],
                            "test-set-images": [],
                            "test-set-labels": []
                        },
                        "parameters": {
                            "max_steps": 300,
                            "learning_rate": 0.001,
                            "dropout": 0.9,
                            "batch_size": 200
                        }
                    }
                },
                {
                    "name": "evaluate1-node",
                    "type": "execution",
                    "template": {
                        "commit": "8d5678c1624837a353648e4ba51e3d44feb59f67",
                        "step": "Batch inference (MNIST)",
                        "inputs": {
                            "model": [],
                            "images": [
                                "https://valohaidemo.blob.core.windows.net/mnist/four-inverted.png",
                                "https://valohaidemo.blob.core.windows.net/mnist/five-inverted.png",
                                "https://valohaidemo.blob.core.windows.net/mnist/five-normal.jpg"
                            ]
                        },
                        "parameters": {
                            "output-best-model": True,
                            "model-dir": "/valohai/inputs/model/",
                            "image-dir": "/valohai/inputs/images/"
                        }
                    }
                },
                {
                    "name": "evaluate2-node",
                    "type": "execution",
                    "template": {
                        "commit": "8d5678c1624837a353648e4ba51e3d44feb59f67",
                        "step": "Batch inference (MNIST)",
                        "inputs": {
                            "model": [],
                            "images": [
                                "https://valohaidemo.blob.core.windows.net/mnist/four-inverted.png",
                                "https://valohaidemo.blob.core.windows.net/mnist/five-inverted.png",
                                "https://valohaidemo.blob.core.windows.net/mnist/five-normal.jpg"
                            ]
                        },
                        "parameters": {
                            "output-best-model": True,
                            "model-dir": "/valohai/inputs/model/",
                            "image-dir": "/valohai/inputs/images/"
                        }
                    }
                },
                {
                    "name": "evaluate3-node",
                    "type": "execution",
                    "template": {
                        "commit": "8d5678c1624837a353648e4ba51e3d44feb59f67",
                        "step": "Batch inference (MNIST)",
                        "inputs": {
                            "model": [],
                            "images": [
                                "https://valohaidemo.blob.core.windows.net/mnist/four-inverted.png",
                                "https://valohaidemo.blob.core.windows.net/mnist/five-inverted.png",
                                "https://valohaidemo.blob.core.windows.net/mnist/five-normal.jpg"
                            ]
                        },
                        "parameters": {
                            "output-best-model": True,
                            "model-dir": "/valohai/inputs/model/",
                            "image-dir": "/valohai/inputs/images/"
                        }
                    }
                },
                {
                    "name": "find-best-model-node",
                    "type": "execution",
                    "template": {
                        "commit": "8d5678c1624837a353648e4ba51e3d44feb59f67",
                        "step": "Compare predictions (MNIST)",
                        "inputs": {
                            "predictions": [],
                            "models": []
                        },
                        "parameters": {
                            "prediction-dir": "/valohai/inputs/predictions/"
                        }
                    }
                },
                {
                    "name": "deploy-node",
                    "type": "deployment",
                    "deployment": "01756f96-4144-265a-611d-cf306e1768ff",
                    "endpoint_configurations": {
                        "predict-digit": {
                            "enabled": True
                        }
                    },
                    "commit": "8d5678c1624837a353648e4ba51e3d44feb59f67"
                }
            ],
            "project": "01756e9b-522c-16b3-5429-2b1920e67e14",
            "title": "Three-Trainings Pipeline"
        },
    )
    if resp.status_code == 400:
        raise RuntimeError(resp.json())
    resp.raise_for_status()
    data = resp.json()

..

.. seealso::

    * `API: DeploymentCreate <https://app.valohai.com/api/docs/#operation/DeploymentCreate>`_
    * `API: DeploymentVersionCreate <https://app.valohai.com/api/docs/#operation/DeploymentVersionCreate>`_
..