These configuration files have been coppied from [Nana](https://gitlab.com/twn-youtube/consul-crash-course/-/tree/main?ref_type=heads)!

Please fill in Access Key Id and Access Key Secret in variables.tf before you attempt running cloud provision script.

Run `./terraform/cluster_provision` and then `./k8s/install_consul` and then go to the external ip for the consul-ui load balance with `https` prefix. Ignore the certificate issue.
