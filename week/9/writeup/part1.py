#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
passlist = [line.rstrip('\n') for line in wordlist]
hashes = [line.rstrip('\n') for line in open("hashes")]

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for salt in salts:
    # do stuff
    for password in passlist:
    	hashed = hashlib.sha512(salt + password).hexdigest()
    	if hashed in hashes:
    		print("hash: " + hashed + " salt: " + salt + " pass: " + password)

