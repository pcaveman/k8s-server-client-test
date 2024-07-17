provider "kubernetes" {
  config_path = "~/.kube/config"
}

provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}


# Define el recurso existente
resource "kubernetes_namespace" "existing_namespace" {
  metadata {
    name = "server-ns"
  }
}

resource "helm_release" "my_app" {
  name       = "mio-server"
  chart      = "../helm-chart"
  namespace  = kubernetes_namespace.existing_namespace.metadata.0.name


  # Otros valores necesarios para tu Helm chart
}

