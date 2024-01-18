Create Kafka server using: `kubectl apply -f kafka-values.yaml`.
Create Kafka topic using: `kubectl apply -f kafka-topic.yaml`.
Verify the installation using: `kubectl get pods`, `kubectl get service`, and `kubectl get kafka myapp-eks-cluster`.

pip install kafka-python

Set the bootstrap_servers in `kafka-producer.py` on line 6 by getting the EXTERNAL-IP from `kubectl get service` for the pods of TYPE LoadBalancer.
Set the bootstrap_servers in `kafka-consumer.py` on line 6 by getting the EXTERNAL-IP from `kubectl get service` for the pods of TYPE LoadBalancer.

Download and extract Kafka from [Apache](https://kafka.apache.org/downloads) and cd to `bin` directory to run `kafka-console-consumer.sh` with arguments `--bootstrap-server` and `--topic my-topic`.