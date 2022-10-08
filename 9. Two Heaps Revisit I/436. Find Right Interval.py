# Given an array of intervals, find the next interval of each interval.
# In a list of intervals, for an interval ‘i’ its next interval ‘j’ will have
# the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

from heapq import *


class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end


def find_next_interval(intervals):
	result = [-1 for x in intervals]

	maxStartHeap = []
	maxEndHeap = []

	for i in range(len(intervals)):
		heappush(maxStartHeap, (-intervals[i].start, i))
		heappush(maxEndHeap, (-intervals[i].end, i))

	for _ in range(len(intervals)):
		topEnd, endIndex = heappop(maxEndHeap)

		if -maxStartHeap[0][0] >= -topEnd:
			topStart, startIndex = heappop(maxStartHeap)

			while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
				topStart, startIndex = heappop(maxStartHeap)
			result[endIndex] = startIndex

			heappush(maxStartHeap, (topStart, startIndex))                             

	return result


def main():

	result = find_next_interval(
		[Interval(2, 3), Interval(3, 4), Interval(5, 6)])
	print("Next interval indices are: " + str(result))

	result = find_next_interval(
		[Interval(3, 4), Interval(1, 5), Interval(4, 6)])
	print("Next interval indices are: " + str(result))


main()

# time complexity: O(NlogN)
# space complexity: O(N)