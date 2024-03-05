## Setup tailscale subnet

### Advertise routes
`sudo tailscale up --advertise-routes=10.10.10.1/24 --exit-node={tailscale-exit-node-ip} --exit-node-allow-lan-access`

### Configure tailscale ACL
Add this ACL to [tailscale](https://login.tailscale.com/admin/acls/file)
{
			"action": "accept",
			"src":    ["10.10.10.0/24"],
			"dst":    ["10.10.10.0/24:*"],
}

### Accept routes on the tailscale exit node
`sudo tailscale up --accept-routes`


## References
- [Subnet routers and traffic relay nodes](https://tailscale.com/kb/1019/subnets)
