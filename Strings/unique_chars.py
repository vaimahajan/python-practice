#!/usr/bin/env python


def unique_chars(string):
	visited = []
	if len(string) > 128:
		return "String does not have all unique chars"		# assuming ASCII char set
	for i in range(len(string)):
		if string[i] in visited:
			return "String does not have all unique chars"
		else:
			visited.append(string[i])
	print (visited)
	return "String has unique chars"
