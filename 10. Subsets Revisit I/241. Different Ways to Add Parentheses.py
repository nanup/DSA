def diff_ways_to_evaluate_expression(input):
	result = []

	if "+" not in input and "-" not in input and "*" not in input:
		result.append(int(input))

	else:
		for i in range(len(input)):
			char = input[i]

			if not char.isdigit():
				leftParts = diff_ways_to_evaluate_expression(input[:i])
				rightParts = diff_ways_to_evaluate_expression(input[i + 1:])

				for part1 in leftParts:
					for part2 in rightParts:
						if char == "+":
							result.append(part1 + part2)
						if char == "-":
							result.append(part1 - part2)
						if char == "*":
							result.append(part1 * part2)

	return result


def main():
	print("Expression evaluations: " +
		  str(diff_ways_to_evaluate_expression("1+2*3")))

	print("Expression evaluations: " +
		  str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()

# time complexity: O(N * 2^N)
# space complexity: O(N * 2^N)