# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers
# from the array such that we are left with maximum distinct numbers.
from heapq import *

def find_maximum_distinct_elements(nums, k):
	# error handling
	distinctElementsCount = 0
	if len(nums) <= k:
		return distinctElementsCount

	# creating number frequency
	numFreq = {}
	for num in nums:
		numFreq[num] = numFreq.get(num, 0) + 1

	# creating minimum heap
	minHeap = []
	for num, count in numFreq.items():
		# push only numbers with duplicates
		if count == 1:
			distinctElementsCount += 1
		else:
			heappush(minHeap, [count, num])

	while k > 0 and minHeap:
		count, num = heappop(minHeap)
		k -= count - 1
		if k >= 0:
			distinctElementsCount += 1

	if k > 0:
		distinctElementsCount -= k

	return distinctElementsCount


def main():

	print("Maximum distinct numbers after removing K numbers: " +
		  str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
	print("Maximum distinct numbers after removing K numbers: " +
		  str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
	print("Maximum distinct numbers after removing K numbers: " +
		  str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()

# time complexity: O(N*logN + K*logN)
# space complexity: O(N)