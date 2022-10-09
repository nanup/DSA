# Given a set of distinct numbers, find all of its permutations.

from collections import deque


def find_permutations(nums):
	result = []

	# permutations = deque()
	# permutations.append([])

	# for i in range(len(nums)):
	# 	for _ in range(len(permutations)):
	# 		permutation = permutations.popleft()
	# 		for j in range(len(permutation) + 1):
	# 			newPermutation = list(permutation)
	# 			newPermutation.insert(j, nums[i])

	# 			if len(newPermutation) == len(nums):
	# 				result.append(newPermutation)
	# 			else:
	# 				permutations.append(newPermutation)

	# if len(nums) == 1:
	# 	return [nums.copy()]

	# for i in range(len(nums)):
	# 	n = nums.pop(0)
	# 	perms = find_permutations(nums)
	# 	for perm in perms:
	# 		perm.append(n)
	# 	result.extend(perms)
	# 	nums.append(n)

	return result


def main():
	print("Here are all the permutations: " +
		  str(find_permutations([1, 3, 5])))


main()

# time complexity: O(N * N!)
# space complexity: O(N * N!)

# time complexity: O()
# space complexity: O(N!)