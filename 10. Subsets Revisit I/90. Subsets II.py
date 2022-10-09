# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

def find_subsets(nums):
	nums.sort()
	subsets = []

	# subsets.append([])
	# startIndex = 0
	
	# for i in range(len(nums)):
	# 	if i > 0 and nums[i] == nums[i - 1]:
	# 		startIndex = endIndex
	# 	endIndex = len(subsets)
	# 	for j in range(startIndex, endIndex):
	# 		subset = list(subsets[j])
	# 		subset.append(nums[i])
	# 		subsets.append(subset)

	subset = []

	def dfs(i):
		if i >= len(nums):
			subsets.append(subset.copy())
			return

		subset.append(nums[i])
		dfs(i + 1)

		subset.pop()
		if subset and subset[-1] == nums[i]:
			return
		dfs(i + 1)

	dfs(0)

	return subsets


def main():

	print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
	print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()

# time complexity: O(2 ^ N)
# space complexity: O(2 ^ N)

# time complexity: O(N log N)
# space complexity: O(N)