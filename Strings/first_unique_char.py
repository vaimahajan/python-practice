#!/usr/bin/python

def find_unique(A):
	table={}
	
	for char in A.lower():
		if char in table:
			table[char] += 1
		elif char != " ":
			table[char] = 1
		else:
			table[char]=0
	print table
	for char in A.lower():
		if table[char]==1:
			#print("First repeated char is %s" %(char))
			return char


string='abczdabc'
print find_unique(string)