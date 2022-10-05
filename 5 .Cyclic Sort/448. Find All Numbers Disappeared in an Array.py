# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
# The array can have duplicates, which means some numbers will be missing. 
# Find all those missing numbers.

def findMissingNumbers(nums):
	missingNumbers = []
	 
	i = 0

	while i < len(nums):
		j = nums[i]

		if j != nums[j - 1]:
			nums[i], nums[j - 1] = nums[j - 1], nums[i]
		else:
			i += 1

	for i in range(len(nums)):
		if nums[i] != i + 1:
			missingNumbers.append(i + 1)

	return missingNumbers

def main():
	print(findMissingNumbers([2, 4, 1, 2]))
	print(findMissingNumbers([2, 3, 2, 1]))
	print(findMissingNumbers([2, 3, 1, 8, 2, 3, 5, 1]))

main()

# time complexity: O(N)
# space complexity: O(1)