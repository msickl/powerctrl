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
    install git on the UCK G2 Plus
    
    apt-get install git

  </li>
  <li>
    clone the repo into /opt
    
    git clone https://github.com/msickl/powerctrl.git
    
  </li>
  <li>
    create an ssh-keygen for the unifi switch

    ssh-keygen -t rsa -b 4096 -C "office@sickl.at" 
    ssh-copy-id admin@10.0.0.250
    
  </li>
  <li>
    Install the service on the UCK G2 Plus

    ln -s /opt/powerctrl/etc/powerctrl.service /etc/systemd/system/
    systemctrl enable powerctrl.service
    systemctrl daemon-reload
    systemctrl start powerctrl.service
    
  </li>
</ol>
