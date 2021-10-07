#Merge Sort
def merge(l,r):
	ans=[]
	i=j=0
	while i<len(l) and j<len(r):
		if l[i]< r[j]:
			ans.append(l[i])
			i+=1
		else:
			ans.append(r[j])
			j+=1
	ans+=l[i:]
	ans+=r[j:]
	return ans
def ms(ar):
	if len(ar)<=1:
		return ar
	m=len(ar)//2
	l=ms(ar[:m])
	r=ms(ar[m:])
	return merge(l,r)
ar=[0,11,13,1,3,2,4,5]
print(ms(ar))
-----------------------------------------
# quick sort

def partition(arr, low, high):
	i = (low-1)		
	pivot = arr[high]	 
	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

arr = [5,4,3,2,1]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
	print("%d" % arr[i]),

-----------------------------------------
#insertion sort
a=[4,3,2,1]
n=len(a)
for i in range(1,n):
	x=a[i]
	j=i-1
	while j>-1 and x<a[j]:
		a[j+1]=a[j]
		j-=1
	a[j+1]=x
print(a)
-----------------------------------------
#bubble sort
a=[4,3,2,1]
n=len(a)
for i in range(n-1):
	for j in range(1,n-i):
		if a[j-1]>a[j]:
			a[j-1],a[j]=a[j],a[j-1]
print(a)
-----------------------------------------
#selection sort
a=[4,3,2,1]
n=len(a)
for i in range(n):
	x=i
	for j in range(i+1,n):
		if a[x]>a[j]:
			x=j
	a[i],a[x]=a[x],a[i]
print(a)
-----------------------------------------
