# powerctrl
<p>Used hardware for this solution</p>
<ul>
  <li>UCK G2 Plus (powerctrl service)</li>
  <li>USW-24-PoE (Switch)</li>
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

    cd /opt
    git clone https://github.com/msickl/powerctrl.git
    
  </li>
  <li>
    install the service

    python3 /opt/powerctrl/install.py
    
  </li>
</ol>
