# Given an array, find the length of the smallest subarray in it
# which when sorted will sort the whole array.

def shortestWindowSort(arr):
	left, right = 0, len(arr) - 1

	while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
		left += 1

	if left == len(arr) - 1:
		return 0

	while right > 0 and arr[right] >= arr[right - 1]:
		right -= 1

	# find the smallest subarray with elements out of sort order

	subarrayMax = max(arr[left:right + 1])
	subarrayMin = min(arr[left:right + 1])

	# extend the subarray on both sides considering the subarray min and max

	while left > 0 and arr[left - 1] > subarrayMin:
		left -= 1

	while right < len(arr) - 1 and arr[right + 1] < subarrayMax:
		right += 1

	return right - left + 1


def main():
	print(shortestWindowSort([1, 3, 2, 0, -1, 7, 10]))

main()

# time complexity: O(N)
# space complexity: O(1)