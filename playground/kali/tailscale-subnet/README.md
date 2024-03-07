## Setup tailscale subnet
This is the setup to create a subnet from a device that has tailscale installed to devices that don't have tailscale installed.
Although the subnet router could be any device, this is tested on a Raspberry Pi 5 with Kali Linux.

### Pre-Req
Assuming an existing tailscale network with an exit node that advertises itself and is enabled from tailscale dashboard.

### Advertise routes
`sudo tailscale up --accept-routes --advertise-routes=10.10.10.0/24 --exit-node={tailscale-exit-node-ip} --exit-node-allow-lan-access`

### Configure tailscale ACL
Add this ACL to [tailscale](https://login.tailscale.com/admin/acls/file)

{\
	"action": "accept",\
	"src":    ["10.10.10.0/24"],\
	"dst":    ["10.10.10.0/24:*"],\
}

## References
- [Subnet routers and traffic relay nodes](https://tailscale.com/kb/1019/subnets)
