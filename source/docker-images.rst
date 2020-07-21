.. meta::
    :description: Find the most common Docker images currently used in machine learning projects on the platform. It is possible to run any kind of code from C to Python as long as it runs inside a Docker container.

Docker Images
********************

Valohai utilizes Docker images to define your runtime environment.
This means that the platform is capable of running any code from C to Python
as long as it can run inside a Docker container.

You can use any Docker image available online.
After getting initial versions working, it makes sense to package your dependencies by
:doc:`building your own images </tutorials/build-docker-image/index>`.

We recommend hosting your images on `Docker Hub <https://hub.docker.com/>`_ but you can use any Docker registry.
You can configure authenticated access under organization settings.

.. include:: /_partials/_image-list.rst

Which images to use depend on your specific use-case, but it usually makes sense to:

* start with as minimal image as possible
* use a specific image tag (the ``:<VERSION>`` part) so everything stays reproducible

Access Private Docker Repositories
****************************************

Organizations can use private repositories from Docker Hub, AWS, GCP or Azure for Valohai executions.

1. Create an access token or credentials, so Valohai workers can authenticate to your container registry (details below)
2. Login at `<https://app.valohai.com>`_
3. Navigate to ``Hi, <name> (the top right menu) > Manage <organization>``. 
4. Go to *Registries* under the organization controls
5. Add a new entry
6. Insert the name in the format of *docker.io/myusername/**
7. Choose your registry type and provide the right access credentials
8. Use the full name of the container (e.g. ``docker.io/myusername/name:tag``) when defining the image in your ``valohai.yaml``

Private container registries can be used only in organization projects.

Create registry credentials for Valohai
=============================================
 
* Docker Hub: `Create an access token <https://docs.docker.com/docker-hub/access-tokens/>`_
* Azure Container Registry: `Authenticate with a service principal <https://docs.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal>`_

Google Cloud Container Registry
------------------------------------

1. Create a new service account under your Google Cloud project.
2. Add "Service Account Token Creator" role so it can create temporary tokens for itself.
3. Allow the service account to access the registry:
    * Go to https://console.cloud.google.com/storage/browser
    * Click on the bucket <OPTIONAL_REGION>.artifacts.<PROJECT_ID>.appspot.com
    * Click "Permissions"
    * Click "Add members"
    * Search for the Service Account using the full ID (the one that looks like an email)
    * Add role "Storage Object Viewer" if pulling or "Storage Admin" if pulling and pushing
    * Click "Save" 
4. Download the Service Account JSON to use in Valohai.

AWS Elastic Container Registry
------------------------------------

1. Create a new User with *Programmatic access*
2. Create a new policy `valohai-ecr-policy` with the below JSON
    * Note: You'll need to replace the placeholders with the right region, account ID and registry.

    .. code:: json

        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "0",
                    "Effect": "Allow",
                    "Action": [
                        "ecr:DescribeImageScanFindings",
                        "ecr:GetLifecyclePolicyPreview",
                        "ecr:GetDownloadUrlForLayer",
                        "ecr:BatchGetImage",
                        "ecr:DescribeImages",
                        "ecr:DescribeRepositories",
                        "ecr:ListTagsForResource",
                        "ecr:ListImages",
                        "ecr:BatchCheckLayerAvailability",
                        "ecr:GetRepositoryPolicy",
                        "ecr:GetLifecyclePolicy"
                    ],
                    "Resource": "arn:aws:ecr:<REGION>:<ACCOUNT_ID>:repository/<REPOSITORY>"
                },
                {
                    "Sid": "1",
                    "Effect": "Allow",
                    "Action": "ecr:GetAuthorizationToken",
                    "Resource": "*"
                }
            ]
        }


    ..
3. Attach the new policy to the user and create the user.
4. Make note of the IAM access key and secret to use in Valohai.