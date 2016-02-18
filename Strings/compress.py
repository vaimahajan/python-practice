#!/usr/bin/env python


#function to compress a string by number of consecutive similar characters
# e.g. 'aaabc' would become a2b1c1

def compress(string):
	newstr = ''
	char_count = 1
	flag = 0

	for i in range(len(string)):

		if (i != len(string)-1) and string[i] == string[i+1]:
			char_count += 1
			if (char_count > 1):
				flag = 1
		else:
			# print('else happening')
			newstr += string[i] + str(char_count)
			# print('newstr currently=', newstr)
			char_count = 1

	# to check if input string has been compressed - if not return original
	if flag == 1:
		return newstr
	else:
		return string
