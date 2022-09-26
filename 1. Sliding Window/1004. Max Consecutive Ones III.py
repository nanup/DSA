# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
# find the length of the longest contiguous subarray having all 1s.

def lengthOfLongestSubstring(arr, k):
	windowStart = 0

	maxLength = 0

	zeroCount = 0

	for windowEnd in range(len(arr)):
		rightChar = arr[windowEnd]

		if rightChar == 0:
			zeroCount += 1

		while zeroCount > k:
			leftChar = arr[windowStart]

			if leftChar == 0:
				zeroCount -= 1

			windowStart += 1

		maxLength = max(maxLength, windowEnd - windowStart + 1)

	return maxLength

def main():
	print(lengthOfLongestSubstring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))

main()

# time complexity: O(N)
# space complexity: O(1)