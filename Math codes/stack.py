class stack:
	def __init__(self):
		self.arr = []
		self.len = 0
	def is_empty(self):
		return self.arr == [] 
	def push(self,data):
		self.arr.append(data)
		self.len+=1 
	def pop(self):
		if self.arr!=[]:
			self.len-=1
			return self.arr.pop()
		else:
			return "stack is empty"
	def stack_top(self):
		if self.arr!=[]:
			return self.arr[-1]
		else:
			return "stack is empty"
	def stack_len(self):
		return self.len
		
s=stack()
print(" (1.) push (2.) pop (3.) is_empty (4.) top (5.) len (0.) end of opr")
while True:
	print("enter opr value :")
	op=int(input())
	if op==1:#push
		print("push data :")
		data=int(input())
		s.push(data)
	if op==2:#pop
		x=s.pop()
		print("pop value :",x)
	if op==3:#is_empty
		x=s.is_empty()
		print("status :",x)
	if op==4:#top
		x=s.stack_top()
		print("top :",x)
	if op==5:#len of stack
		x=s.stack_len()
		print("stack len :",x)
	if op==0:#end of stack opr
		break
print("end of all operations")
