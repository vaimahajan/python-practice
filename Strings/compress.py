#!/usr/bin/env python


#function to compress a string by number of consecutive similar characters
# e.g. 'aaabc' would become a2b1c1

# def compress(string):
# 	newstr = ''
# 	char_count = 1
# 	flag = 0

# 	for i in range(len(string)):

# 		if (i != len(string)-1) and string[i] == string[i+1]:
# 			char_count += 1
# 			if (char_count > 1):
# 				flag = 1
# 		else:
# 			# print('else happening')
# 			newstr += string[i] + str(char_count)
# 			# print('newstr currently=', newstr)
# 			char_count = 1

# 	# to check if input string has been compressed - if not return original
# 	if flag == 1:
# 		return newstr
# 	else:
# 		return string


# def alternate(A):
# 	ctr=1
# 	tmp=A[0]
# 	finalstr=''
# 	for i in range(1,len(A)):
# 		if (A[i]==tmp):
# 			ctr+=1
# 		# else append letter and its count to final string. reset counter and make tmp the new element to count
# 		else:
# 			finalstr+=tmp
# 			finalstr+=str(ctr)
# 			ctr=1
# 			tmp=A[i]
# 	# need to append letter and count again to make sure that last letter is not missed
# 	finalstr+=tmp
# 	finalstr+=str(ctr)
# 	print finalstr
# 	return

# alternate('aaabc')


def alternate_dict(string):
	ctr={}
	uniq_chars=[]

	for char in list(string):
		if char not in ctr:
			ctr[char]=1
			uniq_chars.append(char)
		else:
			ctr[char]+=1
	tmp=''

	for char in uniq_chars:
		tmp=tmp+(char+str(ctr[char]))
	print tmp
	return

alternate_dict('aaabc')