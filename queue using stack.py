# this program is from leetcode, link to the ques : https://leetcode.com/problems/implement-queue-using-stacks/description/
# in this program a queue is implemented using stack operations 

# In this approach dequeue is 0(n) while enqueue is 0(1)
# this solution is uses 2 stacks 
# everytime a dequeue is called we need to pop the first element that was pushed but it is at the bottom of the stack1.
# so we pop all the items, except the last one, from stack1 to stack2.
# when there is only one item left in stack1 we just pop it out as we usually do.
# then we pop back everything from stack2 to stack 1 to maintain the order 


# creating a queue which will have the functionality of the queue using stack operations. 
class queue():

	# initialling two empty list, stack1 and stack2 , on which we will perform the stack operation push (using append()) and pop()

	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	# pushing the items into stack1 , complexity is O(1) since we are directly pushing to the stack 

	def enqueue(self,value):
		self.stack1.append(value)



	# when a dequeue function implemented using stack functions, it should follow FIFO 
	# complexity is O(n) (after ignoring the constants and taking the highest power)

	def dequeue(self):

		# checks if stack1 is empty 
		if self.isEmpty():
			print ("The queue is empty")


		else:
			lenOfStack1 = len(self.stack1) 		# saves the length of stack1 so as pop as many elements from it 
			while lenOfStack1 > 1:				# runs till there is only one left in stack1
				self.stack2.append(self.stack1.pop(lenOfStack1-1))	# pushes the elemenet from stack1 to stack2
				lenOfStack1-=1					# decreases the length counter after each iteration 

			print("The item popped : " + str(self.stack1.pop()))  # the first element entered in stack1 is left and popped off 


			# this part is for popping the elements back into stack1 from stack2
			lenOfStack2 = len(self.stack2) # saves length of stack2 as a counter to pop elements back to stack1
			while lenOfStack2 >= 1 :
				#print (lenOfStack2-1)
				self.stack1.append(self.stack2.pop(lenOfStack2-1)) # pops item at index number = (lenofStack2-1) of stack2  and pusphes 
																   # to stack1   
				lenOfStack2 -=1									   # reduces the counter by 1 after each pop 



	def peek(self):
		if self.isEmpty():
			print("the queue is empty")
		else :
			print(str(self.stack1[len(self.stack1)-1]))


	# check if stack1 is empty or not 
	def isEmpty(self):
		if len(self.stack1) == 0:
			return True 
		else :
			return False 


# main function 
qu = queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)
qu.enqueue(50)
qu.dequeue()
qu.dequeue()
qu.peek()

