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

# receive some data
data = s.recv(1024)
reg = re.search('Find me the (.+?) hash of (.*)', data).groups()
print(data)
algorithm = hashlib.new(reg[0])
print(reg[0])
print(algorithm)
print(reg[1])
hashed = algorithm.update(reg[1].encode('utf-8')).hexdigest()
print(hashed)
# close the connection
s.close()
