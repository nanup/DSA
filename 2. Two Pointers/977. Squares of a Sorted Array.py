# Given a sorted array, create a new array containing 
# squares of all the number of the input array in the sorted order.

def makeSquares(arr):
	result = [0] * len(arr)

	nextIndex = len(arr) - 1

	left, right = 0, len(arr) - 1

	while nextIndex >= 0:
		if abs(arr[left]) > abs(arr[right]):
			result[nextIndex] = arr[left] ** 2
			left += 1
		else:
			result[nextIndex] = arr[right] ** 2
			right -= 1

		nextIndex -= 1

	return result

def main():
	print(makeSquares([-2, -1, 0, 2, 3]))
	print(makeSquares([-3, -1, 0, 1, 2]))

main()

# time complexity: O(N)
# space complexity: O(N)