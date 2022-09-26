# Given an array of positive numbers and a positive number ‘k’, 
# find the maximum sum of any contiguous subarray of size ‘k’.
import math

def maxSubArrayOfSizeK(k, arr):
	maxSum = -math.inf

	windowStart, windowSum = 0, 0

	for windowEnd in range(len(arr)):
		windowSum += arr[windowEnd] # adds the new end element to the windowSum

		if windowEnd >= (k - 1):
			maxSum = max(windowSum, maxSum)

			windowSum -= arr[windowStart] # subtracts the start element from the windowSum
			windowStart += 1 # slides the window one element ahead at windowStart

	return maxSum

def main():
	print("Maximum sum of subarray of size K: " + str(maxSubArrayOfSizeK(3, [2, 1, 5, 1, 3, 2])))

main()

# time complexity: O(N)
# space complexity: O(1)