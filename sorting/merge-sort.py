#!/usr/bin/python

def merge_sort(A):
	if (len(A) > 1):
		# dividing...
		mid=len(A)/2
		left_half=A[:mid]
		right_half=A[mid:]

		#conquering
		merge_sort(left_half)
		merge_sort(right_half)

		#initializing keys for the halves and the original array
		i=j=k=0

		#comparing elts of smaller halves and inserting into right position
		while (i<len(left_half) and j<len(right_half)):
			if (left_half[i]<right_half[j]):
				A[k]=left_half[i]
				i+=1
			else:
				A[k]=right_half[j]
				j+=1
			k+=1

		#dumping remaining elements of other half into right position
		while (i<len(left_half)):
			A[k]=left_half[i]
			i+=1
			k+=1
		while (j<len(right_half)):
			A[k]=right_half[j]
			j+=1
			k+=1

array=[534,246,933,127,277]

print 'array before sort=',array

merge_sort(array)

print 'after sort',array