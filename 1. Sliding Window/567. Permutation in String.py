# Given a string and a pattern,
# find out if the string contains any permutation of the pattern.
def findPermutation(str, pattern):
    patternDict = {}

    for char in pattern:
        if char not in patternDict:
            patternDict[char] = 0

        patternDict[char] += 1

    windowStart = 0

    matched = 0

    for windowEnd in range(len(str)):
        rightChar = str[windowEnd]

        if rightChar in patternDict:
            patternDict[rightChar] -= 1

            if patternDict[rightChar] == 0:
                matched += 1

        if matched == len(patternDict):
            return True

        # If the window size is greater than the length of the pattern, 
		# shrink the window to make it equal to the size of the pattern. 
		# At the same time, if the character going out was part of the pattern, 
		# put it back in the frequency HashMap.

        if windowEnd - windowStart + 1 >= len(pattern): # equals because the comparision for the pattern lengthed subarray is already done
			# and next step adds a new windowEnd and so windowStart should already move ahead by one
            leftChar = str[windowStart]
            windowStart += 1

            if leftChar in patternDict:
                if patternDict[leftChar] == 0:
                    matched -= 1
                patternDict[leftChar] += 1

    return False


def main():
    print("Permutation exist: " + str(findPermutation(("oidbcaf"), "abc")))
    print("Permutation exist: " + str(findPermutation(("odicf"), "dc")))
    print("Permutation exist: " + str(findPermutation(("bcdxabcdy"), "bcdyabcdx")))
    print("Permutation exist: " + str(findPermutation(("aaacb"), "abc")))


main()

# time complexity: O(N + M)
# space complexity: O(M)