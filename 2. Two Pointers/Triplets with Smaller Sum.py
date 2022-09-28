# Given an array arr of unsorted numbers and a target sum, 
# count all triplets in it such that 
# arr[i] + arr[j] + arr[k] < target where 
# i, j, and k are three different indices. 
# Write a function to return the count of such triplets.

def tripletWithSmallerSum(arr, target):
	result = 0

	arr.sort()

	for i in range(len(arr)):
		if i > 0 and arr[i - 1] == arr[i]:
			continue

		left, right = i + 1, len(arr) - 1

		while left < right:
			currentSum = arr[i] + arr[left] + arr[right]

			if currentSum < target:
				result += right - left

				left += 1
			else:
				right -= 1

	return result

def main():
	print(tripletWithSmallerSum([-1, 0, 2, 3], 3))
	print(tripletWithSmallerSum([-1, 4, 2, 1, 3], 5))

main()

# time complexity: O(N^2)
# space complexity: O(N)