# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
# The array originally contained all the numbers from 1 to ‘n’, 
# but due to a data error, one of the numbers got duplicated 
# which also resulted in one number going missing. Find both these numbers.

def findCorruptPair(nums):
	i = 0

	while i < len(nums):
		j = nums[i]

		if j != nums[j - 1]:
			nums[i], nums[j - 1] = nums[j - 1], nums[i]
		else:
			i += 1

	for i in range(len(nums)):
		if nums[i] != i + 1:
			return [nums[i], i + 1]

def main():
	print(findCorruptPair([3, 1, 2, 3, 6, 4]))
	print(findCorruptPair([3, 1, 2, 5, 2]))

main()

# time complexity: O(N)
# space complexity: O(1)