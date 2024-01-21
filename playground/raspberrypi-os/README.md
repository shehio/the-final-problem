# Raspberry Pi OS Setup
The scripts in this directory have been tested with Bookworm.

### Verifying the Version
If you're in doubt, run the following command in terminal: `cat /etc/os-release | grep PRETTY_NAME`. If you get `PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"` then we're on the right track.

### USB Booting
1. **Boot from USB**: `sudo raspi-config` > `6 Advanced Options` > `A4 Boot Order` > `B1 SD Card Boot  Boot from SD Card if available, otherwise boot from NVMe`.
2. **Disable power limits**: `sudo raspi-config` > `4 Performance Options` > `P4 USB Current` > `Would you like the USB current limit to be disabled?` > `<Yes>`.

### KVM

#### Mouse and Keyboard

Run `./kvm/barrier.sh`

Steps to manually disable Wayland and enable X11
- $ sudo raspi-config
- Choose 6 Advanced Options > A6 Wayland > W1 X11

Run Barrier
- Accessories > Barrier > Run as a server
- Click Configure Server
- Drag and drop a client from the upper right to where it would appear relative to the server
- Add a screen name that matches the computer's name
- Optional: Add an alias or modify keys

#### Webcam

Run `./kvm/mjpg.sh`
Check localhost:8080 for the stream on the same node

For any node on the network: it should be {ipaddress}:8080 or custom ip address from tailscale if you're using overlay vpn

To enable this camera on zoom on any node on the network:
- Install OBS
- In source, add browser
- Add url: http://{ip}:8080/?action=stream
- In controls, click Start Virtual Camera
- In Zoom > Preferences > Video > OBS Virtual Camera

### Install Tools:
Run `./install_apps.sh && ./cloud/install_cloud_apps.sh`

### VPN
1. **Configure the pi as an exit node**: run `sudo sysctl -w net.ipv4.ip_forward=1` then `sudo tailscale up --advertise-exit-node`.
2. **Enable the exit node**: On [Tailscale Machines](https://login.tailscale.com/admin/machines) > `Choose the machine` > `...` > `Edit route settings ...` > `Checkbox: Use as exit node`.

### venv
Run `./python_setup.sh` in the root of the repo.