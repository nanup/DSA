# For a given number ‘N’, write a function to generate
# all combination of ‘N’ pairs of balanced parentheses.
# from collections import deque


# class ParenthesesString():
# 	def __init__(self, str, openCount, closeCount):
# 		self.str = str
# 		self.openCount = openCount
# 		self.closeCount = closeCount


def generate_valid_parentheses(num):
	result = []

	string = [0 for x in range(2 * num)]

	def recurse(openCount, closeCount, index, string):
		if openCount == num and closeCount == num:
			result.append("".join(string))
			return
		else:
			if openCount < num:
				string[index] = "("
				recurse(openCount + 1, closeCount, index + 1, string)
			if closeCount < openCount:
				string[index] = ")"
				recurse(openCount, closeCount + 1, index + 1, string)

	recurse(0, 0, 0, string)

	return result

	# queue = deque()
	# queue.append(ParenthesesString("", 0, 0))

	# while queue:
	# 	ps = queue.popleft()
	# 	if ps.openCount == num and ps.closeCount == num:
	# 		result.append(ps.str)

	# 	else:
	# 		if ps.openCount < num:
	# 			queue.append(ParenthesesString(ps.str + "(", ps.openCount + 1, ps.closeCount))
	# 		if ps.openCount > ps.closeCount:
	# 			queue.append(ParenthesesString(ps.str + ")", ps.openCount, ps.closeCount + 1))

def main():
	print("All combinations of balanced parentheses are: " +
		  str(generate_valid_parentheses(1)))
	print("All combinations of balanced parentheses are: " +
		  str(generate_valid_parentheses(3)))


main()

# time complexity: O(N * 2 ^ N)
# space complexity: O(N * 2 ^ N)
