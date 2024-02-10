Set the bootstrap_servers in `kafka-consumer.py` on line 6 by getting the EXTERNAL-IP from `kubectl get service` for the pods of TYPE LoadBalancer.
Set the bootstrap_servers in `kafka-producer.py` on line 6 by getting the EXTERNAL-IP from `kubectl get service` for the pods of TYPE LoadBalancer.

Download and extract Kafka from [Apache](https://kafka.apache.org/downloads) and cd to `bin` directory to run `kafka-console-consumer.sh` with arguments `--bootstrap-server` and `--topic my-topic`.