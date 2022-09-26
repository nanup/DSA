# Given a string, find the length of the longest substring in it 
# with no more than K distinct characters.

import math

def longestSubstringWithKDistinct(str, k):
	charFrequency = {}

	maxSize = -math.inf

	windowStart = 0

	for windowEnd in range(len(str)):
		rightChar = str[windowEnd]

		if rightChar not in charFrequency: # adding the rightChar to charFrequency if it doesn't already exist
			charFrequency[rightChar] = 0
		charFrequency[rightChar] += 1

		while len(charFrequency) > k:
			leftChar = str[windowStart]

			charFrequency[leftChar] -= 1 # decreasing the frequency of leftChar by one as the window is slid one step to right

			if charFrequency[leftChar] == 0:
				del charFrequency[leftChar] # removing the leftChar when its frequency becomes zero

			windowStart += 1

		maxSize = max(windowEnd - windowStart + 1, maxSize)

	return maxSize

def main():
	print("Length of longest substring: " + str(longestSubstringWithKDistinct("araaci", 2)))

main()