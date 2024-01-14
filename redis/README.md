sudo apt-get install redis-tools

export REDIS_PASSWORD=$(kubectl get secret --namespace default my-redis4 -o jsonpath="{.data.redis-password}" | base64 -d)
kubectl port-forward --namespace default svc/my-redis4-master 6379:6379 & REDISCLI_AUTH="$REDIS_PASSWORD" redis-cli -h 127.0.0.1 -p 6379

kubectl get pods
kubectl get service
python redis-write-read.py