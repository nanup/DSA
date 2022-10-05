# Given an unsorted array containing numbers, find the smallest missing positive number in it.

def findFirstMissingPositive(nums):
	# first, middle, last = 0, 0, len(nums) - 1

	# while middle <= last:
	# 	if nums[first] <= 0:
	# 		nums[first], nums[last] = nums[last], nums[first]
	# 		last -= 1

	# 	if nums[first] > nums[middle]:
	# 		nums[first], nums[middle] = nums[middle], nums[first]
			
	# 	if middle == last:
	# 		first += 1
	# 		middle = first
	# 	else:
	# 		middle += 1

	first, last = 0, len(nums)

	while first < last:
		j = nums[first] - 1
		if nums[first] > 0 and nums[first] <= last and nums[first] != nums[j]:
			nums[first], nums[j] = nums[j], nums[first]
		else:
			first += 1

	for i in range(len(nums)):
		if nums[i] != i + 1:
			return i + 1

	return n + 1

def main():
	print(findFirstMissingPositive([-3, 1, 5, 4, 2]))
	print(findFirstMissingPositive([3, -2, 0, 1, 2]))
	print(findFirstMissingPositive([3, 2, 5, 1]))

main()

# time complexity: O(N)
# space complexity: O(1)