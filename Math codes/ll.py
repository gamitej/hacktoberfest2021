class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class ll:
	def  __init__(self):
		self.len=0
		self.head=None
	# insert at start
	def ins1(self,data):
		x=node(data)
		self.len+=1
		if self.head is None:
			self.head=x
		else:
			x.next=self.head
			self.head=x
	# insert at end
	def ins2(self,data):
		x=node(data)
		self.len+=1
		temp=self.head
		while (temp.next):
			temp=temp.next
		temp.next=x
	# insert at given point
	def ins3(self,data,data1):
		x=node(data)
		self.len+=1
		temp=self.head
		while (temp.data!=data1):
			temp=temp.next
		y=temp.next
		temp.next=x
		x.next=y
	# delete from front
	def del1(self):
		self.len-=1
		self.head=self.head.next
	# delete given node value
	def del2(self,data):
		self.len-=1
		curr=self.head
		prev=None
		while curr.data!=data:
			prev=curr
			curr=curr.next
		prev.next=curr.next
	# delete a given position node
	def del3(self,x):
		if x==0:
			self.head=self.head.next
			return
		c=0
		self.len-=1
		prev=None
		curr=self.head
		while curr!=None and c!=x:
			prev=curr
			curr=curr.next
			c+=1
		prev.next=curr.next
	#reverse the linkedlist
	def rev(self):
		curr=self.head
		prev,x=None,None
		while curr:
			x=curr.next
			curr.next=prev
			prev=curr
			curr=x
		self.head=prev
	# mid of linked-list using two pointer
	def mid(self):
		f=c=self.head
		while f!=None and f.next!=None:
			c=c.next
			f=f.next.next
		return c.data
	def len(self):
		return self.len
	def trav(self,l):
		temp=self.head
		while (temp):
			l.append(temp.data)
			temp=temp.next
		return l
""" ins1->to insert at start 
	ins2->to insert at end	
	ins3->to insert after given node"""
l=ll()
l.ins1(12)
l.ins1(44)
print(l.trav([]),"1")
l.ins2("Amisha")
l.ins1(34)
l.ins1(2) 
print(l.trav([]),"2")
l.ins2("Tiwari")
print(l.trav([]),"3")
l.ins3("Amrita","Amisha")
print(l.trav([]),"4")
l.rev()
print(l.trav([]),"reversed ll")
l.del2(12)
l.rev()
l.del2("Tiwari")
print(l.trav([]),"5")
l.ins3("Tiwari","Amisha")
l.ins3("Tiwari","Amrita")
print(l.trav([]),"6")
l.del3(0)
print(l.trav([]),"7")
l.del3(3)
print(l.trav([]),"8")
print("Middle value is : ",l.mid())














