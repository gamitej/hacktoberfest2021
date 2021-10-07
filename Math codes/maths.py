"""this file contain 
prime,factors and prime factor
using diviser method and sieve """ 
------------------------------------------------------
#prime number in given range T.C-->O(sqrt(n))
import math
def prime(n):
	if n<=1:
		return False
	if n==2:	
		return True
	if n>2 and n%2==0:
		return False
	maxi=int(math.sqrt(n))+1
	for i in range(3,maxi,2):
		if n%i==0:
			return False
	return True
l=[2]
x,y=map(int,input().split())
for i in range(x,y+1):
	if prime(i):
		l.append(i)
print(*l)
----------------------------------------------------------
#number is prime or not T.C-->O(sqrt(n))
import math
def prime(n):
	if n<=1:
		return False
	if n==2:	
		return True
	if n>2 and n%2==0:
		return False
	maxi=int(math.sqrt(n))+1
	for i in range(3,maxi,2):
		if n%i==0:
			return False
	return True
n=int(input())
print(prime(n))
----------------------------------------------------------
#prime factor of a given  number
import math
n=int(input())
l=[]
#total no divisible by even
while n%2==0:
	l.append(2)
	n=n//2
# n reduces to become odd
for i in range(3,int(math.sqrt(n))+1,2):
	# till i divides n
	while n%i==0:
		l.append(i)
		n=n//i
#if final n value is prime
if n>2:
	l.append(n)
print(*l)
---------------------------------------------------------
#Sieve of Eratosthenes for Prime No. T.C-->n*log(log n)
def SOE(n): 
    p=[True]*(n+1) 
    i=2
    while(i*i <= n): 
        if p[i] == True:      
            for j in range(i*i,n+1,i):
                p[j] = False
        i+=1
    l=[]
    for i in range(2,n): 
        if p[i]: 
            l.append(i)
    return l
x=SOE(100)
print(*x) 
---------------------------------------------------------
#prime factor by sieve
# Time Complexity : O(logn) 
import math
def sieve(n): 
	prime = [0]*(n+1) 
	prime[1] = 1
	for i in range(2,n):  
		prime[i] = i  
	for i in range(2,int(math.sqrt(n))+1): 
		if prime[i] == i: 
			for j in range(i*i,n,i):      
				if prime[j] == j: 
					prime[j] = i 
	return prime


print("Set high limit::")
maxi=int(input())
prime=sieve(maxi)
# A O(log n) function returning prime 
l=[] 
print("enter val of which you want prime fact:")
x=int(input())
while x!=1: 
	l.append(prime[x]) 
	x=x//prime[x] 
print(*l)
---------------------------------------------------------
# factor in O(sqrt(n))
# factor of a number in O(sqrt(n))
import math
def factor(n):
	l1,l2=[],[]
	for i in range(1,int(math.sqrt(n))+1):
		if n%i==0:
			#if divisor are equal take only one
			if n//i==i:
				l1.append(i)
			else:
				l1.append(i)
				l2.append(n//i)
	l=l1+l2[::-1]
	return l
n=int(input())
print(factor(n))
-----------------------------------------------------------
""" KYA BAAT HAI :) """
