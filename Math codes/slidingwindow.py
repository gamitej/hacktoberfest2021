# Sliding Window

def maxSum(arr, n, k):
	sum = -2**32
	for i in range(n - k + 1):
		current = 0
		for j in range(k):
			current_sum = current + arr[i + j]
		sum = max(current_sum, sum)
	return sum
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))

