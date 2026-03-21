kubectl get pods
kubectl get service

export REDIS_PASSWORD=$(kubectl get secret --namespace default my-redis -o jsonpath="{.data.redis-password}" | base64 -d)
export SERVICE_IP=$(kubectl get svc my-redis-master -o jsonpath='{.spec.clusterIP}')
redis-cli -c -h $SERVICE_IP -p 6379 -a $REDIS_PASSWORD
