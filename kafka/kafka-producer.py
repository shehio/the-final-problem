from kafka import KafkaProducer

# **Obtain bootstrap server addresses from your EKS cluster:**
# - Use `kubectl get service my-cluster-kafka-bootstrap -n <namespace>` to get the service's external IP and port.
# - Replace `<namespace>` with the actual namespace where your Kafka cluster is deployed.
bootstrap_servers = ['<external-IP>:<port>']  # Replace with actual values

# Configure the producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: v.encode('utf-8'))

# Specify the topic name
topic_name = 'my-topic'  # Replace with your desired topic name

# Send some messages
for i in range(10):
    message = f"Message {i}"
    producer.send(topic_name, message)
    print(f"Sent message: {message}")

# Flush messages to ensure delivery
producer.flush()

# Close the producer
producer.close()