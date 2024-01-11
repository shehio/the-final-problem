aws configure
aws eks update-kubeconfig --name consul-cluster
kubectl get pods