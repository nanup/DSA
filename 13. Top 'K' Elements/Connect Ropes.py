# Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost.
# The cost of connecting two ropes is equal to the sum of their lengths.
from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
	minHeap = []

	for ropeLength in ropeLengths:
		heappush(minHeap, ropeLength)

	temp, cost = 0, 0
	while len(minHeap) > 1:
		temp = heappop(minHeap) + heappop(minHeap)
		cost += temp
		heappush(minHeap, temp)

	return cost

def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()

# time complexity: O(logN)
# space complexity: o(N)