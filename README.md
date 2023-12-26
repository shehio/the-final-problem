# The Final Problem
<p align="justify">
As you might have guessed, The Final Problem references The Memoirs of Sherlock Holmes. I named this project The Final Problem because, in computer science, a cluster of computers can solve any problem, so solving for the abstractions of distributed computing is the final problem I need to solve.
</p>

## The Plan
The plan is to create a stateful cluster that is able to communicate and solve problems where the nodes can communicate with one another. These nodes can split the workload amongst them based on their ability to compute (how socialist!). This cluster can be on AWS, [Raspberry Pis](https://www.raspberrypi.org/), or Docker. They will also leverage new technology like [Zookeeper](https://zookeeper.apache.org/), [Kafka](https://kafka.apache.org/), and [Cadence](https://cadenceworkflow.io/).

## Currently
So far, the code that has been checked in:
- Raspberry Pi: Scripts to provision orchestrating tools (not the infrastructure applications) and convenience tools on [Raspberry Pi OS](https://www.raspberrypi.com/software/).
- Zookeeper: Zookeeper helps with coordination problems, as it abstracts the problem of consensus away. The zookeeper folder provides a configuration file to deploy a cluster of zookeepers on a local/cloud cluster manually. It also provides a Python code example to communicate with the cluster from any node.
- Consul: Consul works as a service registry and onboards new pods to the service mesh. Among many functionalities, it leverages envoy's reverse proxy capabilities to route and secure traffic. Consul code is provided with an Elastic Kubernetes Service (EKS) installation. The cloud infrastructure is provided in Terraform, and the application itself is provided in Helm.
