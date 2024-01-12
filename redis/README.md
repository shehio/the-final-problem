
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install my-redis bitnami/redis -f redis-values.yaml
kubectl get pods
kubectl get service
python redis-write-read.py