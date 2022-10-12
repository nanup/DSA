# Given an unsorted array of numbers,

# find the top ‘K’ frequently occurring numbers in it.

from heapq import *


def find_k_frequent_numbers(nums, k):

	topNumbers = []

	minHeap = []

	hashMap = {}
	for num in nums:

		if num not in hashMap:
			hashMap[num] = 0
		hashMap[num] += 1


	for num, count in hashMap.items():
		heappush(minHeap, (count, num))
		if len(minHeap) > k:
			heappop(minHeap)

	while minHeap:
		topNumbers.append(heappop(minHeap)[1])
	return topNumbers


def main():


	print("Here are the K frequent numbers: " +

		  str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))


	print("Here are the K frequent numbers: " +

		  str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

# time complexity: O(N + NlogK)
# space complexity: O(N)