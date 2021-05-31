#!/bin/python3

import sys
import socket
from datetime import datetime

# define target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid number of arguments.")
    print("Ex: python3 scanner.py <ip>")
    sys.exit()

# Add a pretty-pretty banner
start_time = datetime.now()
print("-" * 50)
print("Scanning target " + target)
print("Time started " + str(start_time))
print("-" * 50)

open_ports = 0
ports = []
try:
    for port in range(1, 10000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[#] {port: < 10} open")
            open_ports += 1
            ports.append(port)
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

print("-" * 50)
print("Finished scanning.")
print(f"Found {open_ports} open ports")
print(f"{ports}")
print(f"Total time: {(datetime.now() - start_time).total_seconds()} seconds")
print("-" * 50)

