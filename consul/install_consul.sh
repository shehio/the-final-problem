helm repo add hashicorp https://helm.releases.hashicorp.com
helm install consul-release hashicorp/consul -version 1.0.0 --values consul-values.yaml --set global.datacenter=eks
kubectl get pods
kubectl get all
