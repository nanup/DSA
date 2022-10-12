# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

from heapq import *


def find_k_largest_numbers(nums, k):
	# result = []
	
	# maxHeap = []

	# for num in nums:
	# 	heappush(maxHeap, -num)

	# while k > 0:
	# 	result.append(-heappop(maxHeap))
	# 	k -= 1

	# return result

	minHeap = []

	for i in range(k):
		heappush(minHeap, nums[i])

	for j in range(k, len(nums)):
		if nums[j] > minHeap[0]:
			heappop(minHeap)
			heappush(minHeap, nums[j])

	return list(minHeap)


def main():

	print("Here are the top K numbers: " +
		  str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

	print("Here are the top K numbers: " +
		  str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()

# time complexity: O(NlogN + KlogK)
# space complexity: O(N + K)

# time complexity: O(NlogK)
# space complexity: O(K)