
## Create a router + access point
These instructions have been tested for Kali version: {}

### Pre-req
sudo apt-get update && sudo apt-get upgrade -y

### Install access point software
sudo apt-get install hostapd -y

### Install dhcp software
sudo apt-get install udhcpd -y

### Assign wlan0 to an ip address
ip addr show wlan0 sudo ip addr add 10.10.10.1/24 dev wlan0

### Forward traffic from wlan0 to eth0
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT sudo iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT'

## Setup tailscale subnet

### Advertise routes
sudo tailscale up --advertise-routes=10.10.10.1/24 --exit-node={tailscale-exit-node-ip} --exit-node-allow-lan-access

### Configure tailscale acl
{

}

### Accept routes on the tailscale exit node
sudo tailscale up --accept-routes