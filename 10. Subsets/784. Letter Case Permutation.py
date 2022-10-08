# Given a string,
# find all of its permutations preserving the character sequence but changing case.

from collections import deque

def find_letter_case_string_permutations(str):
	permutations = []
	permutations.append(str)

	for i in range(len(str)):
		if str[i].isalpha():
			for j in range(len(permutations)):
				chs = list(permutations[j])
				chs[i] = chs[i].swapcase()
				permutations.append("".join(chs))

	return permutations		

def main():
	print("String permutations are: " +
		  str(find_letter_case_string_permutations("ad52")))
	print("String permutations are: " +
		  str(find_letter_case_string_permutations("ab7c")))


main()

# time complexity: O(N * 2 ^ N)
# space complexity: O(N * 2 ^ N)
