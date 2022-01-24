Install NGINX Ingress Controller
---------------------------------

Installing NGINX Ingress Controller which we use routing incoming connections to individual endpoints.

.. code-block:: bash

    kubectl create namespace ingress-nginx

    helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
    helm repo update

    # you can use `helm show values ingress-nginx/ingress-nginx` to get the all possible installation customization
    helm install \
        ingress-nginx \
        ingress-nginx/ingress-nginx \
        --version v3.31.0 \
        --namespace ingress-nginx


Make sure ``ingress-nginx-controller`` pod is running, might take a minute:

.. code-block:: bash

    kubectl get pods --all-namespaces
    # NAMESPACE       NAME                                        READY   STATUS    RESTARTS   AGE
    # ingress-nginx   nginx-ingress-controller-6885bc7778-rckm6   1/1     Running   0          2m15s

See that the ``ingress-nginx`` is running and get the external address:

.. code-block:: bash

    kubectl -n ingress-nginx get service/ingress-nginx-controller
    # The external IP is something on the lines of `XXX.YYY.elb.amazonaws.com` or a raw IP

Now we should get a default NGINX 404 from the load balancer external IP:

.. code-block:: bash

    curl http://XXX.YYY.elb.amazonaws.com


.. admonition:: Optional: Modify Load Balancer Security Group
    :class: tip

    You can now modify the NGINX configuration, like adding a load balancer security group on AWS to allow only certain CIDR ranges or Security Groups to access the endpoints.

    .. code-block:: 

        kubectl -n ingress-nginx edit service/ingress-nginx-controller

        # e.g. adding to annotations:

        # **If** you want to use TLS certificates generated through AWS, replace with the correct value of 
        # the generated certificate in the AWS console. Otherwise, setup free TLS/HTTPS in `3-deployment-https`.
        service.beta.kubernetes.io/aws-load-balancer-ssl-cert: "arn:aws:acm:YYYYYYY:XXXXXXXX:certificate/XXXXXX-XXXXXXX-XXXXXXX-XXXXXXXX"

        # Ensure the ELB idle timeout is less than nginx keep-alive timeout. By default,
        # NGINX keep-alive is set to 75s. ELB is 60. If using WebSockets, the value will need to be
        # increased to '3600' to avoid any potential issues.
        service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout: "60"

        # **If** a customer wants to limit access to the endpoints, you might want to create a new security group where 
        # you can set the inbound rules, but you can also simply modify the existing one.
        service.beta.kubernetes.io/aws-load-balancer-security-groups: "sg-XXXXXXXXX”

