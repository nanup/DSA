# Given an infinite sorted array (or an array with unknown size),
# find if a given number ‘key’ is present in the array.
# Write a function to return the index of the ‘key’
# if it is present in the array, otherwise return -1.

import math


class ArrayReader:

	def __init__(self, arr):
		self.arr = arr

	def get(self, index):
		if index >= len(self.arr):
			return math.inf
		return self.arr[index]


def search_in_infinite_array(reader, key):
	start, end = 0, 1

	while key > reader.get(end):
		newStart = end + 1
		end += (end - start + 1) * 2
		start = newStart

	while start <= end:
		mid = (end + start) // 2

		if reader.get(mid) == key:
			return mid
		elif reader.get(mid) < key:
			start = mid + 1
		else:
			end = mid - 1

	return -1


def main():
	reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
	print(search_in_infinite_array(reader, 16))
	print(search_in_infinite_array(reader, 11))
	reader = ArrayReader([1, 3, 8, 10, 15])
	print(search_in_infinite_array(reader, 15))
	print(search_in_infinite_array(reader, 200))


main()

# time complexity: O(log N)
# space complexity: O(1)