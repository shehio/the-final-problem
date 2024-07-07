kubectl get pods
kubectl get service

export REDIS_PASSWORD=$(kubectl get secret --namespace default my-redis -o jsonpath="{.data.redis-password}" | base64 -d)
redis-cli -c -h $SERVICE_IP -p 6379 -a $REDIS_PASSWORD

python redis-write-read.py