# Given an array of intervals, find the next interval of each interval.
# In a list of intervals, for an interval ‘i’ its next interval ‘j’ will have
# the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

# Write a function to return an array containing indices of the next interval of each input interval.
# If there is no next interval of a given interval, return -1.
# It is given that none of the intervals have the same start point.

from heapq import *

class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end


def find_next_interval(intervals):
	result = []
	
	minStartHeap = []

	for i in range(len(intervals)):
		heappush(minStartHeap, (intervals[i].start, i))

	for i in range(len(intervals)):
		if minStartHeap:
			while minStartHeap:
				start, index = heappop(minStartHeap)
				if intervals[i].end <= start and i < index:
					result.append(index)
		else:
			result.append(-1)

	return result


def main():

	result = find_next_interval(
		[Interval(2, 3), Interval(3, 4), Interval(5, 6)])
	print("Next interval indices are: " + str(result))

	result = find_next_interval(
		[Interval(3, 4), Interval(1, 5), Interval(4, 6)])
	print("Next interval indices are: " + str(result))


main()
