#!/bin/bash

sudo apt -y install python3 2>&1 | tee -a setup-machine.sh.log
sudo apt -y install python3-pip 2>&1 | tee -a setup-machine.sh.log
pip3 install --user --upgrade awscli  2>&1 | tee -a setup-machine.sh.log 
echo -n $PATH | awk -v RS=: '!($0 in a) {a[$0]; printf("%s%s", length(a) > 1 ? ":" : "", $0)}' 2>&1 | tee -a setup-machine.sh.log 
[[ ":$PATH:" != *":~/.local/bin:"* ]] && echo 'export PATH="~/.local/bin:$PATH"' | tee -a ~/.bash_profile  2>&1 | tee -a setup-machine.sh.log 
echo $(source ~/.bash_profile) 2>&1 | tee -a setup-machine.sh.log
sudo apt-get -y install software-properties-common 2>&1 | tee -a setup-machine.sh.log
sudo add-apt-repository -y ppa:certbot/certbot 2>&1 | tee -a setup-machine.sh.log
sudo apt-get -y update 2>&1 | tee -a setup-machine.sh.log
sudo apt-get -y install certbot 2>&1 | tee -a setup-machine.sh.log 
sudo git clone https://github.com/letsencrypt/letsencrypt /opt/letsencrypt
git clone https://github.com/jackkeck/rot.git