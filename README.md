# powerctrl

1. First create an ssh-keygen for the unifi switch

```
ssh-keygen -t rsa -b 4096 -C "office@sickl.at"
ssh-copy-id admin@10.0.0.250
```

2. Install the service on the unifi cloud key

```
ln -s /opt/powerctrl/etc/powerctrl.service /etc/systemd/system/
systemctrl enable powerctrl.service
systemctrl daemon-reload
systemctrl start powerctrl.service
```
