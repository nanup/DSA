# Given a set with distinct elements, find all of its distinct subsets.

from heapq import *

def find_subsets(nums):
	# result = []
	# result.append([])

	# for i in range(len(nums)):
	# 	for j in range(len(result)):
	# 		subset = list(result[j])
	# 		subset.append(nums[i])
	# 		result.append(subset)

	# return result

	# alternate solution
	result = []
	subset = []

	def findSubsets(i):
		if i >= len(nums):
			result.append(subset.copy())
			return

		subset.append(nums[i])
		findSubsets(i + 1)

		subset.pop()
		findSubsets(i + 1)

	findSubsets(0)

	return result

def main():

	print("Here is the list of subsets: " + str(find_subsets([1, 3])))
	print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()

# time complexity: O(2 ^ N)
# space complexity: O(2 ^ N)

# time complexity: O(N)
# space complexity: O(N)