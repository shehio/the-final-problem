### Distributed Components
- <div align="justify"> Setup: Scripts to install orchestrating tools on <a href="https://www.raspberrypi.com/software/">Raspberry Pi OS </a>. </div>
- <div align="justify"> <a href="https://aws.amazon.com/eks/">Elastic Kubernetes Service</a>: Elastic Kubernetes Service is AWS offerring of managed Kubernetes.</div>
- <div align="justify"> <a href="https://www.consul.io/">Consul</a>: Consul is a service registry that onboards new pods to the service mesh. It leverages Envoy's reverse proxy capabilities to route and secure traffic. </div>
- <div align="justify"> <a href="https://www.envoyproxy.io/">Envoy</a>: Envoy is an out-of-process proxy that can be configured to reroute traffic and enable the service mesh. </div>
- <div align="justify"> <a href="https://zookeeper.apache.org/">Zookeeper</a>: Zookeeper helps with coordination problems, as it abstracts the consensus problem away. The zookeeper folder provides a configuration file to manually deploy a cluster of zookeepers on a local/cloud cluster. It also provides a Python code example to communicate with the cluster from any node. </div>
- <div align="justify"> <a href="https://kafka.apache.org/">Kafka</a>: Kafka is a high-speed messaging system for real-time data streams. In an asynchronous computational model, where data liberation is a concern, Kafka prevails. </div>
- <div align="justify"> <a href="https://cadenceworkflow.io/">Cadence</a>: Cadence is a high-level fault-tolerant platform. It relies on a fault-oblivious stateful programming model. </div>
- <div align="justify"> <a href="https://redis.io/">Redis</a>: Redis is an open source in memory data store, often used as a cache for a variety of reasons. </div>

### Concepts
In this section, we'll cover many concepts related to distributed systems.
- <div align="justify"> Consistency </div>
- <div align="justify"> Availability </div>
- <div align="justify"> Partition Tolerance </div>
- <div align="justify"> Scalability </div>
- <div align="justify"> Consensus </div>
- <div align="justify"> Concurrency </div>
- <div align="justify"> Fault Tolerance </div>
- <div align="justify"> Observability </div>
- <div align="justify"> Security </div>

### Prerequisites
You have to provision the cluster (EKS) before attempting to create any of the other tools.