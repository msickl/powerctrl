#!/usr/bin/env python3

import socket

def send(server, port):
    print(f"Send magic packet to {server} on port {port}")
    magic_packet = bytes.fromhex('FF' * 6 + server.replace(':', '') * 16)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(magic_packet, ('<broadcast>', port))
    sock.close()