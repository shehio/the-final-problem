aws  configure
aws eks update-kubeconfig --name consul-cluster

helm repo add hashicorp https://helm.releases.hashicorp.com

kubectl apply -f config-consul.yaml
kubectl get pods