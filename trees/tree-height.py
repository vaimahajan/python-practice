#!/usr/bin/python

# ----------------------------
# Find height of given tree
# ----------------------------

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
	if (root is None):
		return 0
	else:
		return (max(height(root.left),height(root.right))+1)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(2)
root1.left.left = Node(3)
root1.right.right = Node(3)

print height(root1)