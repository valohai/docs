:orphan:

.. meta::
    :description: How to set up your EKS cluster for Valohai deployments


Deployment Cluster on AWS
######################################################

Install the tools
-----------------------------

* `AWS CLI & EKS CLI <https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html>`_
* `Kubectl <https://kubernetes.io/docs/tasks/tools/install-kubectl/>`_
* `Helm v3 <https://helm.sh/docs/intro/install/>`_
* `AWS IAM authenticator (for kubectl) <https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html>`_


Provision an Amazon EKS (Elastic Kubernetes Service)
---------------------------------------------------------

IAM: Admin user (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This user is needed only if you want to give Valohai elevated permissions to install an EKS cluster in your subscription.

You can skip this IAM user if you're creating the cluster yourself.

- Create a user ``valohai-eks-admin``.
    - enable ``Programmatic access`` and ``Console access``
- Attach the following existing policies
    - AmazonEKSClusterPolicy
    - AmazonEC2FullAccess
    - AmazonVPCFullAccess
    - AmazonEC2ContainerRegistryPowerUser
    - AmazonEKSServicePolicy
- Click on ``Create policy`` to open a new tab. Describe the new policy with the JSON below.
    .. code-block:: json
  
      {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "1",
                "Effect": "Allow",
                "Action": [
                    "iam:GetRole",
                    "iam:ListRoleTags",
                    "iam:CreateRole",
                    "iam:DeleteRole",
                    "iam:AttachRolePolicy",
                    "iam:PutRolePolicy",
                    "iam:PassRole",
                    "iam:DetachRolePolicy",
                    "iam:CreateServiceLinkedRole",
                    "iam:GetRolePolicy",
                    "eks:*",
                    "cloudformation:*"
                ],
                "Resource": "*"
            },
            {
                "Sid": "2",
                "Effect": "Allow",
                "Action": "ecr:*",
                "Resource": "arn:aws:ecr:*:*:repository/*"
            }
        ]
      }
      
    
- Name the policy ``VH_EKS_ADMIN`` and create it.
- Back in your ``Add user`` tab click on the refresh button and select the ``VH_EKS_ADMIN`` policy.
- Store the access key & secret in a safe location.

IAM: EKS User (required)
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


Create the EKS cluster
------------------------

.. admonition:: info

    Follow the instructions below to create a new EKS cluster with our default settings.
    
    You can also skip this section and use an existing cluster - or define different settings.

We'll use `eksctl <https://eksctl.io/>`_ , a simple CLI tool to create the cluster on EKS.

Start by logging in to the AWS CLI ``aws configure --profile valohai-eks-admin`` and by passing in the right keys.

Then set the current profile with ``export AWS_PROFILE=valohai-eks-admin``

Start the cluster creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below a sample command to start a new cluster creation with max four ``t3.medium`` nodes and with a dedicated VPC.

Create a couple of env variables to make life easier:

.. code-block:: bash

    export CLUSTER=<customer-name>-valohai
    export REGION=<aws-region>


Then create the cluster:

.. code-block:: bash

    eksctl create cluster \
    --name $CLUSTER \
    --region $REGION \
    --nodegroup-name standard-workers \
    --node-type t3.medium \
    --nodes 1 \
    --nodes-min 1 \
    --nodes-max 4 \
    --managed \
    --write-kubeconfig=0


This takes 10-15 minutes to go up.

Logs are available under CloudFormation on console or with CLI:

* ``aws cloudformation describe-stack-events --stack-name eksctl-$CLUSTER-cluster``
* ``aws cloudformation describe-stack-events --stack-name eksctl-$CLUSTER-nodegroup-standard-workers``

Setup kubeconfig
--------------------

We're defining a custom location for the config file (with `--kubeconfig`) to ensure we're writing to an empty file
instead of modifying to the default config.

.. code-block:: bash

    aws eks --region $REGION update-kubeconfig --name $CLUSTER --kubeconfig ~/.kube/$CLUSTER

    # now you can either give '--kubeconfig ~/.kube/$CLUSTER' to 'kubectl' commands
    # or define `KUBECONFIG` for the session like below:
    export KUBECONFIG=~/.kube/$CLUSTER


Check that the cluster is up and running:

.. code-block:: bash

    kubectl get svc --kubeconfig ~/.kube/$CLUSTER


Install NGINX Ingress Controller (required)
----------------------------------------------

.. code-block:: bash

    kubectl create namespace ingress-nginx

    helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
    helm repo update
    helm install \
    ingress-nginx \
    ingress-nginx/ingress-nginx \
    --version v3.31.0 \
    --namespace ingress-nginx
    
    # there is also a lot of configuration you can do here but defaults should be fine:
    # helm show values ingress-nginx/ingress-nginx


Make sure ``ingress-nginx-controller`` pod is running, might take a minute:

.. code-block:: bash

    kubectl get pods --all-namespaces --kubeconfig ~/.kube/$CLUSTER
    # NAMESPACE       NAME                                        READY   STATUS    RESTARTS   AGE
    # ingress-nginx   nginx-ingress-controller-6885bc7778-rckm6   1/1     Running   0          2m15s


See that the ``ingress-nginx`` is running and get the external address:

.. code-block:: bash

    kubectl -n ingress-nginx get service/ingress-nginx-controller --kubeconfig ~/.kube/$CLUSTER
    # The external IP is something on the lines of `XXX.YYY.elb.amazonaws.com`


Now we should get a default NGINX 404 from the load balancer external IP:

.. code-block:: bash

    curl http://XXX.YYY.elb.amazonaws.com


Setup the RBAC user on Kubernetes (required)
--------------------------------------------------

Create the files below to enable the `valohai-eks-user` to deploy from Valohai to your cluster.

Create a Kubernetes user and map it to the IAM user:

.. code-block:: bash

    cat <<EOF > aws-auth-patch.yaml
    data:
    mapUsers: |
        - userarn: arn:aws:iam::<ACCOUNT-ID>:user/valohai-eks-user
        username: valohai-eks-user
    EOF
    vim aws-auth-patch.yaml
    kubectl -n kube-system patch configmap/aws-auth --patch "$(cat aws-auth-patch.yaml)" --kubeconfig ~/.kube/$CLUSTER
    # you can check what it looks like with:
    # kubectl -n kube-system get configmap/aws-auth -o yaml --kubeconfig ~/.kube/$CLUSTER


Create a ``namespace-reader`` role that will give ``valohai-eks-user`` permissions on the cluster:

.. code-block:: bash

    cat <<EOF > rbacuser-clusterrole.yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
    name: namespace-reader
    rules:
    - apiGroups: [ "" ]
        resources: [ "namespaces", "services" ]
        verbs: [ "get", "watch", "list", "create", "update", "patch", "delete" ]
    - apiGroups: [ "" ]
        resources: [ "pods", "pods/log", "events" ]
        verbs: [ "list","get","watch" ]
    - apiGroups: [ "extensions","apps" ]
        resources: [ "deployments", "ingresses" ]
        verbs: [ "get", "list", "watch", "create", "update", "patch", "delete" ]
    - apiGroups: [ "networking.k8s.io" ]
        resources: [ "ingresses" ]
        verbs: [ "get", "list", "watch", "create", "update", "patch", "delete" ]
    EOF
    kubectl apply -f rbacuser-clusterrole.yaml --kubeconfig ~/.kube/$CLUSTER
    # and verify changes with...
    # kubectl get clusterrole/namespace-reader -o yaml --kubeconfig ~/.kube/$CLUSTER


Bind our cluster role and user together:

.. code-block:: bash

    cat <<EOF > rbacuser-clusterrole-binding.yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
    name: namespace-reader-global
    subjects:
    - kind: User
        name: valohai-eks-user
        apiGroup: rbac.authorization.k8s.io
    roleRef:
    kind: ClusterRole
    name: namespace-reader
    apiGroup: rbac.authorization.k8s.io
    EOF
    kubectl apply -f rbacuser-clusterrole-binding.yaml --kubeconfig ~/.kube/$CLUSTER
    # and verify changes with...
    # kubectl get clusterrolebinding/namespace-reader-global -o yaml --kubeconfig ~/.kube/$CLUSTER


Send details to Valohai
--------------------------

Send Valohai engineers:

* `valohai-eks-user` access key ID and secret.
* AWS region of the cluster
* Details of the created cluster - Find these on the cluster's page on EKS
    * Cluster name
    * API server endpoint
    * Cluster ARN
    * Certificate authority
* ECR name - Copy the URL you see when creating a new repository in your ECR (for example
  accountid.dkr.ecr.eu-west-1.amazonaws.com)
* External IP of the ingress-nginx
    * Run ``kubectl -n ingress-nginx get service/ingress-nginx-controller`` to see the IP
