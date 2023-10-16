#!/usr/bin/env python3

import os
import json

config_file_path = os.path.join(os.path.dirname(__file__), '../var/config.json')

with open(config_file_path, "r") as f:
    cfg = json.load(f)

def get(s):
    return cfg[s]
    
def switch(s):
    return cfg['Switch']
    
def nvrdisplay(s):
    return cfg['NVRDisplay']
    
def ptzcamera(s):
    return cfg['PTZCamera']

def projector(s):
    return cfg['Projector']