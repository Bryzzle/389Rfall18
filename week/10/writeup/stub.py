#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import time
import struct

host = "142.93.118.186"   # IP address or URL
port = 1234     # port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.recv(1024)
s.send('1\n')
s.recv(1024)
message = 'CMSC389R Rocks!'    # original message here
s.send(message + '\n')
data = s.recv(1024).strip()
legit = data.split("hash: ", 1)[1]

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'badbadbad'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()

#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

for secretlen in range(6, 16):
	# converts number to its little endian representation
	endian = struct.pack("<q", (len(message) + secretlen) * 8)
	zeroes = '\x00' * (64 - len(message) - secretlen - len(endian) - 1)
	# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
	# after the 0's is a byte with message length in bits, little endian style
	padding = '\x80' + zeroes + endian
	payload = message + padding + malicious
	s.send('2\n')
	print(s.recv(1024))
	s.send(fake_hash + '\n')
	print(s.recv(1024))
	s.send(payload + '\n')
	print(s.recv(1024))
# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!

print("legit: " + legit)
print("fake: " + fake_hash)
print("payload: " + payload)

s.close()