#!/usr/bin/env python3

import requests
import re

def status(server, headers):

    url = f"http://{server}/cgi-bin/projector_status.cgi"
    res = requests.get(url, headers=headers)

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

def poweron(server, headers):
    url = f"http://{server}/cgi-bin/power_on.cgi"
    requests.post(url, headers=headers)

def poweroff(server, headers):
    url = f"http://{server}/cgi-bin/power_off.cgi"
    requests.post(url, headers=headers)

def sethdmi2(server, headers):
    url = f"http://{server}/cgi-bin/proj_ctl.cgi?key=hdmi2&lang=e&x=79&y=12"
    requests.get(url, headers=headers)