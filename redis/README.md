choice: https://docs.bitnami.com/kubernetes/infrastructure/redis-cluster/get-started/compare-solutions/
cluster management params: https://github.com/bitnami/charts/tree/main/bitnami/redis-cluster

export REDIS_PASSWORD=$(kubectl get secret --namespace default my-redis4 -o jsonpath="{.data.redis-password}" | base64 -d)
kubectl port-forward --namespace default svc/my-redis4-master 6379:6379 & REDISCLI_AUTH="$REDIS_PASSWORD" redis-cli -h 127.0.0.1 -p 6379
