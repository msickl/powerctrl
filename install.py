import subprocess
from lib import config as cfg

# Generate an SSH key pair
subprocess.run('ssh-keygen -t rsa -b 4096', shell=True)

# Copy the SSH public key to the remote server
cmd = f"ssh-copy-id {cfg.switch('Username')}@{cfg.switch('Address')}"
subprocess.run(cmd, shell=True)

# Create a symbolic link and configure the systemd service
subprocess.run('ln -s /opt/powerctrl/etc/powerctrl.service /etc/systemd/system/', shell=True)
subprocess.run('systemctl enable powerctrl.service', shell=True)
subprocess.run('systemctl daemon-reload', shell=True)
subprocess.run('systemctl start powerctrl.service', shell=True)
