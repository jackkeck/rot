# cat <<EOT > rot_core.py
import boto3
import json
import time
import os
import subprocess
import sys
from subprocess import Popen, PIPE
from bson import json_util 

def run_shell_command(shell_command):
    process = subprocess.Popen([shell_command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    (strdout, strderr) = process.communicate() 
    if strdout != None:
        shell_out = strdout.splitlines()
    else:
        shell_out = ["no stdout for ./setup_machine"]
    if strderr != None:
        shell_err = strderr.splitlines()
    else:
        shell_err = ["no stderr for ./setup_machine" ]
    return shell_out, shell_err
    
def setup_directory():
    log_create_command  =   '''
                            rot_run_dir="rot-run-$(date "+%Y%m%d-%H%M%S")" && mkdir $rot_run_dir && cd "$_"
                            '''
    working_directory = os.getcwd()
    return working_directory

def install_required(working_directory): 
    shell_command = './setup_machine.sh' 
    (shell_out, shell_err) = run_shell_command(shell_command)  
    return shell_out, shell_err

def fetch_lets_encrypt(working_directory, domain, web_master_email):
    shell_command  =    '''
                        sudo /opt/letsencrypt/letsencrypt-auto certonly --standalone --non-interactive --agree-tos --email ''' + web_master_email  + ''' --domains ''' + domain + ''' --pre-hook 'sudo service openvpnas stop' --post-hook 'sudo service openvpnas start
                        '''
    (shell_out, shell_err) = run_shell_command(shell_command)   
    return shell_out, shell_err  

def symlink_lets_encrypt(domain):
    shell_command  =    '''
                        sudo ln -s -f /etc/letsencrypt/live/''' + domain + '''/cert.pem /usr/local/openvpn_as/etc/web-ssl/server.crt 
                        sudo ln -s -f /etc/letsencrypt/live/''' + domain + '''/privkey.pem /usr/local/openvpn_as/etc/web-ssl/server.key
                        '''
    (shell_out, shell_err) = run_shell_command(shell_command)   
    return shell_out, shell_err  

def power_to_open_vpnas(boom='restart'):
    shell_command  =    '''
                        sudo service openvpnas '''+boom+''' &&
                        echo ${boom}
                        '''
    shell_out = subprocess.run(shell_command)   
    return shell_out   


 
