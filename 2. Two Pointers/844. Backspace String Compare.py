# Given two strings containing backspaces (identified by the character ‘#’), 
# check if the two strings are equal.

def backspaceCompare(str1, str2):
	firstIndex, secondIndex = len(str1) - 1, len(str2) - 1

	while firstIndex >= 0 or secondIndex >= 0:

		firstIndex = nextChar(str1, firstIndex)
		secondIndex = nextChar(str2, secondIndex)

		if firstIndex < 0 and secondIndex < 0:
			return True

		if firstIndex < 0 or secondIndex < 0:
			return False

		if str1[firstIndex] != str2[secondIndex]:
			return False

		firstIndex -= 1
		secondIndex -= 1
	
	return True

def nextChar(str, index):
	count = 0

	while index >= 0:
		if str[index] == "#":
			count += 1
		elif count > 0:
			count -= 1
		else:
			break

		index -= 1

	return index

def main():
	print(backspaceCompare("xy#z", "xzz#"))
	print(backspaceCompare("xy#z", "xyz#"))
	print(backspaceCompare("a#b#", ""))

main()

# time complexity: O(M + N)
# space complexity: O(1)