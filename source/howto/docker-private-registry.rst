.. meta::
    :description: Authenticating with private docker registries

.. _docker-private-registries:

Access a private Docker repository
####################################

Organizations can use private repositories from Docker Hub, AWS, GCP or Azure for Valohai executions.

.. admonition:: Prerequirements
    :class: attention

    This functionality is available only to projects that are owned by an organization or team. Personal projects don't have access to private repositories.


Create registry credentials for Valohai
------------------------------------------------


.. tab:: Docker Hub
    
    
    1. Log in to hub.docker.com.
    2. Click on your username in the top right corner and select **Account Settings**.
    3. Select **Security > New Access Token**.
    4. Add a description for your token. For example "Valohai access token".
    5. Copy the token that appears on the screen. Make sure you do this now: once you close this prompt, Docker will never show the token again.


    Read more at `Docker Hub: access tokens <https://docs.docker.com/docker-hub/access-tokens/>`_

.. tab:: Azure

    Create and use `service principal credentials <https://docs.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal>`_

.. tab:: GCP

    Container Registry uses Cloud Storage buckets as their storage for your images.
    You control access to your images by granting appropriate Cloud Storage permissions to identities.

    1. Create a new service account under your Google Cloud project that contains the registry
    2. Add ``Service Account Token Creator`` role so it can create temporary tokens for itself
    3. Allow the service account to access the registry:
        * Go to https://console.cloud.google.com/storage/browser (Cloud Storage listing)
        * Find and click the bucket that hosts your Container Registry images, it's in format ``<OPTIONAL_REGION>.artifacts.<PROJECT_ID>.appspot.com``
        * Click *Permissions*
        * Click *Add members*
        * Search for the service account using the full ID (the one that looks like an email)
        * Add role ``Storage Object Viewer`` if pulling or ``Storage Admin`` if pulling and pushing
        * Click *Save*
    4. Download the service account JSON to use in Valohai

.. tab:: AWS

    1. Login to your AWS Management Console
    2. Create a new User with *Programmatic access*
    3. Create a new policy `valohai-ecr-policy` with the below JSON
        * **Note:** Replace the placeholders with the right region, account ID and registry name.

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
    4. Attach the new policy to the user and create the user.
    5. Make note of the IAM access key and secret to use in Valohai

Add credentials to Valohai
------------------------------------

* Login at `<https://app.valohai.com>`_
* Navigate to ``Hi, <name> (the top right menu) > Manage <organization>``
* Go to *Registries* under the organization controls
* Add a new entry
* Insert the match pattern in the format of ``<domain>/<owner-and-or-repository>/*`` e.g.
    * ``docker.io/myusername/*``
    * ``my-account-id.dkr.ecr.my-region.amazonaws.com/*``
    * ``gcr.io/my-project/*``
    * ``gcr.io/my-project/my-registry:*``
    * The exact form largely depends on your registry provider. Find how they report image names to learn the format.
* Choose your registry type and provide the access credentials generated in the first step
* Use the full name of the tagged container (e.g. ``docker.io/myusername/name:tag``) when defining the image in your ``valohai.yaml``

