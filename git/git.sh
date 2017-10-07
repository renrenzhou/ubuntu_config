sudo apt-get install git
sudo apt-get install git-core
sudo apt-get install ssh
#create a ssh key 
ssh-keygen -C "itjustzhou@gmail.com" -t rsa
cp -rf ~/.ssh/* .

#config git
git config --global user.name "renrenzhou"
git config --global user.email "itjustzhou@gmail.com"

