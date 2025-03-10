#!/usr/bin/env python3

import json
import subprocess
from . import wol

class NVRDisplayController:
    def __init__(self, server, username, password):
        self.server = server
        pjauth = f"{username}:{password}"
        pjauthbytes = base64.b64encode(pjauth.encode("utf-8"))
        self.headers = {
            "Authorization": f"Basic {pjauthbytes.decode('utf-8')}"
        }

    def shutdown(self, server, port):
        url = f"http://{server}:{port}"
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
    
    def start(self, server, port):
        wol.send(server, port)
