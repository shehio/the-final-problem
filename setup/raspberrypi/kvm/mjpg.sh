sudo apt-get install cmake libjpeg62-turbo-dev
sudo apt-get install gcc g++
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental/
make
sudo make install
/usr/local/bin/mjpg_streamer -i "input_uvc.so -r 640x480 -d /dev/video0 -f 24 -q 80" -o "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"