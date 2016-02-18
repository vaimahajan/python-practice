#!/usr/bin/env python


#fn to check if a string is a permutation of another
def permute(a, b):
	if len(a) != len(b):
		return "Strings not permutations -1"
	else:
		a_dict = {}
		b_dict = {}

		# making dictionary of chars in string a
		for char in a:
			if char in a_dict.keys():
				a_dict[char] += 1
			else:
				a_dict[char] = 1
		
		# making dictionary of characters in string b
		for char in b:
			if char not in a_dict.keys():
				print ('keys in a are:', a_dict.keys())
				print ('this wasnt found', char)
				return "Strings not permutations -2"
			elif char in b_dict.keys():
				b_dict['char'] += 1
			else:
				b_dict['char'] = 1

	# comparing dictionaries for both strings
		for a_key in a_dict.keys():
			for b_key in b_dict.keys():
				if (a_key == b_key) and (a_dict[a_key] != b_dict[b_key]):
					return "Not permutations! -3"
		return "Strings are permutations!"
