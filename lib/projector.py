#!/usr/bin/env python3

import requests
import re

def init(server, username, password):
    this.server = server
    pjauth = f"{username}:{password}"
    pjauthbytes = base64.b64encode(pjauth.encode('utf-8'))
    this.headers = {
        "Authorization": f"Basic {pjauthbytes.decode('utf-8')}"
    }

def status():

    url = f"http://{this.server}/cgi-bin/projector_status.cgi"
    res = requests.get(url, headers=this.headers)

    if res.status_code == 200:

        html = res.content.decode('utf-8')
        tables = re.findall(r'<table[^>]*>.*?</table>', html.lower(), re.DOTALL)
        table = tables[5]
        fonts = re.findall(r'<font[^>]*>.*?</font>', table, re.DOTALL)

        colors = []
        for font in fonts:
            match = re.findall(r'<font color="#([0-9a-fA-F]{6})">', font)
            colors.append(match[0])

        if colors[0] == "00ff12" and colors[1] == "999999":
            return 1
        else:
            return 0
    else:
        return -1

def poweron():
    url = f"http://{this.server}/cgi-bin/power_on.cgi"
    requests.post(url, headers=this.headers)

def poweroff():
    url = f"http://{this.server}/cgi-bin/power_off.cgi"
    requests.post(url, headers=this.headers)

def sethdmi2():
    url = f"http://{this.server}/cgi-bin/proj_ctl.cgi?key=hdmi2&lang=e&x=79&y=12"
    requests.get(url, headers=this.headers)
