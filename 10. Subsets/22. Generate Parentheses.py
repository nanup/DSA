# For a given number ‘N’, write a function to generate
# all combination of ‘N’ pairs of balanced parentheses.

from collections import deque


def generate_valid_parentheses(num):
	result = []

	parentheses = deque()

	parentheses.append("")

	for i in range(num):
		for _ in range(len(parentheses)):
			oldPair = parentheses.popleft()
			k = i
			while k < len(oldPair) + 1:
				newPair = list(oldPair)
				newPair.insert(k, "()")
				newPair = "".join(newPair)

				k += 1
				
				if len(newPair) == 2 * num:
					result.append(newPair)
				else:
					parentheses.append(newPair)

	return result


def main():
	print("All combinations of balanced parentheses are: " +
		  str(generate_valid_parentheses(2)))
	print("All combinations of balanced parentheses are: " +
		  str(generate_valid_parentheses(4)))


main()
