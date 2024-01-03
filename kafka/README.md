Create Kafka server using: `kubectl apply -f kafka-values.yaml`
Create Kafka topic using: `kubectl apply -f kafka-topic.yaml`
kubectl get pods
kubectl get kafka myapp-eks-cluster

pip install kafka-python

Set the bootstrap_servers in `kafka-producer.py` on line 6 by getting the EXTERNAL-IP from `kubectl get service` for the pods of TYPE LoadBalancer