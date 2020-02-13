# cat <<EOT > rot_execute.py
import rot_core
import boto3
import json
import time
import os
import subprocess
import sys
from subprocess import Popen, PIPE
from bson import json_util 

def execute(domain, web_master_email):

    # BOOM GOES THE DYNAMITE
    rot_core.power_to_open_vpnas('stop')

    # CREATE BASE WORKING DIRECTORY 
    working_directory = rot_core.setup_directory()

    # INSTALL REQUIRED LIBRARIES AND PACKAGES
    rot_core.install_required(working_directory)

    # GENERATE CERTIFICATES & KEYS USING LETSENCRYPT
    rot_core.fetch_lets_encrypt(working_directory, domain, web_master_email)

    # SYMLINK CERTIFICATES & KEYS DELIVERED BY LETSENCRYPT
    rot_core.symlink_lets_encrypt(domain)

    # BOOM GOES THE DYNAMITE
    rot_core.power_to_open_vpnas('start')


domain = 'openvpn.jackkeck.fail'
web_master_email = 'jkeck@xops.it'
execute(domain, web_master_email)
