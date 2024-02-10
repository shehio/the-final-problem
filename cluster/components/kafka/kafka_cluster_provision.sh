helm repo add strimzi https://strimzi.io/charts/

helm install kafka-app strimzi/strimzi-kafka-operator

kubectl apply -f kafka-values.yaml