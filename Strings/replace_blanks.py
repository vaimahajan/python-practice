#!/usr/bin/python

def replace(string,replace,replacer):
	for i in range(len(string)):
		if (replace == string[i:i+len(replacer)]):
			string=string[:i]+replacer+string[i+1:]
	print string

string='Hello world'
replace=" "

replace(string,"xx","%20")