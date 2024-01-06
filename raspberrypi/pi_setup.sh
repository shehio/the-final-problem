sudo apt update
sudo apt install snapd
sudo snap install core

sudo apt install awscli

sudo snap install terraform --classic
sudo ln -s /snap/terraform/current/bin/terraform /snap/bin/

sudo snap install kubectl --classic
sudo ln -s /snap/kubectl/current/bin/kubectl /snap/bin/

sudo snap install k9s
sudo ln -s /snap/k9s/current/bin/k9s /snap/bin/

curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh

sudo apt install code