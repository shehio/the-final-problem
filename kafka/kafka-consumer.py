from kafka import KafkaConsumer

# **Obtain bootstrap server addresses from your EKS cluster:**
# - Use `kubectl get service my-cluster-kafka-bootstrap -n <namespace>` to get the service's external IP and port.
# - Replace `<namespace>` with the actual namespace where your Kafka cluster is deployed.
bootstrap_servers = ['<external-IP>:<port>']  # Replace with actual values

# Configure the consumer
consumer = KafkaConsumer(
    'my-topic',  # Replace with the topic you want to consume from
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',  # Start consuming from the beginning of the topic
    enable_auto_commit=True,  # Automatically commit offsets
    group_id='my-consumer-group',  # Assign a consumer group name
    value_deserializer=lambda m: m.decode('utf-8')  # Deserialize message values
)

# Consume messages indefinitely
try:
    for message in consumer:
        print(f"Consumed message: {message.value}")
except KeyboardInterrupt:
    pass

# Close the consumer
consumer.close()