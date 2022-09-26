# Given a string with lowercase letters only, 
# if you are allowed to replace no more than ‘k’ letters with any letter, 
# find the length of the longest substring having the same letters after replacement.

def lengthOfLongestSubstring(str, k):
	maxLength, maxRepeat = 0, 0

	charFrequency = {}

	windowStart = 0

	for windowEnd in range(len(str)):
		rightChar = str[windowEnd]

		if rightChar not in charFrequency:
			charFrequency[rightChar] = 0

		charFrequency[rightChar] += 1

		maxRepeat = max(maxRepeat, charFrequency[rightChar])

		# maxRepeat tracks the count of max repeating char
		# that implies all other elements of subarray less than
		# maxRepeat should be replaced and hence, less than k in number

		if windowEnd - windowStart + 1 - maxRepeat > k:
			leftChar = str[windowStart]

			charFrequency[leftChar] -= 1

			windowStart += 1

		maxLength = max(maxLength, windowEnd - windowStart + 1)

	return maxLength
 
def main():
	print(lengthOfLongestSubstring("aabccbb", 2))

main()
