
#!/usr/bin/python

import socket
ip = raw_input("Enter the ip address: ")
port = input("Enter the port number")
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if soc.connect_ex((ip,port)):
	print "port", port, "is closed"
else:
	print "Port", port, "port is  open"

