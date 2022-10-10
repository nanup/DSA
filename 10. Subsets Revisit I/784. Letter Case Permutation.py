# Given a string, find all of its permutations preserving the character sequence but changing case.

def find_letter_case_string_permutations(str):
	permutations = []

	# permutations.append(str)

	# for i in range(len(str)):
	# 	for j in range(len(permutations)):
	# 		permutation = list(permutations[j])
	# 		if permutation[i].isalpha():
	# 			permutation[i] = permutation[i].swapcase()
	# 			permutations.append("".join(permutation))

	# return permutations

	permutation = []

	def permute(i):
		if i == len(str):
			permutations.append("".join(permutation.copy()))
			return

		char = str[i]

		permutation.append(char)
		permute(i + 1)

		if char.isalpha():
			for i in range(len(str) - i):
				permutation.pop()
			permutation.append(char.swapcase())
			permute(i + 1)
			
	permute(0)

	return permutations
		

def main():
	print("String permutations are: " +
		  str(find_letter_case_string_permutations("ab")))
	# print("String permutations are: " +
	# 	  str(find_letter_case_string_permutations("ab7c")))


main()

# time complexity: O(N * 2 ^ N)
# space complexity: O(N * 2 ^ N)

