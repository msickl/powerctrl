#!/usr/bin/env python3
import subprocess
import json
import os
from lib import config as cfg

data = {
    'previous': 0,
    'current': 0
}

envpath = '/tmp/portstatus.json'

def current_port_status(server, port):
    global data, envpath

    if os.path.exists(envpath):
        with open(envpath, 'r') as file:
            data = json.load(file)
    else:
        with open(envpath, 'w') as file:
            json.dump(data, file)
    
    status = portstatus(server, port)
    if status != -1:
        data['current'] = status

    with open(envpath, 'w') as file:
        json.dump(data, file)
        
    return data['current']

def port_status_changed():           
    global data, envpath

    if os.path.exists(envpath):
        with open(envpath, 'r') as file:
            data = json.load(file)
            
        if data['previous'] != data['current']:
            data['previous'] = data['current']
            with open(envpath, 'w') as file:
                json.dump(data, file)
            return data['current']
        else:
            return -1
    else:
        return -1

def portstatus(server, port):
    try:
        cmd = f"ssh admin@{server} \"swctrl port show id {port}"
        cmd += " | awk '{print \$2}' | sed -e 3d -e '\$!d'\""

        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=4)
        if result.returncode == 0:
            status = result.stdout.strip()
            if status == 'U/U':
                return 1
            else:
                return 0
        else:
            return -1
    except subprocess.TimeoutExpired:
        return -1
    except Exception as e:
        return -1

def connect():
    print("Generate an SSH key pair")
    subprocess.run("ssh-keygen -f /root/.ssh/id_rsa -q -t rsa -b 4096 -N '' <<< y", shell=True)
    
    print("Copy the SSH public key to the remote server")
    cmd = f"sshpass -p {cfg.switch('Password')} ssh-copy-id -i /root/.ssh/id_rsa -f {cfg.switch('Username')}@{cfg.switch('Address')}"
    subprocess.run(cmd, shell=True)


    
