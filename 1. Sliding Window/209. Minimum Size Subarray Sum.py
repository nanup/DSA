# Given an array of positive numbers and a positive number ‘S’, 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
# Return 0, if no such subarray exists.

import math

def smallestSubarrayWithGivenSum(s, arr):
	minSize = math.inf

	windowStart, windowSum = 0, 0

	for windowEnd in range(len(arr)):
		windowSum += arr[windowEnd] # adds the new end element to the windowSum

		while windowSum >= s: # 'while' used to make sure the window is shrinked as much as possible
			minSize = min(windowEnd - windowStart + 1, minSize)

			windowSum -= arr[windowStart] # subtracts the start element from the windowSum
			windowStart += 1 # slides the window one element ahead at windowStart

	if minSize == math.inf:
		return 0
	else:
		return minSize

def main():
	print("Smallest subarray length: " + str(smallestSubarrayWithGivenSum(7, [2, 1, 5, 2, 3, 2])))
	print("Smallest subarray length: " + str(smallestSubarrayWithGivenSum(7, [2, 1, 5, 2, 8])))
	print("Smallest subarray length: " + str(smallestSubarrayWithGivenSum(8, [3, 4, 1, 1, 6])))

main()

# time complexity: O(N)
# space complexity: O(1)