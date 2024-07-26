# k8s-server-client-test

# Kubernetes Cluster Testing Project

This project aims to test different aspects within a Kubernetes (k8s) cluster.

## Overview

### Server / Client Directories
These directories contain two simple applications that are connected via TCP and store logs on the hard disk.

#### prerequisite for Python
python3.12 -m pip install --upgrade pip
pip3.12 install -r requirements.txt

### k8s Directory
The `k8s` directory includes resources for the k8s cluster:
- Two deployments
- A service
- Persistent volumes

### istio Directory
The `istio` directory includes resources for configuring istio.io planes, which help the cluster function by providing auxiliary functions such as monitoring, traffic management, etc.

### consul Directory
The `consul` directory includes resources for configuring Consul.

## Current technologies used for running
### Container management (Rancher Desktop can be an alternative)
- containerd 
- nerdctl
- buildkit
### K8s cluster tools
- kubectl
- microk8s
### service mash 
- istio.io
- hashicorp/consul


## Setup instructions
- Configurer prerequisites mentioned above
### microk8s 
required for istio to find a cluster
microk8s config > ~/.kube/config

### install helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm repo add stable https://charts.helm.sh/stable
helm repo update

### install terraform
sudo apt-get update && sudo apt-get upgrade -y
wget https://releases.hashicorp.com/terraform/1.9.2/terraform_1.9.2_linux_amd64.zip
sudo apt-get install unzip -y
unzip terraform_1.9.2_linux_amd64.zip
sudo mv terraform /usr/local/bin/
terraform version

### images
running buildkit: sudo ~/.local/bin/buildkitd

nerdctl images
cd ./server
nerdctl build -t my-server-image .
nerdctl save -o my-server-image.tar my-server-image:latest
microk8s ctr image import my-server-image.tar
### istio install 
alias k="kubectl"
istioctl upgrade
istioctl install --set profile=demo
k get all
k get namespaces
k get istio-system
k get all -n istio-system
k label namespace server-ns istio-injection=enabled
k get namespace -L istio-injection

### deploy app in k8s 
k config set-context --current --namespace=server-ns
k delete service,deployment,pv,pvc --all -n server-ns 
k apply -f ./k8s/cluster.yaml
k get all
k exec -n server-ns -it server-deployment-785c46c697-7xg2w -- /bin/sh

### remove k8s deployments
k delete deployments,service --all

### istio analyse
istioctl dashboard
istioctl dashboard kiali
istioctl dashboard envoy server-deployment-6ffdffd9f9-qf4tt.server-ns


istioctl proxy-config cluster client-deployment-86747c8d66-l29sp -n server-ns
istioctl proxy-config route client-deployment-86747c8d66-l29sp -n server-ns

### istio disabling for delivering sidecar container

k label namespace server-ns istio-injection=disabled

### istio removal

kubectl delete -f <aplicacion-1.yml>
kubectl delete -f <aplicacion-2.yml>
kubectl get namespaces
istioctl uninstall --purge
kubectl delete namespace istio-system
kubectl get crds | grep 'istio.io' | awk '{print $1}' | xargs kubectl delete crd
kubectl get all --all-namespaces | grep -i istio

### helm install with k8s
helm install mio-server ./my-chart
helm uninstall mio-server

### terraform install with k8s
alias t=terraform
cd "terraform" folder
t init
t import
t plan
t apply
t show
t destroy

## TODO
- helm chart
  + extract parameters into values (e.g. port)
  + delivery to local cluster
  - delivery resources for istio
- terraform
  + delivery to local k8s cluster
  - delivery to GKE
- observability 
  - add info to prometheus, not only in logs