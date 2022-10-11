# Given an array of numbers sorted in ascending order,
# find the element in the array that has the minimum difference with the given ‘key’.

def search_min_diff_element(arr, key):
	n = len(arr)

	if key <= arr[0]:
		return arr[0]

	if key >= arr[n - 1]:
		return arr[n - 1]

	start, end = 0, n - 1

	while start <= end:
		mid = (end + start) // 2

		if arr[mid] == key:
			return key
		elif arr[mid] < key:
			start = mid + 1
		else:
			end = mid - 1

	if abs(arr[start] - key) < abs(arr[end] - key):
		return arr[start]
	return arr[end]


def main():
	print(search_min_diff_element([4, 6, 10], 7))
	print(search_min_diff_element([4, 6, 10], 4))
	print(search_min_diff_element([1, 3, 8, 10, 15], 12))
	print(search_min_diff_element([4, 6, 10], 17))


main()

# time complexity: O(log N)
# space complexity: O(1)