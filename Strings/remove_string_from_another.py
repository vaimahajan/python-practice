#!/usr/bin/python

# Script to remove chars of one string from another

def string_chars_removal(mainString,removeCharsString):
	dict_removal={}		#hash table of chars to remove
	final_str=[]

	for char in removeCharsString.lower():
		dict_removal[char]=1

	for i in mainString.lower():
		if i not in dict_removal:
			final_str.append(i)

	return ''.join(final_str)


print string_chars_removal('Hello','lo')