#!/bin/python

import sys
import socket
from datetime import datetime


#Defind our target
if len(sys.argv) == 2 :
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("invalid amount of argument.")
	print("syntax: python3 scanner.py")
	
# Add a banner
print("-"*50)
print("Scanning target "+target)
print("Time started : " + str(datetime.now()))
print("_"*50)
print("please specify the port range")
start = int(input("the scan starts at Port: "))
end = int(input("the scan ends at port: "))
try: 
	for port in range(start, end):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		print("checking port{}".format(port))
		if result == 0:
			print("port {} is open".format(port))
		else: 
			toPrint = ("port {} is not open".format(port))
		print(toPrint)
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gairerror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Couldn't connect to the server.")
	sys.exit()
