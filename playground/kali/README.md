
## Create a router + access point
These instructions have been tested for Kali version: {}

### Pre-req
`sudo apt-get update && sudo apt-get upgrade -y`

### Install access point software
`sudo apt-get install hostapd -y`

### Install dhcp software
`sudo apt-get install udhcpd -y`

### Assign wlan0 to an ip address
`ip addr show wlan0`
`sudo ip addr add 10.10.10.1/24 dev wlan0`

### Configure hostapd
Add
```
interface=wlan0
driver=nl80211
ssid=test-ssid
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=test-password
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
```
to `hostapd.conf`

### Forward traffic from wlan0 to eth0
`sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE`

`sudo iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT`

`sudo iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT'`

## Setup tailscale subnet

### Advertise routes
`sudo tailscale up --advertise-routes=10.10.10.1/24 --exit-node={tailscale-exit-node-ip} --exit-node-allow-lan-access`

### Configure tailscale acl
{

}

### Accept routes on the tailscale exit node
`sudo tailscale up --accept-routes`


## References
- [Subnet routers and traffic relay nodes](https://tailscale.com/kb/1019/subnets)
