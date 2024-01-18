# Playground Setup
This section of the repo describes the playground in order to be more productive and create the cluster defined in other parts of this repo.

### venv
Run `./python_setup.sh`

### VPN
1. **Install tailscale**: [instructions](https://tailscale.com/download/linux/debian-bookworm).
2. **Configure the pi as an exit node**: run `sudo sysctl -w net.ipv4.ip_forward=1` then `sudo tailscale up --advertise-exit-node`.
3. **Enable the exit node**: On [Tailscale Machines](https://login.tailscale.com/admin/machines) > `Choose the machine` > `...` > `Edit route settings ...` > `Checkbox: Use as exit node`.
