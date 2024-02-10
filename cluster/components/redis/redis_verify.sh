kubectl get pods
kubectl get service

export SERVICE_IP=$(kubectl get svc --namespace default my-redis2-redis-cluster-0-svc --template "{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}")
export REDIS_PASSWORD=$(kubectl get secret --namespace "default" my-redis2-redis-cluster -o jsonpath="{.data.redis-password}" | base64 -d)
redis-cli -c -h $SERVICE_IP -p 6379 -a $REDIS_PASSWORD

python redis-write-read.py