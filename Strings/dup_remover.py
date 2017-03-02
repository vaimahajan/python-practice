#!/usr/bin/python

def remove_dups(A):
	A.sort()
	j=0
	for i in range(1,len(A)):
		if(A[j]!=A[i]):
			j+=1
			A[j]=A[i]
	print A[:j+1]


arr=[5,4,5,6,7,8,5]
remove_dups(arr)