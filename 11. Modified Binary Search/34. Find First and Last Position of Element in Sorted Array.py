# Given an array of numbers sorted in ascending order,
# find the range of a given number ‘key’.
# The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

# Write a function to return the range of the ‘key’.
# If the ‘key’ is not present return [-1, -1].

def find_range(arr, key):
	result = [- 1, -1]

	if key > arr[len(arr) - 1] or key < arr[0]:
		return result

	start, end = 0, len(arr) - 1

	while start <= end:
		mid = (end + start) // 2

		if key == arr[mid]:
			while arr[mid] == arr[start] and start > 0:
				start -= 1

			while arr[mid] == arr[end] and end < len(arr):
				end += 1

			return [start + 1, end - 1]
		elif key < arr[mid]:
			end = mid - 1
		else:
			start = mid + 1

	return [-1, -1]


def main():
	print(find_range([4, 6, 6, 6, 9], 6))
	print(find_range([1, 3, 8, 10, 15], 10))
	print(find_range([1, 3, 8, 10, 15], 12))


main()

# time complexity: O(log N)
# space complexity: O(1)