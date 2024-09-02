#!/usr/bin/env python3

import subprocess
from lib import config as cfg
from lib import switch as sw

# Connect to unifi Switch
sw.connect()

# Create a symbolic link and configure the systemd service
print("Create a symbolic link and configure the systemd service")
subprocess.run('ln -sf /opt/powerctrl/etc/powerctrl.service /etc/systemd/system/', shell=True)
subprocess.run('systemctl enable powerctrl.service', shell=True)
subprocess.run('systemctl daemon-reload', shell=True)
subprocess.run('systemctl start powerctrl.service', shell=True)
