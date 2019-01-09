---
title:  "kubernetes"
tags:
  - kubernetes
  - tutorial
---
{% include toc %}

# Install kubernetes on Ubuntu 18.04.1 LTS (Bionic Beaver)

### [install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/){:target="_blank"}
```shell
apt-get update && sudo apt-get install -y apt-transport-https
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y kubectl
```

### [install docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1){:target="_blank"}
```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
apt-key fingerprint 0EBFCD88
add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
apt-get update
```


Since minikube doesn't support docker's latest version i'll install the previous version.
```shell
#[ERROR SystemVerification]: unsupported docker version: 18.09.0
#
apt-get install docker-ce=18.06.1~ce~3-0~ubuntu
```

### [install minikube](https://github.com/kubernetes/minikube/releases){:target="_blank"}
```shell
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.32.0/minikube-linux-amd64 && chmod +x minikube && sudo cp minikube /usr/local/bin/ && rm minikube
```

# Start minikube
```shell
minikube version
minikube start --vm-driver=none
```

# Discover kubernetes

## Create a Cluster
### cluster version
```shell
kubectl version
```
###  cluster details
```shell
kubectl cluster-info
```
###  show all nodes
```shell
kubectl get nodes
```
## Deploy an app
```shell
kubectl run kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1 --port=8080
```
### list deployments
```shell
kubectl get deployments
```
### run the proxy
```shell
kubectl proxy
```
### query version through the API
```shell
curl http://localhost:8001/version
```
### get API of the Pod
{% raw %}
```shell
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/
```
{% endraw %}

## Explore Your App
### look for existing Pods
```shell
kubectl get pods
```
### details about the Pod’s container
```shell
kubectl describe pods
```
### print the logs from a container in a pod
{% raw %}
```shell
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
kubectl logs $POD_NAME
```
{% endraw %}

### execute a command on a container in a pod
```shell
kubectl exec $POD_NAME env
```
### start a bash session in the Pod’s container
```shell
kubectl exec -ti $POD_NAME bash
```
###  list the current Services
```shell
kubectl get services
```
## [kubeadm reset](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-reset/){:target="_blank"}
Certificate not valid after changing IP
```shell
Unable to connect to the server: x509: certificate is valid for xxx.xxx.xxx.xxx
```
```shell
kubeadm reset
minikube start --vm-driver=none
```

## Expose Your App Publicly
### Create a new service
{% raw %}
```shell
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
kubectl get services
kubectl describe services/kubernetes-bootcamp
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT
curl $(minikube ip):$NODE_PORT
```
{% endraw %}

### Using labels
{% raw %}
```shell
kubectl describe deployment
kubectl get pods -l run=kubernetes-bootcamp
kubectl get services -l run=kubernetes-bootcamp
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
kubectl label pod $POD_NAME app=v1
kubectl describe pods $POD_NAME
kubectl get pods -l app=v1
```
{% endraw %}

### Deleting a service
```shell
kubectl delete service -l run=kubernetes-bootcamp
kubectl get services
curl $(minikube ip):$NODE_PORT
kubectl exec -ti $POD_NAME curl localhost:8080
```

## Scale Your App
### Scaling a deployment
```shell
kubectl scale deployments/kubernetes-bootcamp --replicas=4
kubectl get deployments
kubectl get pods -o wide
kubectl describe deployments/kubernetes-bootcamp
```

### Load Balancing
{% raw %}
```shell
kubectl describe services/kubernetes-bootcamp
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT
curl $(minikube ip):$NODE_PORT
```
{% endraw %}

### Scale Down
```shell
kubectl scale deployments/kubernetes-bootcamp --replicas=2
kubectl get deployments
kubectl get pods -o wide
```

## Update Your App
### Update the version of the app
```shell
kubectl get deployments
kubectl get pods
kubectl describe pods
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2
kubectl get pods
```

### Verify an update
{% raw %}
```shell
kubectl describe services/kubernetes-bootcamp
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT
curl $(minikube ip):$NODE_PORT
kubectl rollout status deployments/kubernetes-bootcamp
kubectl describe pods
```
{% endraw %}

### Rollback an update
```shell
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10
kubectl get deployments
kubectl get pods
kubectl describe pods
kubectl rollout undo deployments/kubernetes-bootcamp
kubectl get pods
kubectl describe pods
```

## [Hello Minikube](https://kubernetes.io/docs/tutorials/hello-minikube/){:target="_blank"}
### Create a Deployment & Service
```shell
kubectl create deployment hello-node --image=gcr.io/hello-minikube-zero-install/hello-node
kubectl get deployments
kubectl get pods
kubectl get events
kubectl config view
kubectl expose deployment hello-node --type=LoadBalancer --port=8080
kubectl get services
minikube service hello-node
```
Browsing to http://xxx.xxx.xxx.xxx:8080 will shows the “Hello World” message.
### Enable addons
```shell
minikube addons list
minikube addons enable heapster
kubectl get pod,svc -n kube-system
minikube addons disable heapster
```
### Clean Up
```shell
kubectl delete service hello-node
kubectl delete deployment hello-node
```

# Docker Compose File to Kubernetes Resources
## kompose
```shell
curl -L https://github.com/kubernetes/kompose/releases/download/v1.17.0/kompose-linux-amd64 -o kompose
chmod +x kompose
sudo mv ./kompose /usr/local/bin/kompose
```
























{% include comments.html %}













