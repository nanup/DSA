# Given an array of characters where each character represents a fruit tree, 
# you are given two baskets and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.

# same as longest k unique characters substring

import math

def fruitsIntoBasket(fruits):
	dict = {}

	maxFruits = -math.inf

	windowStart = 0

	for windowEnd in range(len(fruits)):
		rightChar = fruits[windowEnd]

		if rightChar not in dict:
			dict[rightChar] = 0

		dict[rightChar] += 1

		while len(dict) > 2:
			leftChar = fruits[windowStart]

			dict[leftChar] -= 1

			if dict[leftChar] == 0:
				del dict[leftChar]

			windowStart += 1

		maxFruits = max(windowEnd - windowStart + 1, maxFruits)

	return maxFruits

def main():
	print("Maximum number of fruits: " + str(fruitsIntoBasket(["A", "B", "C", "A", "C"])))

main()

# time complexity: O(N)
# space complexity; O(K)