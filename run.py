#!/usr/bin/env python3

import os
import base64
import time
import sys

from lib import config as cfg
from lib.nvrdisplay import NVRDisplayController
from lib import switch as sw
from lib.projector import ProjectorController
from lib.ptzcamera import PTZCameraController

def main():
    # Initialize Switch Parameters
    current_status = sw.current_port_status(
        cfg.switch('Address'),
        cfg.switch('PortToMonitor')
    )
    status_changed = sw.port_status_changed()
    
    pj = ProjectorController(cfg.projector('Address'), cfg.projector('Username'), cfg.projector('Password'))
    nvr = NVRDisplayController(cfg.nvrdisplay('PhysicalAddress'), cfg.nvrdisplay('WOLPort'), cfg.nvrdisplay('Address'), cfg.nvrdisplay('ComPort'))
    ptz = PTZCameraController(cfg.ptzcamera('Address'))
    
    # everytime when script is called
    if current_status == 1:
        print("PORT: Port is online.")

        # Start NVR Monitor
        print("NVRDISPLAY: Initiate startup. Send wake on lan.")
        nvr.start()

        if pj.status() == 1:
            print("PROJECTOR: Projector is online. Nothing todo.")
        else:
            print("PROJECTOR: Projector is offline. Initiate power on.")
            pj.power_on()
            time.sleep(2)
            pj.set_hdmi2()
            time.sleep(1)
            pj.set_picture_mode_dynamic()

    elif current_status == 0:
        print("PORT: Port is offline.")
        
        # Stop NVR Monitor
        print("NVRDISPLAY: Initiate shutdown.")
        
        nvr.shutdown()
        
        # Stop Projector
        pjstat = pj.status()
        if pjstat == 1:
            print("PROJECTOR: Projector is online. Switch off projector.")
            pj.power_off()
        else:
            print("PROJECTOR: Projector is offline. Nothing todo.")
    else:
        print("PORT: Error can not get current port status from switch")
    
    # only if status has changed
    if status_changed == 0:
        # Status changed to off state
        print("PORT: Status has changed to offline")
        print("PTZCAMERA: Set position to offline")
        
        ptz.setposition(cfg.ptzcamera('StandbyPosition'))

    elif status_changed == 1:
        # Status changed to on state
        print("PORT: Status has changed to online")
        print("NVRDISPLAY: Set position")
        
        ptz.setposition(cfg.ptzcamera('DefaultPosition'))
    else:
        print("PORT: Status has not been changed")

    # Wait for 5 seconds due to port issues before initiating the next restart.
    time.sleep(5)    
    sys.exit(1)
    
if __name__ == "__main__":
    main()
