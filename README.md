# k8s-server-client-test

# Kubernetes Cluster Testing Project

This project aims to test different aspects within a Kubernetes (k8s) cluster.

## Overview

### Server / Client Directories
These directories contain two simple applications that are connected via TCP and store logs on the hard disk.

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

### istio analyse
istioctl dashboard
istioctl dashboard kiali
istioctl dashboard envoy server-deployment-6ffdffd9f9-qf4tt.server-ns


istioctl proxy-config cluster client-deployment-86747c8d66-l29sp -n server-ns
istioctl proxy-config route client-deployment-86747c8d66-l29sp -n server-ns

