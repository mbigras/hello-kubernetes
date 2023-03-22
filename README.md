# hello-kubernetes

> Repo hello-kubernetes illustrates how to get up and running with Kubernetes YAML API.

## Getting started

The following procedure describes how to build and run your Docker container on Kubernetes on Docker Desktop on your laptop. You deploy your app on Kuberetes with the Deployment, ConfigMap, and Secrets Kubernetes objects and also consider extension points.

1. Install Docker—see [_Get Docker_](https://docs.docker.com/get-docker/).

1. Start your Kubernetes cluster on Docker Desktop on your laptop.

   Navigate through Docker settings > Kubernetes menus, then check the _Enable Kubernetes_ box, then choose the _Apply & restart_ button—see screenshot. **Note:** You can also freely reset your Kubernetes cluster to a known clean state with the _Reset Kubernetes Cluster_ big red button.

   <img width="1382" alt="Screenshot 2023-03-21 at 12 42 36 PM" src="https://user-images.githubusercontent.com/5590632/226723415-ad587ca0-77df-450c-827a-a6a17da5af81.png">


1. Get this code.

   ```
   git clone ...
   cd hello-kubernetes
   ```

1. Build your _app_ local Docker image.

   ```
   docker build -t app app
   ```

1. Before you apply your Kubernetes YAML files against your cluster, discover all the Kubernetes resources in the _default_ namespace.

   ```
   kubectl get all
   ```

   Your output should look like the following.

   ```
   $ kubectl get all
   NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
   service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   8m29s
   ```

   Notice how there aren't many resources—only one Service Kubernetes object—that is, there isn't anything about your app running yet.

1. Before you apply your Kubernetes YAML files against your cluster, do a client-side dry-run to check that things look alright—that is, form a plan about which Kubernetes objects you're going to create.

   ```
   kubectl apply -f . --dry-run=client
   ```

   Your output should look like the following.

   ```
   $ kubectl apply -f . --dry-run=client
   configmap/app created (dry run)
   deployment.apps/app created (dry run)
   secret/app created (dry run)
   ```

   Notice that the apply should succeed and the following expected objects should be created.

   1. _app_ ConfigMap - corresponds to the key–value pairs that configure your app; these aren't secret and you can freely store the key–value pair in version control.
   1. _app_ Deployment - corresponds to the Kubernetes object that runs your app. The relationship between Kubernetes objects is like: Deployment->ReplicaSet->Pod->Container where _->_ means _manages_.
   1. _app_ Secret - corresponds to the secret key–value pairs that configure your app—for example, a password—; you should not store the secret value in version control. One strategy to follow is: store the secret key, cloud provider secrets manager secret ID, and cloud provider secrets manager secret version ID in version control; but store your secret value in your cloud provider secrets manager. **Caution**: This example puts the secret key and value in version control for illustration purposes.

1. Apply your Kubernetes YAML files against your Kuberentes cluster.

   ```
   kubectl apply -f .
   ```

   Your output should look like the following.

   ```
   $ kubectl apply -f .
   configmap/app created
   deployment.apps/app created
   secret/app created
   ```

1. Again, discover all the Kubernetes resources in the _default_ namespace.

   ```
   kubectl get all
   ```

   Your output should look like the following.

   ```
   $ kubectl get all
   NAME                       READY   STATUS    RESTARTS   AGE
   pod/app-68c8d86c84-29vtg   1/1     Running   0          38s
   pod/app-68c8d86c84-722xs   1/1     Running   0          38s
   pod/app-68c8d86c84-ztx9d   1/1     Running   0          38s
   
   NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
   service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   19m
   
   NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
   deployment.apps/app   3/3     3            3           38s
   
   NAME                             DESIRED   CURRENT   READY   AGE
   replicaset.apps/app-68c8d86c84   3         3         3       38s
   ```

   Notice that when you create a Deployment Kubernetes object, then you also create ReplicaSet and Pod objects.

1. Also, discover your ConfigMap and Secret objects.

   ```
   kubectl get configmap && kubectl get secret
   ```

   Your output should look like the following.

   ```
   $ kubectl get configmap && kubectl get secret
   NAME               DATA   AGE
   app                2      2m48s
   kube-root-ca.crt   1      21m
   NAME   TYPE     DATA   AGE
   app    Opaque   1      2m48s
   ```

1. Port forward from 8080 on your laptop to port 80 on your deployment.

   ```
   kubectl port-forward deployment/app 8080:80
   ```

1. In a new terminal, send a test GET HTTP request.

   ```
   curl localhost:8080
   ```

   Your output should look like the following.

   ```
   $ curl localhost:8080
   {
     "app": "app",
     "env": "docker-desktop",
     "features": "speed=fast,stability=unstable,experimental=true"
   }
   ```

1. Back in your terminal with your Kubernetes YAML files, delete your _app_ Deployment, ConfigMap, and Secret Kuberentes objects.

   ```
   kubectl delete -f .
   ```

   Your output should look like the following.

   ```
   $ kubectl delete -f .
   configmap "app" deleted
   deployment.apps "app" deleted
   secret "app" deleted
   ```

   **Note:** Also, you can freely reset your Kubernetes cluster to a known clean state with the _Reset Kubernetes Cluster_ big red button from Kubernetes menu in the Docker Desktop settings.


## Conclusion

This hello-kubernetes repo illustrates how to get up and running with Kubernetes with the Deployment, ConfigMap, and Secret Kubernetes objects. Consider the following extension points.

1. For secrets management, store your secrets in your cloud provider secrets manager, then you can store your app secret key, cloud provider secrets manager secret ID, and cloud provider secrets manager secret version ID in version control; but store your secret value in your cloud provider secrets manager. **Caution**: This example puts the secret key and value in version control for illustration purposes.
1. For configuration management—that is applying Kubernetes across multiple environments like dev, QA, and prod—consider the [_Kustomize_](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) default Kubernetes configuration management tool.
1. To visualize Kubernetes, consider running [_Kubernetes Dashboard_](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/).
