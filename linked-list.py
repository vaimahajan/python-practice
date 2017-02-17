#!/usr/bin/python

class Node:
	def __init__(self,data=None,next=None):
		self.data=data
		self.next=next
	def __str__(self):
		return str(self.data) 

#functions defined outside of class definition since want to use None to rep empty list but cant call method on None

def list_length(nodelist):
	ctr=1
	current=nodelist
	while (current.next != None):
		ctr+=1
		current = current.next
	return ctr

def printList(node):
	while node:
		print node.data
		node_arr.append(node)
		node=node.next
		
def printBackward(nodelist):
  if nodelist == None: 
  	return
  head = nodelist
  tail = nodelist.next
  printBackward(tail)
  print head

# removing node at particular position - NEED TO FIX THIS
def removeNode(nodelist,pos):
	if pos > list_length(nodelist):
		return -1
	elif nodelist == None:
		return
	else:
		previous = nodelist
		current = nodelist
		ctr = 0
		while (current.next!=None and ctr<pos):
			ctr+=1
			if (ctr == pos):
				previous.next=current.next
				current.next=None
			else:
				newcurrent=current.next
				tail=newcurrent.next


def insertNode(nodelist,value,pos):
	newNode=Node(value)
	ctr=0
	current=nodelist
	previous=nodelist
	while (ctr <= pos):
		if ctr==pos:



node_arr=[]
node4=Node(4)
node3=Node(3,node4)
node2=Node(2,node3)
node1=Node(1,node2)

print 'Original linked list:-'
printList(node1)
#printBackward(node2)

print 'len=',list_length(node1)
print 'deleting node 3'
removeNode(node1,3)
print 'Modified list=', printList(node1)

# head = list ; second=list.next