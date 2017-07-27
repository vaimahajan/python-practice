#/usr/bin/python

#-------------------------------------
# Sort array of 0s 1s and 2s - TO DO!!!!!!!
#-------------------------------------

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

def sort_dutch(A):
	low=0
	high=len(A)-1
	mid=0
	while (mid<=high):
		if (A[mid]==0):
			A[low],A[mid]=A[mid],A[low]
			low+=1
			mid+=1
		elif (A[mid]==1):
			mid+=1
		else:
			A[mid],A[high]=A[high],A[mid]
			high-=1
	print A
	return

sort_dutch(arr)