# Given a string, find the length of the longest substring 
# which has no repeating characters.

def nonRepeatSubstring(str):
	charFrequency = {}

	maxLength = 0

	windowStart = 0

	for windowEnd in range(len(str)):
		rightChar = str[windowEnd]

		if rightChar not in charFrequency:
			charFrequency[rightChar] = 0
		
		charFrequency[rightChar] += 1

		while charFrequency[rightChar] > 1:
			charFrequency[rightChar] -= 1

			if charFrequency[rightChar] == 0:
				del charFrequency[rightChar]

			windowStart += 1

		maxLength = max(windowEnd - windowStart + 1, maxLength)

	return maxLength

def main():
	print("length of the longest substring: " + str(nonRepeatSubstring("aabccbb")))

main()

# time complexity: O(N)
# space complexity: O(K)