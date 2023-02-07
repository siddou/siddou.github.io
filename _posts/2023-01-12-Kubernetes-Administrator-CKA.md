---
classes: wide
title:  "Certified kubernetes Administrator (CKA)"
tags:
  - kubernetes
  - certification
---
{% include toc %}

## [Exam guide](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/){:target="_blank"}

## [Exam course](https://github.com/kodekloudhub/certified-kubernetes-administrator-course){:target="_blank"}


## Notes

### Core Concepts

#### Cluster Architecture

##### Master Node

- Manage, Plan, Schedule, Monitor Nodes:
  - **ETCD Cluster**: DB, Highly available key-value store. Store informations about the cluster.
  - **Kube-Scheduler**:
  - **Controller-Manager**:
  - **Node-Controller**:
  - **Replication-Controller**:
  - **Kube-apiserver**: Responsible for orchestrating all operation within the cluster

##### Worker Nodes

- Host Application as Containers:
  - **kubelet**: Agent that run on each node, listen for kube-apiserver instructions, deploy, destroy containers on the node as required
  - **kube-proxy**: ensure that rules are in place on the worker node to allow the container running on them to reach each other
  - **Container Runtime**: Run container, installed on all nodes. Support multiple runtime engine (Docker, Containerd, rkt)

#### ETCD For Beginners

##### What is ETCD?

- Distributed reliable key-value store that is Simple, Secure & Fast.
- it has pod in the kube-system namespace on the Master Node named **etcd-master**.
- Listen on port 2379.
- In a HA Environment, you will have multiple master nodes so multiple ETCD instances.

##### What is a Key-Value Store?

Store information in the form of documents or pages so each individual gets a document and all information about that individual is stored within that file. These files can be in any format (json, yaml) or structure and changes to one file doesn't affect the others.

#### Kube-API Server

- Primary managment component in K8S.
- **kubctl** utility is reaching to the Kube-API server.
- the Kube-API server first authenticate the request and validates it.
- Then retrieves data from the ETCD cluster and response back with request information.
- Only component that interacts directly with the ETCD Datastore.
- Responsible for
  - Authenticate user
  - Validate request
  - Retrieve data
  - Update ETCD
  - Scheduler
  - Kubelet
- it has pod in the kube-system namespace on the Master Node named **kube-apiserver-master**.

#### Kube Controller Manager

##### Node-Controller

- monitor the status of the nodes and keep the application running.
- Node Monitor Period = 5s
- Node Monitor Grace Period = 40s
- POD Eviction Timeout = 5m
- If the pod doesn't comeback up, it remove the pod assign to that node, and provision it on healty node.

##### Replication-Controller

- Monitor status of replicas set.
- Ensure desired number of pods are available at all time within the set.
- If the pod dies, it create another one

#### Kube Scheduler

- Decides which node the pods are placed on depending on certain criteria.
- Looks at each nodes and tries to find the best node for it.
- 1. Filter Nodes
- 2. Rank Nodes

#### Kubelet

- Register Node
- Create PODs
- Monitor Node & PODs

#### Kube Proxy

-**POD Network**: internal virtual network the spans across all the nodes in the cluster.
-**service**: virtual component that only lives in the K8S memory.
- Process that runs on each nod
- Its job is to look for new services
- create rules on each nodes to forward traffic to those services to the backend pods with Iptables.

#### PODs

- Container encapsulated in a K8S object known as pods.
- Pod have a one-to-on relationship with containers running your application.
- To scale up, create new pods.
- To scale down, you delete existing pod.
- **Multi-containers PODs**
  - a single pod can have multiple containers
  - they're usually not multiple containers of the same kind
  - ex. Helper containers (process or fetch data from elsewhere)
  - they communicate together by referring to each other as localhost since they share the same network/storage space

##### Replication Controller

- **Replication Controller**: older technology
- **Replica Set**: new recommended way to setup replication
- monitor the pod and ensure that the specified number of pods are running at all times
- Create multiple pods to share the load across them

##### Labels and Selectors

- Use label as a filter for replicat set

##### Deployments

- kind: Deployment
- K8S object that comes higher than Replicat Set
- Provide capability to upgrade the underlying instances seamlessly using rolling updates, undo changes, and pause, and resume changes as required.

##### Services

- enable communication between component
- kind: Service
- **NodePort**: service make makes an internal port accessible on a port on the node.
- **Cluster IP**: create a virtualIP inside the cluster to enable communication between different services (ex set of frontend to set of backend servers)
- **Loadbalancer**: distribute load

##### Namespaces

- kind: Service
- can enable resource quota by namespace

##### Imperative vs Declarative

- **Imperative**: Specify what to do
- **Declarative**: Specify final destination (ex.IAC tools).
- "kubectl run"   -> Imperative
- "kubectl apply -f /path/to/config-files" -> Declarative



## Commands

List all:

```shell
kubectl get all
```

List pods:

```shell
kubectl get pods
```

Create a new pod:

```shell
vim pod.yaml
```

```shell
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx
```

```shell
kubectl create -f pod.yaml
```

Show specific pod:

```shell
kubectl describe pod newpods-kblb2
```

Show all pods with their Node:

```shell
kubectl describe pod | grep -B 4 "Node:"
```

List replicasets:

```shell
kubectl get replicasets
```

Delete a pod:

```shell
kubectl delete pod new-replica-set-2mpd8
```

Create a replicaset:

```shell
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: replicaset-1
spec:
  replicas: 2
  selector:
    matchLabels:
      tier: frontend
  template:
    metadata:
      labels:
        tier: frontend
    spec:
      containers:
      - name: nginx
        image: nginx
```

```shell
kubectl create -f replicaset-definition-1.yaml
```

Delete Replicaset

```shell
kubectl delete replicaset replicaset-1
```

Edit ReplicatSet

```shell
kubectl edit replicaset new-replica-set
```

Replace or Update ReplicatSet

```shell
kubectl replace -f replicaset-definition-1.yaml
```

Scale ReplicatSet

```shell
kubectl scale --replicas=5 rs/new-replica-set
```

Create an NGINX Pod:

```shell
kubectl run nginx --image=nginx
```

Generate POD Manifest YAML file (dry run):

```shell
kubectl run nginx --image=nginx --dry-run=client -o yaml
```

Generate Deployment YAML file (dry run):

```shell
kubectl create deployment --image=nginx nginx --replicas=4 --dry-run=client -o yaml > nginx-deployment.yaml
```

Defining a Service:

```shell
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```

```shell
kubectl create -f service-definition-1.yaml
```

List pods on all namespaces:

```shell
kubectl get pods --all-namespaces | grep blue
```

