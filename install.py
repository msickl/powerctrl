ssh-keygen -t rsa -b 4096 -C "office@sickl.at" 
ssh-copy-id admin@10.0.0.250

ln -s /opt/powerctrl/etc/powerctrl.service /etc/systemd/system/
systemctrl enable powerctrl.service
systemctrl daemon-reload
systemctrl start powerctrl.service
