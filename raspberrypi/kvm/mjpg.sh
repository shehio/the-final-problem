sudo apt-get install cmake libjpeg62-turbo-dev
sudo apt-get install gcc g++
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental/
make
sudo make install
/usr/local/bin/mjpg_streamer -i "input_uvc.so -r 640x480 -d /dev/video0 -f 24 -q 80" -o "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"

Check localhost:8080 for the stream on the same node

For any node on the network: it should be {ipaddress}:8080 or custom ip address from tailscale if you're using overlay vpn

To enable this camera on zoom on any node on the network:
- Install OBS
- In source, add browser
- Add url: http://{ip}:8080/?action=stream
- In controls, click Start Virtual Camera
- In Zoom > Preferences > Video > OBS Virtual Camera