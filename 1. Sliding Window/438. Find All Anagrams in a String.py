# Given a string and a pattern, 
# find all anagrams of the pattern in the given string.

def findStringAnagrams(str, pattern):
	charFrequency = {}

	for char in pattern:
		if char not in charFrequency:
			charFrequency[char] = 0
		charFrequency[char] += 1

	result = []

	windowStart, matched = 0, 0

	for windowEnd in range(len(str)):
		rightChar = str[windowEnd]

		if rightChar in charFrequency:
			charFrequency[rightChar] -= 1

			if charFrequency[rightChar] == 0:
				matched += 1

		if matched == len(charFrequency):
			result.append(windowStart)

		if windowEnd - windowStart + 1 >= len(pattern):
			rightChar = str[windowStart]
			windowStart += 1

			if rightChar in charFrequency:
				if charFrequency[rightChar] == 0:
					matched -= 1

				charFrequency[rightChar] += 1

	return result

def main():
	print(findStringAnagrams("abbcabc", "abc"))
	print(findStringAnagrams("ppqp", "pq"))

main()

# time complexity: O(M + N)
# space complexity: O(M)