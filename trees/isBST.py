#!/usr/bin/python

# ----------------------------
# Check if given tree is BST
# ----------------------------

import sys

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# creating tree (is a valid BST)
root=Node(5)
root.left=Node(3)
(root.left).left=Node(2)
(root.left).right=Node(4)

root.right=Node(6)
(root.right).right=Node(7)

minN=-(sys.maxint)
maxN=(sys.maxint)

def isBST(root,minN,maxN):
	if (root is None):
		return True
	# each node needs to be within valid BST range
	elif ((root.data<=minN) or (root.data>maxN)):
		return False
	else:
		return (isBST(root.left,minN,root.data) and isBST(root.right,root.data,maxN))

print isBST(root,minN,maxN)