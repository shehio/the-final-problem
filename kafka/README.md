kubectl apply -f kafka-values.yaml
kubectl apply -f kafka-topic.yaml
kubectl get pods
kubectl get kafka myapp-eks-cluster

pip install kafka-python