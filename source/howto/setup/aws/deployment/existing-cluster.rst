
:orphan:

.. meta::
    :description: How to allow Valohai to access your existing Kubernetes cluster


Deploying to an existing Kubernetes cluster
######################################################

Valohai can push deployments to an existing Kubernetes cluster.

Valohai uses standard Kubernetes APIs to communicate with your Kubernetes cluster and app.valohai.com (34.248.245.191) should be able to access your clusters API Server over HTTPS.

You cluster can be configured to serve only private deployment endpoints.

* Install ingress-nginx on the cluster
  
  * https://kubernetes.github.io/ingress-nginx/deploy/
* Get the external IP of your ingress-nginx. You'll need to share this with Valohai.
    ``kubectl -n ingress-nginx get service/ingress-nginx-controller``
* Create a Kubernetes service account that Valohai will use
    ``kubectl create serviceaccount valohai-deployment``
* Find the token name (one secret token should be generated automatically). You'll need to provide this token back to Valohai.
    ``kubectl get serviceaccounts valohai-deployment -o json``
    ``kubectl get secret valohai-deployment-token-<TOKEN_NAME> -o json``
* Setup the `valohai-metadata-role` in Kuberenetes. If you want to limit access to specific namespace define it below, otherwise leave it empty.
  
  * Create a new file ``valohai-deployment-role.yml`` with the following contents:
    
    .. code-block:: yaml

        kind: Role
        apiVersion: rbac.authorization.k8s.io/v1
        metadata:
            name: valohai-deployment-role
            namespace: <IF THERE IS A NAMESPACE>
        rules:
        - apiGroups: [""]
            resources: ["events", "namespaces"]
            verbs: ["get", "list", "watch"]
        - apiGroups: [""]
            resources: ["pods", "services"] 
            verbs: ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"]
        - apiGroups: ["apps", "extensions"]
            resources: ["deployments", "deployments/rollback", "deployments/scale"]
            verbs: ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"]
        - apiGroups: ["extensions"]
            resources: ["ingresses"]
            verbs: ["create", "delete", "deletecollection", "get", "list", "patch", "update", "watch"]
    
  * Apply the role with ``kubectl apply -f valohai-deployment-role.yml``
  * Create a rolebinding
    
    .. code-block:: bash

        kubectl create rolebinding valohai-deployment-binding \
            --role=valohai-deployment-role \
            --serviceaccount=<IF_NAMESPACED>:valohai-deployment \
            --namespace=<IF_NAMESPACED>


.. warning:: 

    Make sure your cluster's nodes can pull from the repository that Valohai is pushing images to.




AWS - User Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This user is required so Valohai can deploy access the cluster and deploy new images to your ECR.

- Create a user ``valohai-eks-user``.
    - enable ``Programmatic access`` and ``Console access``
- Attach the following existing policies
    - AmazonEC2ContainerRegistryFullAccess
    - AmazonEKSServicePolicy
- Click on ``Create policy`` to open a new tab. Describe the new policy with the JSON below.
    .. code-block:: json

      {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "1",
                "Effect": "Allow",
                "Action": "eks:ListClusters",
                "Resource": "*"
            }
        ]
      }
      

- Name the policy ``VH_EKS_USER`` and create it.
- Back in your ``Add user`` tab click on the refresh button and select the ``VH_EKS_USER`` policy.
- Store the access key & secret in a safe place.

GCP - Service Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``valohai-sa-deployments`` service account is used by Valohai to manage deployments and images in your GCR.

* **Type:** Service Account
* **Name:** valohai-sa-deployments
* **Role:**
    * Service Account Token Creator
    * Storage Admin
* **Create Key:** JSON

Download the JSON key, as you’ll need to share it with Valohai later.


Other
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use standard Docker login (username/password) credentials when pushing to Azure Container Registry, GitLab, Artifactory, Docker Hub, and others.

Make sure you create a seperate account for Valohai to be able to push to your repository.


Conclusion
------------

You should now have the following values:

* Cluster name
* ``valohai-deployment`` service accounts token
* External IP of ingress-nginx (``kubectl -n ingress-nginx get service/ingress-nginx-controller``)
* Cluster API address and the ``cluster-certificate-data``
  * If you have a ALB that has a well-trusted cert and points to the Kubernetes API, you'll need to just provide the ALB address

Share this information with your Valohai contact using the Vault credentials provided to you.