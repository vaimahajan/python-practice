#!/usr/bin/python

import os

def bubble_sort(A):
	for i in range(len(A)):
		for k in range(len(A)-1,i,-1):
			if (A[k]<A[k-1]):
				swap(A,k,k-1)

def swap(A,x,y):
	temp=A[x]
	A[x]=A[y]
	A[y]=temp

array=[534,246,933,127,277]

f=open('op_bubble','w')

#print 'array before sort=',array

f.write('array before sort= ')
#f.write(array) -> wont work!!
for item in array:
	f.write(str(item)+' ')

bubble_sort(array)

#print 'after sort',array

f.write("\n"+'after sort ')
#f.write(array)
for item in array:
	f.write(str(item)+' ')

f.close()