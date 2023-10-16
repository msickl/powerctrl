# powerctrl

```
ln -s /opt/powerctrl/etc/powerctrl.service /etc/systemd/system/
systemctrl enable powerctrl.service
systemctrl daemon-reload
systemctrl start powerctrl.service
