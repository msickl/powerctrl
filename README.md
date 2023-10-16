# powerctrl
<p>Used hardware for this solution</p>
<ul>
  <li>USW-24-PoE</li>
  <li>UCK G2 Plus</li>
  <li>Panasonic PT-VW530 (Projector)</li>
  <li>Dell OptiPlex 3050 Micro (NVR Display)</li>
  <li>Value-HD V60CL-N (PTZ Camera)</li>
</ul>

<ol>
  <li>
    First create an ssh-keygen for the unifi switch

    ssh-keygen -t rsa -b 4096 -C "office@sickl.at" 
    ssh-copy-id admin@10.0.0.250
    
  </li>
  <li>
    Install the service on the unifi cloud key

    ln -s /opt/powerctrl/etc/powerctrl.service /etc/systemd/system/
    systemctrl enable powerctrl.service
    systemctrl daemon-reload
    systemctrl start powerctrl.service
    
  </li>
</ol>
