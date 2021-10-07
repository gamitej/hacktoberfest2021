class Queue:
	def __init__(self):
		self.arr = []
		self.len = 0
	def is_empty(self):
		return self.arr == [] 
	def queue(self,data):
		self.arr.append(data)
		self.len+=1 
	def dequeue(self):
		if self.len!=0:
			self.len-=1
			return self.arr.pop(0)
		else:
			return "queue is empty"
	def queue_len(self):
		return self.len
		
q=Queue()
print(" (1.) push (2.) pop (3.) is_empty (4.) len (0.) end opr ")
while True:
	print("enter opr value :")
	op=int(input())
	if op==1:#push
		print("push data :")
		data=int(input())
		q.queue(data)
	if op==2:#pop
		x=q.dequeue()
		print("pop value :",x)
	if op==3:#is_empty
		x=q.is_empty()
		print("status :",x)
	if op==4:#len of stack
		x=q.queue_len()
		print("stack len :",x)
	if op==0:#end of stack opr
		break
print("end of all operations")
