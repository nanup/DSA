# Given a string with lowercase letters only, 
# if you are allowed to replace no more than ‘k’ letters with any letter, 
# find the length of the longest substring having the same letters after replacement.

def lengthOfLongestSubstring(str, k):
	charFrequency = {}

	maxLength = 0

	windowStart = 0

	for windowEnd in range(len(str)):
		rightChar = str[windowEnd]

		if rightChar not in charFrequency:
			charFrequency[rightChar] = 0

		charFrequency[rightChar] += 1

		while len(charFrequency) > 2 or charFrequency[rightChar] > k:
			rightChar = str[windowStart]

			charFrequency[rightChar] -= 1

			if charFrequency[rightChar] == 0:
				del charFrequency[rightChar]

			windowStart += 1

			if len(charFrequency) == 1:
				break

		maxLength = max(maxLength, windowEnd - windowStart + 1)

	return maxLength

def main():
	print(lengthOfLongestSubstring("aabccbb", 2))

main()
