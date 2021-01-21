#this program is an implementation of stacks using Linked List  
#Stacks work on the idea of LIFO - Last in first out. 


#creating a class to initiate the nodes for the linked list,
#each node has two element : the data and the pointer to the item in the linked list 
#the value is passed everytime the node is to be created 
class Node():

	def __init__(self,value):
		self.data = value
		self.next = None


class stack():
	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0

	def peek(self):
		if self.isEmpty():
			print ("stack is empty")
		else :
			print (self.top.data)


	def pop(self):
		if self.isEmpty():
			print ("stack is empty")
		else:
			print ("Popped : "  + str(self.top.data))
			temp = self.top.next 
			self.top = None 
			self.top = temp 

	def push(self,value):
		newNode = Node(value)

		if self.isEmpty():
			self.top = newNode
			self.bottom = newNode

		else :
			newNode.next = self.top
			self.top = newNode

		self.length+=1 


	def isEmpty(self):
		if self.top is None:
			return True
		else :
			return False



if __name__ == '__main__':
	st = stack()
	st.push(10)
	st.push(20)
	st.push(30)
	st.peek()
	st.pop()
	st.pop()
	st.pop()
	st.peek()