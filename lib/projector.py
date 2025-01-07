#!/usr/bin/env python3

import requests
import re
import base64

class ProjectorController:
    def __init__(self, server, username, password):
        self.server = server
        pjauth = f"{username}:{password}"
        pjauthbytes = base64.b64encode(pjauth.encode("utf-8"))
        self.headers = {
            "Authorization": f"Basic {pjauthbytes.decode('utf-8')}"
        }

    def status(self):
        try:
            url = f"http://{self.server}/cgi-bin/projector_status.cgi"
            res = requests.get(url, headers=self.headers, timeout=5)

            if res.status_code == 200:
                html = res.content.decode("utf-8")
                tables = re.findall(r"<table[^>]*>.*?</table>", html.lower(), re.DOTALL)

                if len(tables) > 5:
                    table = tables[5]
                    fonts = re.findall(r"<font[^>]*>.*?</font>", table, re.DOTALL)
                    colors = [
                        match[0]
                        for font in fonts
                        for match in re.findall(r'<font color="#([0-9a-fA-F]{6})">', font)
                    ]

                    if len(colors) >= 2 and colors[0] == "00ff12" and colors[1] == "999999":
                        return 1  # Projector is ON
                    else:
                        return 0  # Projector is OFF
                else:
                    print("Expected table structure not found.")
                    return -1
            else:
                print(f"Error: Received status code {res.status_code}")
                return -1

        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return -1

    def power_on(self):
        try:
            url = f"http://{self.server}/cgi-bin/power_on.cgi"
            res = requests.post(url, headers=self.headers, timeout=5)
            if res.status_code == 200:
                print("Power ON command sent successfully.")
            else:
                print(f"Failed to send Power ON command: {res.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")

    def power_off(self):
        try:
            url = f"http://{self.server}/cgi-bin/power_off.cgi"
            res = requests.post(url, headers=self.headers, timeout=5)
            if res.status_code == 200:
                print("Power OFF command sent successfully.")
            else:
                print(f"Failed to send Power OFF command: {res.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")

    def set_hdmi2(self):
        try:
            url = f"http://{self.server}/cgi-bin/proj_ctl.cgi?key=hdmi2&lang=e&x=79&y=12"
            res = requests.get(url, headers=self.headers, timeout=5)
            if res.status_code == 200:
                print("HDMI2 command sent successfully.")
            else:
                print(f"Failed to send HDMI2 command: {res.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")

# Example usage:
# projector = ProjectorController("192.168.1.100", "username", "password")
# print(projector.status())
# projector.power_on()
