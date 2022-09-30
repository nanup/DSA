# Given two lists of intervals, find the intersection of these two lists.
# Each list consists of disjoint intervals sorted on their start time.

def merge(intervals_a, intervals_b):
	result = []

	i, j = 0, 0

	start, end = 0, 1

	while i < len(intervals_a) and j < len(intervals_b):
		if intervals_a[i][start] < intervals_b[j][start]:
			if intervals_a[i][end] >= intervals_b[j][start]:
				result.append([intervals_b[j][start], min(intervals_a[i][end], intervals_a[j][end])])
				j += 1
			else:
				while i < len(intervals_a) and intervals_a[i][end] < intervals_b[j][start]:
					i += 1

		else:
			if intervals_a[i][start] <= intervals_b[j][end]:
				result.append([intervals_a[i][start], min(intervals_a[i][end], intervals_b[j][end])])
				i += 1
			else:
				while j < len(intervals_b) and intervals_a[i][start] < intervals_b[j][end]:
					j += 1

	return result


def main():
	print("Intervals Intersection: " +
		  str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
	print("Intervals Intersection: " +
		  str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()

# time complexity: O(N + M)
# space complexity: O(N)