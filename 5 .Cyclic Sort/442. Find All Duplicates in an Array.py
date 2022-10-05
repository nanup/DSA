# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
# The array has some duplicates, find all the duplicate numbers without using any extra space.

def findAllDuplicates(nums):
	duplicates = []

	i = 0

	while i < len(nums):
		j = nums[i]

		if j != nums[j - 1]:
			nums[i], nums[j - 1] = nums[j - 1], nums[i]
		else:
			i += 1

	for i in range(len(nums)):
		if nums[i] != i + 1:
			duplicates.append(nums[i])

	return duplicates

def main():
	print(findAllDuplicates([3, 4, 4, 5, 5]))
	print(findAllDuplicates([5, 4, 7, 2, 3, 5, 3]))

main()

# time complexity: O(N)
# space complexity: O(1)