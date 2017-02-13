#!/usr/bin/python

def selection_sort(A):
	for i in range(len(A)):
		least=i
		# finding index of the minimum value in the list
		for j in range(i+1,len(A)):
			if (A[j] < A[least]):
				least=j
		swap(A,i,least)

def swap(A,x,y):
	temp=A[x]
	A[x]=A[y]
	A[y]=temp

array=[534,246,933,127,277]

print 'array before sort=',array

selection_sort(array)

print 'after sort',array