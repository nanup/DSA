# Given an array of numbers sorted in an ascending order,
# find the ceiling of a given number ‘key’.
# The ceiling of the ‘key’ will be the smallest element in the given array
# greater than or equal to the ‘key’.

# Write a function to return the index of the ceiling of the ‘key’.
# If there isn’t any ceiling return -1.

def search_ceiling_of_a_number(arr, key):
	if key > arr[len(arr) - 1]:
		return -1

	start, end = 0, len(arr) - 1

	while start <= end:
		mid = start + (end - start) // 2

		if key < arr[mid]:
			end = mid - 1
		elif key > arr[mid]:
			start = mid + 1
		else:
			return mid

	return start


def main():
	print(search_ceiling_of_a_number([4, 6, 10], 6))
	print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
	print(search_ceiling_of_a_number([4, 6, 10], 17))
	print(search_ceiling_of_a_number([4, 6, 10], -1))


main()

# time complexity: O(log N)
# space complexity: O(1)