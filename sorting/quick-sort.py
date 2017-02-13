#!/usr/bin/python

def quick_sort(A,low,high):
	if (low<high):
		pivot=partition(A,low,high)		#real pivot
		quick_sort(A,low,pivot-1)
		quick_sort(A,pivot+1,high)

#to find the pivot index
def partition(A,low,high):
	pivot = low
	swap(A,low,high)
	#high is temp pivot used for comparisons and all swapping done between A[i] and A[low]
	for i in range(low,high):
		if(A[i]<=A[high]):
			swap(A,i,low)
			low+=1

	#swapping updated low value with high
	swap(A,low,high)
	return low

def swap(A,x,y):
	temp=A[x]
	A[x]=A[y]
	A[y]=temp

array=[534,246,933,127,277]

print 'array before sort=',array

quick_sort(array,0,len(array)-1)

print 'array after sort=',array