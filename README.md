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
