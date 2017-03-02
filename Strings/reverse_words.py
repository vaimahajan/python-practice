#!/usr/bin/python

import re

string = "Hello world"

oldlist = string.split(' ')		#works if string doesnt have punctuations, else use regex!
newlist=[]

for word in oldlist:
	newlist.append(word[::-1])
print " ".join(newlist)