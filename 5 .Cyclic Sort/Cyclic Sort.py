# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return in-place sorted array

def cyclicSort(nums):
	i = 0

	while i < len(nums):
		if nums[i] != i + 1:
			num = nums[i]
			nums[i], nums[num - 1] = nums[num - 1], nums[i]
		else:
			i += 1

	return nums

def main():
	print(cyclicSort([3, 1, 5, 4, 2]))
	print(cyclicSort([2, 6, 4, 3, 1, 5]))
	print(cyclicSort([1, 5, 6, 4, 3, 2]))

main()

# time complexity: O(N)
# space complexity: O(1)