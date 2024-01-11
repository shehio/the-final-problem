# The Final Problem
<div align="justify"> As you might have guessed, The Final Problem references The Memoirs of Sherlock Holmes. In computer science, a cluster of computers can solve any problem, so solving for the abstractions of distributed computing is the final problem. You could enjoy reading about this project while listening to <a href="https://youtu.be/uorGmVFwNQI?si=qKTMRNN-vwvqRQkY">Who You Really Are</a> soundtrack from British Sherlock! </div>
<br/>

![image](https://github.com/shehio/the-final-problem/assets/4094464/fd77053b-dadf-4cb3-afd1-5cc7b47e08b4)

### The Plan
<div align="justify">
Create a <a href="https://en.wikipedia.org/wiki/State_(computer_science)">stateful</a> cluster where the nodes, in the cloud or on premise, can communicate with one another to solve problems. The nodes can split the workload amongst them based on their computational abilities (how socialist!). The problems can have a wide range from <a href="https://en.wikipedia.org/wiki/Number_theory">Number Theory</a> to Financial Mathematics, <a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software Defined Radio</a>, and Artificial Intelligence.
</div>


### How
<div align="justify">
 Create a <a href="https://en.wikipedia.org/wiki/Service_mesh">service mesh</a> where microservices can exist on different nodes and communicate with one another. By delegating consensus to other components, the stateful cluster can make progress for any generic problem. At that point, we'll introduce some problems the cluster can solve from  We will then automate and offload some of these responsibilities to higher-level abstractions like <a href="https://kafka.apache.org/">decoupling data streams</a> and <a href="https://kafka.apache.org/(https://cadenceworkflow.io/)">fault-oblivious models</a>.
</div>

### Components
- <div align="justify"> Setup: Scripts to install orchestrating tools on <a href="https://www.raspberrypi.com/software/">Raspberry Pi OS </a>. </div>
- <div align="justify"> <a href="https://aws.amazon.com/eks/">Elastic Kubernetes Service</a>: Elastic Kubernetes Service is AWS offerring of managed Kubernetes.</div>
- <div align="justify"> <a href="https://www.consul.io/">Consul</a>: Consul is a service registry that onboards new pods to the service mesh. It leverages Envoy's reverse proxy capabilities to route and secure traffic. </div>
- <div align="justify"> <a href="https://www.envoyproxy.io/">Envoy</a>: Envoy is an out-of-process proxy that can be configured to reroute traffic and enable the service mesh. </div>
- <div align="justify"> <a href="https://zookeeper.apache.org/">Zookeeper</a>: Zookeeper helps with coordination problems, as it abstracts the consensus problem away. The zookeeper folder provides a configuration file to manually deploy a cluster of zookeepers on a local/cloud cluster. It also provides a Python code example to communicate with the cluster from any node. </div>
- <div align="justify"> <a href="https://kafka.apache.org/">Kafka</a>: Kafka is a high-speed messaging system for real-time data streams. In an asynchronous computational model, where data liberation is a concern, Kafka prevails. </div>
- <div align="justify"> <a href="https://cadenceworkflow.io/">Cadence</a>: Cadence is a high-level fault-tolerant platform. It relies on a fault-oblivious stateful programming model. </div>
- <div align="justify"> <a href="https://redis.io/">Redis</a>: Redis is an open source in memory data store, often used as a cache for a variety of reasons. </div>

### Prerequisites
You have to provision the cluster (EKS) before attempting to create any of the other tools.
