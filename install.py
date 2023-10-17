import subprocess
from lib import config

# Generate an SSH key pair
subprocess.run('ssh-keygen -t rsa -b 4096 -C "office@sickl.at"', shell=True)

# Copy the SSH public key to the remote server
subprocess.run('ssh-copy-id admin@10.0.0.250', shell=True)

# Create a symbolic link and configure the systemd service
subprocess.run('ln -s /opt/powerctrl/etc/powerctrl.service /etc/systemd/system/', shell=True)
subprocess.run('systemctl enable powerctrl.service', shell=True)
subprocess.run('systemctl daemon-reload', shell=True)
subprocess.run('systemctl start powerctrl.service', shell=True)
