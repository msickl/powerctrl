#!/usr/bin/env python3
import subprocess
import json
import os

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
    
    data['current'] = portstatus(server, port)
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
    

    
