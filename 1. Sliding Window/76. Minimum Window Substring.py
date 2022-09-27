# Given a string and a pattern, 
# find the smallest substring in the given string 
# which has all the characters of the given pattern.

def findSubstring(str, pattern):
	charFrequency = {}

	for char in pattern:
		if char not in charFrequency:
			charFrequency[char] = 0
		charFrequency[char] += 1

	windowStart, matched = 0, 0

	start, end = 0, len(str)

	for windowEnd in range(len(str)):
		rightChar = str[windowEnd]

		if rightChar in charFrequency:
			charFrequency[rightChar] -= 1

			if charFrequency[rightChar] >= 0:
				matched += 1

		while matched == len(pattern): # since we are matching every char we use len of pattern instead of charFrequency
			if end - start > windowEnd - windowStart:
				start = windowStart
				end = windowEnd

			leftChar = str[windowStart]
			windowStart += 1
			if leftChar in charFrequency:
				if charFrequency[leftChar] == 0:
					matched -= 1
				charFrequency[leftChar] += 1

	if end - start + 1 > len(str):
		return ""
	return str[start: end + 1]		

def main():
	print(findSubstring("abdabca", "abc"))

main()

# time complexity: O(M + N)
# space complexity: O(M)