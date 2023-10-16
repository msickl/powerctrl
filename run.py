#!/usr/bin/env python3

import os
import base64
import time
import sys

from lib import config as cfg
from lib import nvrdisplay as nvr
from lib import switch as sw
from lib import projector as pj
from lib import ptzcamera as ptz

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
        print("PORT: Port is online.")
        # Start Projector
        pjstat = pj.status(pjsrv, pjh)
        print(pjstat)
        if pjstat == 1:
            print("PROJECTOR: Projector is online. Nothing todo.")
        else:
            print("PROJECTOR: Projector is offline. Initiate power on.")
            pj.poweron(pjsrv, pjh)
            time.sleep(2)
            pj.sethdmi2(pjsrv, pjh)

    elif current_status == 0:
        print("PORT: Port is offline.")
        # Stop Projector
        pjstat = pj.status(pjsrv, pjh)
        if pjstat == 1:
            print("PROJECTOR: Projector is online. Switch off projector.")
            pj.poweroff(pjsrv, pjh)
        else:
            print("PROJECTOR: Projector is offline. Nothing todo.")
    else:
        print("PORT: Error can not get current port status from switch")
    
    # only if status has changed
    if status_changed == 0:
        print("PORT: Status has changed to offline")

        print("NVRDISPLAY: Initiate shutdown.")
        # Stop NVR Monitor
        nvr.shutdown(
            cfg.nvrdisplay('Address'), 
            cfg.nvrdisplay('ComPort')
        )
        
        print("PTZCAMERA: Set position to offline")
        # Status changed to off state
        ptz.setposition(
            cfg.ptzcamera('Address'),
            0
        )

    elif status_changed == 1:
        print("PORT: Status has changed to online")

        print("NVRDISPLAY: Initiate startup. Send wake on lan.")
        # Start NVR Monitor
        nvr.start(
            cfg.nvrdisplay('PhysicalAddress'), 
            cfg.nvrdisplay('WOLPort')
        )
        
        print("NVRDISPLAY: Set position to 1")
        # Status changed to on state
        ptz.setposition(
            cfg.ptzcamera('Address'),
            1
        )

    else:
        print("PORT: Status has not been changed")
        
    sys.exit(1)
    
if __name__ == "__main__":
    main()