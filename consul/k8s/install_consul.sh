helm repo add hashicorp https://helm.releases.hashicorp.com
helm install eks hashicorp/consul -version 1.0.0 --values consul-values.yaml
kubectl get pods