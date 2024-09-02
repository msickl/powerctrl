#!/usr/bin/env python3

import subprocess
from lib import config as cfg

# Generate an SSH key pair
print("Generate an SSH key pair")
subprocess.run("ssh-keygen -f /root/.ssh/id_rsa -q -t rsa -b 4096 -N ''", shell=True)

# Copy the SSH public key to the remote server
print("Copy the SSH public key to the remote server")
cmd = f"sshpass -p {cfg.switch('Password')} ssh-copy-id -i /root/.ssh/id_rsa -f {cfg.switch('Username')}@{cfg.switch('Address')}"

subprocess.run(cmd, shell=True)

# Create a symbolic link and configure the systemd service
print("Create a symbolic link and configure the systemd service")
subprocess.run('ln -sf /opt/powerctrl/etc/powerctrl.service /etc/systemd/system/', shell=True)
subprocess.run('systemctl enable powerctrl.service', shell=True)
subprocess.run('systemctl daemon-reload', shell=True)
subprocess.run('systemctl start powerctrl.service', shell=True)
