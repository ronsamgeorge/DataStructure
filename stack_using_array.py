#this program is an implementation of stacks using arrays 
#Stacks work on the idea of LIFO - Last in first out. 


class stack():
	def __init__(self):
		self.arr = []
		self.length = 0

	def peek(self):
		if self.isEmpty():
			print ("stack is empty")
		else :
			#print(self.length)
			print (self.arr[self.length-1])


	def pop(self):
		if self.isEmpty():
			print ("stack is empty")
		else:
			print ("Popped : "  + str(self.arr[self.length-1]))
			self.length-=1
			

	def push(self,value):

		#print(self.length)		
		self.arr.insert(self.length,value)
		self.length+=1 


	def isEmpty(self):
		if self.length <= 0:
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