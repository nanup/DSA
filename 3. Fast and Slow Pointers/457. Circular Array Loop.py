# We are given an array containing positive and negative numbers.
# Suppose the array contains a number ‘M’ at a particular index.
# Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices.

# You should assume that the array is circular which means two things:
# 1. If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
# 2. If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.

# Write a method to determine if the array has a cycle.
# The cycle should have more than one element and should follow one direction
# which means the cycle should not contain both forward and backward movements.

def circular_array_loop_exists(arr):
	for i in range(len(arr)):
		isForward = arr[i] >= 0

		slow, fast = i, i

		while True:
			slow = findNextValidIndex(slow, isForward, arr)
			fast = findNextValidIndex(fast, isForward, arr)

			if fast != -1:
				fast = findNextValidIndex(fast, isForward, arr)

			if slow == fast or slow == -1 or fast == -1:
				break

		if slow != -1 and slow == fast:
			return True

	return False

def findNextValidIndex(index, isForward, arr):
	direction = arr[index] >= 0

	if direction != isForward:
		return -1

	nextIndex = (index + arr[index]) % len(arr)

	if index == nextIndex:
		return - 1

	return nextIndex
def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()

# time complexity: O(N ^ 2)
# space complexity: O(1)
