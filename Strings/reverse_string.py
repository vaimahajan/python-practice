#!/usr/bin/env python


#sample string = 'Hello world\x00'
#alternatively, could use extended slice for this - str[::-1]
def reverse(string):
	rev = ''
	strlen = len(string)
	print (strlen)
	for i in range(-1, -(strlen+1), -1):
		rev += string[i]
	return rev
