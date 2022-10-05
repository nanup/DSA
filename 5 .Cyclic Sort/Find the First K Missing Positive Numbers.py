# Given an unsorted array containing numbers and a number ‘k’,
# find the first ‘k’ missing positive numbers in the array.

def findFirstKMissingPositive(nums, k):
	missingNumbers = []

	i, n = 0, len(nums)

	while i < n:
		j = nums[i]

		if j > 0 and j <= n and j != nums[j - 1]:
			nums[i], nums[j - 1] = nums[j - 1], nums[i]
		else:
			i += 1

	for i in range(len(nums)):
		if nums[i] != i + 1:
			missingNumbers.append(i + 1)

			if len(missingNumbers) == k:
				return missingNumbers

	n = max(nums) + 1

	while len(missingNumbers) < k:
		missingNumbers.append(n)
		n += 1

	return missingNumbers


def main():
	print(findFirstKMissingPositive([3, -1, 4, 5, 5], 3))
	print(findFirstKMissingPositive([2, 3, 4], 3))
	print(findFirstKMissingPositive([-2, -3, 4], 2))


main()

# time complexity: O(N)
# space complexity: O(K)