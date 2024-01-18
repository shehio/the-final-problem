### VPN
1. **Install tailscale**: [instructions](https://tailscale.com/download/linux/debian-bookworm).
2. **Configure the pi as an exit node**: run `sudo sysctl -w net.ipv4.ip_forward=1` then `sudo tailscale up --advertise-exit-node`.
3. **Enable the exit node**: On [Tailscale Machines](https://login.tailscale.com/admin/machines) > `Choose the machine` > `...` > `Edit route settings ...` > `Checkbox: Use as exit node`.
