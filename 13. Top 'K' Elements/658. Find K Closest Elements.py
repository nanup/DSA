# Given a sorted number array and two integers ‘K’ and ‘X’,
# find ‘K’ closest numbers to ‘X’ in the array.
# Return the numbers in the sorted order.
# ‘X’ is not necessarily present in the array.
from heapq import *

def find_closest_elements(arr, K, X):
	index = binarySearch(arr, X)

	low, high = index - K, index + K
	low = max(low, 0)
	high = min(high, len(arr) - 1)

	minHeap = []

	for i in range(low, high + 1):
		heappush(minHeap, (abs(arr[i] - X), arr[i]))

	result = []
	for _ in range(K):
		result.append(heappop(minHeap)[1])

	result.sort()
	return result

def binarySearch(arr, target):
	start, end = 0, len(arr) - 1

	while start <= end:
		mid = (end + start) // 2

		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			end = mid - 1
		else:
			start = mid + 1

	if end > 0:
		end -= 1

	return end


def main():
	print("'K' closest numbers to 'X' are: " +
		  str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
	print("'K' closest numbers to 'X' are: " +
		  str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
	print("'K' closest numbers to 'X' are: " +
		  str(find_closest_elements([0,0,1,2,3,3,4,7,7,8], 3, 5)))


main()

# time complexity: O(N*logK + K*logK)
# space complexity: O(K)