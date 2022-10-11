def search_bitonic_array(arr, key):
	n = len(arr)

	start, end = 0, n - 1

	while start < end:
		mid = (end + start) // 2

		if arr[mid] < arr[mid + 1]:
			start = mid + 1
		else:
			end = mid

	maxIndex = start

	if key > arr[maxIndex]:
		return -1

	if key == arr[maxIndex]:
		return maxIndex

	start, end = 0, maxIndex - 1

	while start <= end:
		mid = (end + start) // 2

		if arr[mid] == key:
			return mid
		elif key > arr[mid]:
			start = mid + 1
		else:
			end = mid - 1

	start, end = maxIndex + 1, n - 1

	while start <= end:
		mid = (end + start) // 2

		if arr[mid] == key:
			return mid
		elif key > arr[mid]:
			end = mid - 1
		else:
			start = mid + 1

	return -1

def main():
	print(search_bitonic_array([1, 3, 8, 4, 3], 4))
	print(search_bitonic_array([3, 8, 3, 1], 8))
	print(search_bitonic_array([1, 3, 8, 12], 12))
	print(search_bitonic_array([10, 9, 8], 10))


main()

# time complexity: O(log N)
# space complexity: o(1)