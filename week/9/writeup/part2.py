#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while(1):
	# receive some data
	data = s.recv(1024)
	print(data)
	if "win" in data: break
	reg = re.search('Find me the (.+?) hash of (.*)', data).groups()
	algorithm = reg[0]
	hashme = reg[1]
	hashobj = hashlib.new(algorithm)
	# print(algorithm)
	hashobj.update(hashme)
	hashed = hashobj.hexdigest()
	s.send(hashed + "\n")
# close the connection
s.close()
