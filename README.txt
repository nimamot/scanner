# Port Scanner

This program is a simple implementation of a port scanner that can scan for open ports on a target host.

## Getting Started

The program takes one argument, the target hostname or IP address. The port range to be scanned can be specified by the user through the program's interface.

```python
import sys
import socket
from datetime import datetime

# Define the target
if len(sys.argv) == 2 :
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py [hostname/IP]")

# Add a banner
print("-"*50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-"*50)

# Specify the port range
print("Please specify the port range")
start = int(input("The scan starts at Port: "))
end = int(input("The scan ends at Port: "))

try:
    for port in range(start, end):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) # Returns an error indicator
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        else:
            toPrint = ("Port {} is not open".format(port))
        print(toPrint)
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to the server.")
    sys.exit()
