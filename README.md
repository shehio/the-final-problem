# The Final Problem
<div align="justify"> As you might have guessed, The Final Problem references The Memoirs of Sherlock Holmes. In computer science, a cluster of computers can solve any problem, so solving for the abstractions of distributed computing is the final problem. You could enjoy reading about this project while listening to <a href="https://youtu.be/uorGmVFwNQI?si=qKTMRNN-vwvqRQkY">Who You Really Are</a> soundtrack from British Sherlock! </div>
<br/>

![image](https://github.com/shehio/the-final-problem/assets/4094464/fd77053b-dadf-4cb3-afd1-5cc7b47e08b4)

## The Plan
<div align="justify">
The plan is to create a stateful cluster where the nodes can communicate with one another to solve problems. These nodes can split the workload amongst them based on their ability to compute (how socialist!). This cluster can have nodes on AWS or locally on <a href="https://www.raspberrypi.org/">Raspberry Pis</a> or Docker.
</div>
<br/>
<div align="justify">
We start by creating a <a href="https://en.wikipedia.org/wiki/Service_mesh">service mesh</a> for microservices to communicate with one another. Some of the nodes are in subnets within a <a href="https://en.wikipedia.org/wiki/Virtual_private_cloud">VPC</a>, while others should exist on-premise. After solving the service mesh problem, we will attempt to solve the consensus problem so that the stateful cluster can make progress for any generic problem. At that point, we'll introduce some problems the cluster can solve from <a href="https://en.wikipedia.org/wiki/Number_theory">Number Theory</a>, Financial Mathematics, <a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software Defined Radio</a>, or Artificial Intelligence. We will then automate and offload some of these responsibilities to higher-level abstractions like <a href="https://kafka.apache.org/">decoupling data streams</a> and <a href="https://kafka.apache.org/(https://cadenceworkflow.io/)">fault-oblivious models</a>.
</div>

## Currently

So far, the code that has been checked in:
- <div align="justify"> Setup: Scripts to install the orchestrating tools (not the infrastructure applications) and convenience tools on <a href="https://www.raspberrypi.com/software/">Raspberry Pi OS</a> and Mac OS. </div>
- <div align="justify"> <a href="https://aws.amazon.com/eks/">Elastic Kubernetes Service</a>: Create an eks cluster in aws where all the other tools are going to be installed on top of. </div>
- <div align="justify"> <a href="https://www.consul.io/">Consul</a>: Consul works as a service registry and onboards new pods to the service mesh. Among many functionalities, it leverages Envoy's reverse proxy capabilities to route and secure traffic. The application itself is supplied in Helm. </div>
- <div align="justify"> <a href="https://zookeeper.apache.org/">Zookeeper</a>: Zookeeper helps with coordination problems, as it abstracts the consensus problem away. The zookeeper folder provides a configuration file to manually deploy a cluster of zookeepers on a local/cloud cluster. It also provides a Python code example to communicate with the cluster from any node. </div>
- <div align="justify"> <a href="https://www.envoyproxy.io/">Envoy</a>: Envoy is an out-of-process proxy that can be configured to reroute traffic and enable the service mesh. </div>


### Prerequisites
You have to provision the cluster (eks) before attempting the create any of the other tools.
