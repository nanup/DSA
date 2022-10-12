# Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.
from heapq import *
from math import sqrt

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance_from_origin(self):
		return (self.x * self.x) + (self.y * self.y)

	def __lt__(self, other):
		return self.distance_from_origin() < other.distance_from_origin()

	def print_point(self):
		print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
	maxHeap = []

	for i in range(k):
		point = points[i]
		heappush(maxHeap, point)

	for j in range(len(points) - k):
		point = points[j]
		if -point.distance_from_origin() > maxHeap[0].distance_from_origin():
			heappop(maxHeap)
			heappush(maxHeap, -point)

	return [point for point in maxHeap]


def main():

	result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
	print("Here are the k points closest the origin: ", end='')
	for point in result:
		point.print_point()


main()

# time complexity: o(N * logK)
# space complexity: O(K)