#!/usr/bin/python

class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
	def set_data(self,data):
		self.data=data
	def get_data(self):
		return self.data()
	def get_left(self):
		return self.left
	def get_right(self):
		return self.right

# creating objects (to allocate memory)
root=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)

# defining object parameters
root.left=node2
root.right=node3

result=[]

# Root -> left -> right
def preorder(root,result):
	# exit condition; base case to end recursive call (when root.left/root.right becomes Null ie. when child nodes reached)
	if not root:
		return
	result.append(root.data)
	preorder(root.left, result)
	preorder(root.right, result)

#preorder(root,result)

# left -> root -> right
def inorder(root,result):
	if not root:
		return
	inorder(root.left,result)
	result.append(root.data)
	inorder(root.right,result)

#inorder(root,result)

# left -> right -> root
def postorder(root,result):
	if not root:
		return
	postorder(root.left,result)
	postorder(root.right,result)
	result.append(root.data)

postorder(root,result)
print result