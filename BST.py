"""
 # This program is the implementation of a Binary search tree.
 # A BST is such a tree in which a node in the tree can have at most two child nodes.
 # A binary search tree has two main rules :
   	1. the values smaller than the node value will go the left of the node and the value greater than the value of the node
   	  will go to the right of the node
  	2. Each node can have either 0 ,1 or 2 number of children 

 # Complexity Analysis : 
 	1. Lookup - O(log n)
 	2. insert  - O(log n) 
 	3. delete - O(log n)

 # a perfectly balanced tree is such that the leaf nodes are all on the same level and have either 0 or 2 child nodes. 
 	this can affect the efficiency a by a lot 
"""


# each node in BST has a value ,and two child node pointers : left and right,
# this class initializes the nodes , sets the data and then initializes the child pointers to none  
class Node():

	def __init__(self,value):
		self.data = value
		self.right = None
		self.left = None 


class BST():

	def __init__(self):
		self.root = None

	def insert(self,value):

		newNode = Node(value)

		if self.isEmpty():
			self.root = newNode

		else:

			currNode = self.root

			while currNode != None:
				if (newNode.data > currNode.data):
					if (currNode.right is None):
						currNode.right = newNode
					
					currNode = currNode.right 


				elif ( newNode.data <= currNode.data):
					if (currNode.left is None):
						currNode.left = newNode

					currNode = currNode.left






	def isEmpty(self):
		if self.root is None :
			return True
		else : 
			return False
