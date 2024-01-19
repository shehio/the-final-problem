# Playground Setup
This section of the repo describes the playground in order to be more productive and create the cluster defined in other parts of this repo. Currently, we cover only ARM x64 Raspberry Pi OS.


### Raspberry Pi
For Raspberry Pi OS, this [README](https://github.com/shehio/the-final-problem/blob/main/playground/raspberrypi%20os/README.md) includes:
- VPN [tailscale]
- KVM [barrier + mjpg]
- venv [python]
- Cluster Management [aws-cli et al]


### iPhone
Assuming all your home devices are connected to tailscale network or a subnet routing from a tailscale node, here are some tools to access your local network anywhere:
- [Ping](https://apps.apple.com/us/app/ping-network-utility/id576773404?platform=iphone): Ping any node in your local network
- [Termius](https://apps.apple.com/us/app/termius-terminal-ssh-client/id549039908): SSH into your nodes
- [Tailscale](https://apps.apple.com/us/app/tailscale/id1470499037): Connect iPhone to the local network and even use any of the nodes as an exit node
- [Passepartout](https://apps.apple.com/us/app/passepartout-vpn-client/id1433648537?platform=iphone): Connect to Wireguard or OpenVPN servers


### GL-iNet Routers
- Home Router
- Travel Router
