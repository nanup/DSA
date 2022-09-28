# Given an array containing 0s, 1s and 2s, sort the array in-place.

def dutchFlagSort(arr):
	left, middle, right = 0, 0, len(arr) - 1

	while middle <= right:
		# middle needs to visit every positon and so <= instead of <
		if arr[middle] == 0:
			arr[middle], arr[left] = arr[left], arr[middle]
			middle += 1
			left += 1
		
		elif arr[middle] == 1:
			middle += 1
		else:
			arr[middle], arr[right] = arr[right], arr[middle]
			right -= 1
			# no middle becuase new char needs to be checked by middle

	return arr

def main():
	print(dutchFlagSort([1, 0, 2, 1, 0]))
	print(dutchFlagSort([2, 2, 0, 1, 2, 0]))

main()

# time complexity: O(N)
# space complexity: O(1)