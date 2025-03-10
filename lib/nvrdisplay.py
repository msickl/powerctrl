#!/usr/bin/env python3

import json
import subprocess
from . import wol

class NVRDisplayController:
    def __init__(self, PhysicalAddress, WOLPort, IPAddress, ComPort):
        self.PhysicalAddress = PhysicalAddress
        self.WOLPort = WOLPort
        self.IPAddress = IPAddress
        self.ComPort = ComPort

    def shutdown(self):
        url = f"http://{self.IPAddress}:{self.ComPort}"
        headers = {
            "Content-Type": "application/json"
        }
    
        data = {
            "shutdown": "true"
        }
        body = json.dumps(data)
        curl_command = [
            "curl",
            "-s",
            "-X", "POST",
            "-H", f"Content-Type: {headers['Content-Type']}",
            "--data", body,
            url,
            "--insecure"
        ]
        try:
            response = subprocess.check_output(curl_command, stderr=subprocess.STDOUT, text=True, timeout=2)
            print(response)
        except subprocess.TimeoutExpired:
            print("NVRIntServer is already offline.")
        except subprocess.CalledProcessError as e:
            print(f"Request failed with error: {e.returncode}\n{e.output}")
    
    def start(self):
        wol.send(self.PhysicalAddress, self.WOLPort)
