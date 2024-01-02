These configuration files have been coppied from [Nana](https://gitlab.com/twn-youtube/consul-crash-course/-/tree/main?ref_type=heads)!

Please fill in Access Key Id and Access Key Secret in variables.tf before you attempt running cloud provision script.

Run `./terraform/cluster_provision` and then `./k8s/install_consul` and then go to the external ip for the consul-ui load balance with `https` prefix. Ignore the certificate issue.

Hopefully then, you could have consul up and running:
<img width="974" alt="image" src="https://github.com/shehio/the-final-problem/assets/4094464/bd181248-9759-41e7-b354-37e195eb576a">

With consul up and running, you can add `consul.hashicorp.com/connect-inject: 'true'` to spec > template > annotations in the yaml definition of your microservice. This will enable:
 -  Service Mesh Integration
 -  Sidecar Proxy Responsibilities (using Envoy): Traffic Management, mTLS, Service Discovery, and Load Balancing.
 -  Automatic Service Registration
