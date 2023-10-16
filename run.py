#!/usr/bin/env python3

import os
import base64
import time
import sys

from lib import config as cfg
from lib import nvrdp as nvr
from lib import switch as sw
from lib import projector as pj
from lib import ptzcameras as ptz

def main():
    # Initialize Switch Parameters
    current_status = sw.current_port_status(
        cfg.switch('Address'),
        cfg.switch('PortToMonitor')
    )
    status_changed = sw.port_status_changed()
    
    # Initialize Projector Parameters
    pjsrv = cfg.projector('Address')
    pjauth = f"{cfg.projector('Username')}:{cfg.projector('Password')}"
    pjauthbytes = base64.b64encode(pjauth.encode('utf-8'))
    pjh = {
        "Authorization": f"Basic {pjauthbytes.decode('utf-8')}"
    }

    # everytime when script is called
    if current_status == 1:
        # Start Projector
        pjstat = pj.status(pjsrv, pjh)
        if pjstat == 1:
            print("Port is online. Projector is online. Nothing todo.")
        else:
            print("Port is online. Projector is offline. Initiate power on.")
            pj.poweron(pjsrv, pjh)
            time.sleep(2)
            pj.sethdmi2(pjsrv, pjh)

    elif current_status == 0:
        # Stop Projector
        pjstat = pj.status(pjsrv, pjh)
        if pjstat == 1:
            print("Port is offline. Projector is online. Switch off projector.")
            pj.poweroff(pjsrv, pjh)
        else:
            print("Port is offline. Projector is offline. Nothing todo.")
    else:
        print("Error can not get current port status from switch")
    
    # only if status has changed
    if status_changed == 0:
        print("Status has changed to online")
        # Start NVR Monitor
        nvr.start(
            cfg.nvrdisplay('PhysicalAddress'), 
            cfg.nvrdisplay('WOLPort')
        )
        
        # Status changed to off state
        ptz.setposition(
            cfg.ptzcamera('Address'),
            0
        )
    elif status_changed == 1:
        # Stop NVR Monitor
        nvr.shutdown(
            cfg.nvrdisplay('Address'), 
            cfg.nvrdisplay('ComPort')
        )
        
        # Status changed to on state
        ptz.setposition(
            cfg.ptzcamera('Address'),
            1
        )
    else:
        print("Status has not been changed")
        
    sys.exit(1)
    
if __name__ == "__main__":
    main()