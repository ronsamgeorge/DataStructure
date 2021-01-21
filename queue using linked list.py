# Queue is a type of data structure which follow the First In First Out(FIFO) principle. 
# in this progrm the queue DS is implented using a Linked list 


#the class node is used to create a node which has two values : a data and a next pointer (as it is a linked list implementation)

class node():

	def __init__(self,value):
		self.data = value
		self.next = None


class queue():

	def __init__(self):
		self.first = None 
		self.last = None 
		self.length = 0

	def enqueue(self,value):
		newNode = node(value)

		if self.isEmpty() :
			self.first = newNode
			self.last = newNode
		else:
			self.last.next = newNode
			self.last = temp

		self.length+=1

	def dequeue(self):
		if self.isEmpty() :
			print("The queue is empty")
		else :
			print("the item dequeued is " + str(self.first.data))
			temp = self.first.next
			self.first = None
			self.first = temp 
			self.length -= 1

	def peek(self):
		if self.isEmpty():
			print("queue is empty")
		else :
			print(self.first.data)


	def isEmpty(self):
		if self.first is None :
			return True
		else :
			return False 


qu = queue()

qu.dequeue()
qu.enqueue(10)
qu.enqueue(20)
qu.dequeue()

qu.dequeue()
qu.peek()