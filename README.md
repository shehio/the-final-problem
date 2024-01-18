# The Final Problem

### What
<div align="justify"> As you might have guessed, The Final Problem references The Memoirs of Sherlock Holmes. In computer science, a cluster of computers can solve any problem, so solving for the abstractions of distributed computing is the final problem. You could enjoy reading about this project while listening to <a href="https://youtu.be/uorGmVFwNQI?si=qKTMRNN-vwvqRQkY">Who You Really Are</a> soundtrack from British Sherlock! </div>
<br/>

### Why
<div align="justify">
Solve problems with a wide range from <a href="https://en.wikipedia.org/wiki/Number_theory">Number Theory</a> to Financial Mathematics, <a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software Defined Radio</a>, and Artificial Intelligence.
</div>

### How
<div align="justify">
Create a <a href="https://en.wikipedia.org/wiki/State_(computer_science)">stateful</a> cluster where the nodes, in the cloud or on premise, can communicate with one another using a <a href="https://en.wikipedia.org/wiki/Service_mesh">service mesh</a>. The nodes can split the workload amongst them based on their computational abilities (how socialist!). By delegating consensus to other components, the stateful cluster can make progress for any generic problem. At that point, we'll introduce some problems the cluster can solve. We will then offload some of these responsibilities to higher-level abstractions like <a href="https://kafka.apache.org/">decoupling data streams</a> and <a href="https://kafka.apache.org/(https://cadenceworkflow.io/)">fault-oblivious models</a>.
</div>

![image](https://github.com/shehio/the-final-problem/assets/4094464/fd77053b-dadf-4cb3-afd1-5cc7b47e08b4)

### Todos
- Infra
  - Add Consul POC based on demo microservices
  - Add Kafka POC based on demo microservices
  - Add Zookeeper in helm
  - Explore Redis options in AWS
- Home Lab
  - Separate home lab code from the cluster code under the setup directory
  - Remove or Modify the code for setup/mac
- Visualization
  - Add icons for the tools used
  - Add service communication figure
- Problems
  - Create prime lists based where different pods reserve chunks of numbers and test their primality -- based on zookeeper
- Misc
  - Clean up different READMEs
  - Make all scripts unblocking and executable
  - Provide AMD64 Debian/Ubuntu setup scripts
 
 ### Future Plans
 Provide an API that makes sense to tackle the largest number of problems: A parser to parse commands and creates infra structure for the specific problem.
