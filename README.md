# powerctrl

To install the Service link the powerctrl.service to the systemd services and enable the service 

```
ln -s /opt/powerctrl/etc/powerctrl.service /etc/systemd/system/
systemctrl enable powerctrl.service
systemctrl daemon-reload
systemctrl start powerctrl.service
```
There u are
