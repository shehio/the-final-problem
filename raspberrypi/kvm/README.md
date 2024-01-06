# KVM

## Mouse and Keyboard

Run `barrier.sh`

Steps to manually disable Wayland and enable X11
- $ sudo raspi-config
- Choose 6 Advanced Options > A6 Wayland > W1 X11

Run Barrier
- Accessories > Barrier > Run as a server
- Click Configure Server
- Drag and drop a client from the upper right to where it would appear relative to the server
- Add a screen name that matches the computer's name
- Optional: Add an alias or modify keys

## Webcam

Run `mjpg.sh`
Check localhost:8080 for the stream on the same node

For any node on the network: it should be {ipaddress}:8080 or custom ip address from tailscale if you're using overlay vpn

To enable this camera on zoom on any node on the network:
- Install OBS
- In source, add browser
- Add url: http://{ip}:8080/?action=stream
- In controls, click Start Virtual Camera
- In Zoom > Preferences > Video > OBS Virtual Camera