#!/usr/bin/python

array=[5,2,4,6,1,3]
array2=[534,246,933,127,277]

# Algo
# START
# for all elements starting from the 2nd till end of list:
# 	Set key to current element index
# 	while key > 0 and current element value < prev element value
# 		swap prev elt and current element
# 		decrement key

def my_insertion_sort(A):
	for i in range(1,len(A)):
		k=i
		while (k>0 and A[k]<A[k-1]):
			temp=A[k-1]
			A[k-1]=A[k]
			A[k]=temp
			k-=1

print 'array before sort=',array2

my_insertion_sort(array2)

print 'after sort',array2