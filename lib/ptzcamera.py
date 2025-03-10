#!/usr/bin/env python3

import requests

class PTZCameraController:
    def __init__(self, server):
        self.server = server

    def setposition(self, pos):
        url = f"http://{self.server}/cgi-bin/ptzctrl.cgi?ptzcmd&poscall&{pos}"
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            print(f"Position {pos} has been set.")
        else:
            print(f"There was a problem to set the position {pos}")
