#!/usr/bin/python

#BINARY SEARCH - ARRAY NEEDS TO BE SORTED!!

def binary_search(A,number):
	low=0
	high=len(A)-1
	found=False

	while low<=high and not found:
		mid=(low+high)//2
		if A[mid]>number: 
			high=mid-1
		elif A[mid]<number:
			low=mid+1
		else: 
			found=True
			return mid
	return -1

array=[5,7,1,2,3,9,12,71,8]

print 'array is: ',array

#print 'Enter no to find:-'
#find_this=int(raw_input('Enter your input:'))

#print type(find_this)

array.sort()

print '\nSorted array is ', array

print '\nsearching for 5'#,find_this

pos=binary_search(array,5)

print '\nElement found at position ',pos