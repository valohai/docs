.. meta::
    :description: How to expose the Kubernetes ingress resource endpoints over HTTPS

.. _setup-eks-https:

Setting up HTTPS on a deployment cluster
######################################################

The goal of the document is to have:

1. A domain DNS A record pointing to the external address of the NGINX Ingress Controller, usually type "External Load Balancer".
    * e.g. valohai.cloud A 35.195.209.140 where the IP is the external IP of ngx-ingress-nginx-ingress-controller
    * then, you would use the https://valohai.cloud/... addresses to point to upcoming Valohai Deployment Endpoints
2. A Kubernetes secret object containing the TLS key in files like tls.crt and tls.key.
    * These will be used by our services to sign the HTTPS connections.

Where the DNS Record (1) exists depends on the setup but usually cloud provider DNS service like AWS Route53, Google CloudDNS or AzureDNS.

What the external IP looks like also depends on the cloud, for example it's something like XXX.YYY.elb.amazonaws.com on AWS EKS or just a simple numeric IP address.

Set up AWS Route53
--------------------------

* Navigate to "AWS Route53 > Hosted Zones > Select the Domain > Create Record"
* Enter record name prefix e.g. valohai-deployment.company.com or leave empty to use the root
* Set record type to A
* For value, select "Alias", "Alias to Application and Classic Load Balancer", and the specific load balancer attached to the cluster
    * Load balancer identifier is something like dualstack.XXX.YYY.elb.amazonaws.com.
* Click "Create Records"

When the cluster and the DNS controls are not under the same cloud account; you might have to piece together the external IP by yourself as the auto-complete isn't helping. It should be in the format dualstack.XXX.YYY.elb.amazonaws.com. where the XXX.YYY.elb.amazonaws.com suffix can be found under "AWS EC2 > Load Balancers > Details > DNS Name".

You can read more about routing to AWS ELB from `the related AWS Documentation <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.html>`_ .

You can verify that this works with:

.. code-block:: bash

    curl http://valohai-deployment.company.com

..

Configure the certificate on the cluster
--------------------------------------------------

Setup kubeconfig by defining a custom location for the config file (with --kubeconfig) to ensure we're writing to an empty file instead of modifying to the default config.

.. code-block:: bash

    aws eks --region $REGION update-kubeconfig --name <cluster-name> --kubeconfig ~/.kube/<cluster-name>

    export KUBECONFIG=~/.kube/$CLUSTER

..

After a domain points to the cluster, we set up the certificate rotation with cert-manager:

.. code-block:: bash

    # make sure you target the right cluster
    kubectl cluster-info

    kubectl create namespace cert-manager

    # install Helm https://helm.sh/docs/intro/install/
    helm repo add jetstack https://charts.jetstack.io
    helm repo update
    helm install \
        cert-manager \
        jetstack/cert-manager \
        --namespace cert-manager \
        --version v1.3.1 \
        --set installCRDs=true

..

You can verify that this worked with:

.. code-block:: bash

    kubectl -n cert-manager get pods 
    # cert-manager-* pods should be transitioning to 1/1 Running

..

Configure Let's Encrypt to update credentials:

.. code-block:: bash

    cat > letsencrypt-prod.yaml <<EOF
    apiVersion: cert-manager.io/v1
    kind: ClusterIssuer
    metadata:
        name: letsencrypt-prod
    spec:
        acme:
            server: https://acme-v02.api.letsencrypt.org/directory
            email: <CUSTOMER_CLOUD_ADMIN_EMAIL_HERE>
            privateKeySecretRef:
                name: letsencrypt-prod-acme-account-key
            solvers:
            - http01:
                ingress:
                    class: nginx
    EOF
    vim letsencrypt-prod.yaml
    kubectl apply -f letsencrypt-prod.yaml

..

You can verify that everything looks promising with:

.. code-block:: bash

    kubectl describe clusterissuer/letsencrypt-prod
    # Status message should be on the lines of:
    #    The ACME account was registered with the ACME server

..

Finally, create a certificate that we'll use:

.. code-block:: bash

    cat > master-cert.yaml <<EOF
    apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
        name: master-cert
        namespace: default
    spec:
        secretName: master-cert
        dnsNames:
        - <your-dns-name>
        issuerRef:
            name: letsencrypt-prod
            kind: ClusterIssuer
    EOF
    vim master-cert.yaml
    kubectl apply -f master-cert.yaml
    # kubectl -n default delete certificate/master-cert

..

To verify that the certificate gets created:

.. code-block:: bash

    kubectl -n default describe certificate/master-cert
    # Should transition to "The certificate has been successfully issued"

    # If it takes more than 5 minutes, begin checking `cert-manager` logs what might be wrong...
    #kubectl -n cert-manager get pods
    #kubectl -n cert-manager logs cert-manager-595474fb56-2ftn2

    # And now we have TLS keys we can use...
    kubectl -n default describe secrets/master-cert
    #Data
    #====
    #tls.crt:  5623 bytes
    #tls.key:  1679 bytes

..

.. code-block:: bash

    kubectl -n ingress-nginx edit deployment/ingress-nginx-controller
    # Add the following to `template.spec.container.args` ...
            - --default-ssl-certificate=default/master-cert

..

Now HTTPS also works:

.. code-block:: bash

    curl http://valohai-deployment.company.com
    curl https://valohai-deployment.company.com

..
