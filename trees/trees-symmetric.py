#!/usr/bin/python

# ----------------------------
# Determine if two trees are symmetric
# ----------------------------

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def symTree(root1,root2):
	if (root1 is None) and (root2 is None):
		return True
	elif (root1 is not None) and (root2 is not None):
		return (root1.data == root2.data) and symTree(root1.left,root2.right) and symTree(root1.right,root2.left)
	else:
		return False

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(2)
root1.left.left = Node(3)
root1.right.right = Node(3)

if symTree(root1.left,root1.right):
	print 'Tree is symmetric'
else:
	print 'Not symettric'