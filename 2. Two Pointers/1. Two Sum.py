# Given an array of sorted numbers and a target sum, 
# find a pair in the array whose sum is equal to the given target.

def pairWithTargetSum(arr, targetSum):
	left, right = 0, len(arr) - 1

	while left < right:
		currentSum = arr[left] + arr[right]

		if currentSum == targetSum:
			return [left, right]

		if currentSum < targetSum:
			left += 1

		if currentSum > targetSum:
			right -= 1

	return []

def main():
	print(pairWithTargetSum([1, 2, 3, 4, 6], 6))

main()

# time complexity: O(N)
# space complexity: O(1)