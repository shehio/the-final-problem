sudo apt update
sudo apt install cmake libjpeg62-turbo-dev -y
sudo apt install gcc g++ -y
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental/
make
sudo make install
/usr/local/bin/mjpg_streamer -i "input_uvc.so -r 640x480 -d /dev/video0 -f 24 -q 80" -o "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"
