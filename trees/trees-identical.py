#!/usr/bin/python

# ----------------------------
# Determine if two trees are identical
# ----------------------------

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def identicalTrees(root1,root2):
	if (root1 is None) and (root2 is None):
		return True
	elif (root1 is not None) and (root2 is not None):
		return (root1.data==root2.data) and identicalTrees(root1.left,root2.left) and identicalTrees(root1.right,root2.right)
	else:
		return False

# Driver program to test identicalTrees function
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(6)

if identicalTrees(root1, root2):
	print "Both trees are identical"
else:
    print "Trees are not identical"
