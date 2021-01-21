#creating  a class to initial a node which has two attributes , the data and the pointer which is pointing to null at the moment  

class Node():
	def __init__(self,value):
		self.data = value
		self.next = None


#creating a the linkedlist class which has all the functionalities of the linkedlist 
class SLinkedList():

#constructor that runs everytime we create an object of this class
#at the beginning the linked list is empty. hence, both head and tail are pointing to none and the lenght of the linked is 0 
#self.head points to the first item in the linked list 
#self.tail points to the last item in the linked list 
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

#inserts the element at the end of the linked list , hence modifying self.tail is sufficient .
# care must be taken that self.tail.next is modified first , otherwise the previous tail value will be lost 
# increase the length of the 

	def append(self,value):
		newNode = Node(value)
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			self.tail = newNode

		self.length+=1

#prepend method inserts an element at the beginning of the linkedlist
#logic : the newnode created is made into the head and the node.next points to the old head. Again be careful of the 
#order in which these are down.

	def prepend(self,value):
		newNode = Node(value)
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else :
			newNode.next = self.head
			self.head = newNode
		self.length+=1

# Remove method deletes a node from the linked list depending the position provided by the user
# if the user enters the number as 2 then the second node is removed from the linked list 


	def remove(self,position):
		if (self.head == None) or (position > self.length):
			print ("invalid")

		elif (position==1):
			temp = self.head.next 
			self.head.next = None
			self.head = temp 


		else :
			currNode  = self.head
			counter = 0 
			while counter < (position-1) :
				temp = currNode
				currNode = currNode.next
				counter+=1 

			node3 = currNode.next
			temp.next = node3


	def display(self):
		if self.head == None:
			return "Empty Linkedlist"
		else:
			currNode = self.head
			while currNode is not None :
				print(currNode.data,end=" ")
				currNode = currNode.next
		print()



	def reverse(self):
		first = self.head 
		second = first.next 
		self.head.next = None 

		while second is not None :
			third = second.next 
			second.next = first 
			first = second 
			second = third

		self.head = self.tail




l1 = SLinkedList()
l1.append(10)
l1.append(20)
l1.append(30)

l1.prepend(5)
#l1.display()

l1.remove(1)
l1.display()

l1.reverse()
l1.display()

