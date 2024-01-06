sudo apt update
sudo apt install barrier

# Create a certificate
cd /home/$(whoami)/.local/share/barrier/SSL/
mkdir -p Fingerprints
openssl req -x509 -nodes -days 365 -subj /CN=barrier -newkey rsa:4096 -keyout Barrier.pem -out Barrier.pem
openssl x509 -fingerprint -sha256 -noout -in Barrier.pem > Fingerprints/Local.txt
sed -e "s/.*=/v2:sha256:/" -i Fingerprints/Local.txt