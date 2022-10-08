# Given a set of investment projects with their respective profits,
# we need to find the most profitable projects.
# We are given an initial capital and are allowed to invest only in a fixed number of projects.
# Our goal is to choose projects that give us the maximum profit.

from heapq import *


def find_maximum_capital(capitals, profits, numberOfProjects, initialCapital):
	minCapitalHeap = []
	maxProfitHeap = []

	for i, capital in enumerate(capitals):
		heappush(minCapitalHeap, (capital, i))

	availableCapital = initialCapital

	for _ in range(numberOfProjects):
		while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
			i = heappop(minCapitalHeap)[1]
			heappush(maxProfitHeap, (-profits[i], i))

		availableCapital += -heappop(maxProfitHeap)[0]

	return availableCapital


def main():

	print("Maximum capital: " +
		  str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
	print("Maximum capital: " +
		  str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()

# time complexity: O(NlogN + KlogN)
# space complexity: O(N)