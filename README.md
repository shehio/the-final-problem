# The Final Problem
<div align="justify"> As you might have guessed, The Final Problem references The Memoirs of Sherlock Holmes. In computer science, a cluster of computers can solve any problem, so solving for the abstractions of distributed computing is the final problem. </div>

## The Plan
<div align="justify">
The plan is to create a stateful cluster where the nodes can communicate with one another to solve problems. These nodes can split the workload amongst them based on their ability to compute (how socialist!). This cluster can have nodes on AWS or locally on <a href="https://www.raspberrypi.org/">Raspberry Pis</a> or Docker.
</div>
<br/>
<div align="justify">
We should start by creating a <a href="https://en.wikipedia.org/wiki/Service_mesh">service mesh</a> for the services to communicate with one another. Some of the nodes should be in subnets within a <a href="https://en.wikipedia.org/wiki/Virtual_private_cloud">VPC</a>, while others should exist on-premise. After solving the service mesh problem, we should solve the consensus problem so that the stateful cluster can make progress. At that point, we'll introduce some problems the cluster can solve. We then should automate and offload some of these responsibilities to higher-level abstractions like <a href="https://kafka.apache.org/">decoupling data streams</a> and <a href="https://kafka.apache.org/(https://cadenceworkflow.io/)">fault-oblivious models</a>.
</div>

## Currently

So far, the code that has been checked in:
- <div align="justify"> Provisioning: Scripts to provision orchestrating tools (not the infrastructure applications) and convenience tools on <a href="https://www.raspberrypi.com/software/">Raspberry Pi OS</a>. </div>
- <div align="justify"> <a href="https://www.consul.io/">Consul</a>: Consul works as a service registry and onboards new pods to the service mesh. Among many functionalities, it leverages Envoy's reverse proxy capabilities to route and secure traffic. Consul code is provided with an Elastic Kubernetes Service (EKS) installation. The cloud infrastructure is provided in Terraform, and the application itself is supplied in Helm. </div>
- <div align="justify"> <a href="https://zookeeper.apache.org/">Zookeeper</a>: Zookeeper helps with coordination problems, as it abstracts the consensus problem away. The zookeeper folder provides a configuration file to manually deploy a cluster of zookeepers on a local/cloud cluster. It also provides a Python code example to communicate with the cluster from any node. </div>
- <div align="justify"> <a href="https://www.envoyproxy.io/">Envoy</a>: Envoy is an out-of-process proxy that can be configured to reroute traffic and enable the service mesh. </div>
