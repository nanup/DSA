# In a non-empty array of numbers, every number appears exactly twice except
# two numbers that appear only once. Find the two numbers that appear only once.

def find_single_numbers(nums):
	n1xn2 = nums[0]
	for i in range(1, len(nums)):
		n1xn2 ^= nums[i]

	rightMostSetByte = 1

	while (rightMostSetByte & n1xn2) == 0:
		rightMostSetByte = rightMostSetByte << 1

	num1, num2 = 0, 0

	for num in nums:
		if (rightMostSetByte & num) == 0:
			num1 ^= num
		else:
			num2 ^= num

	return [num1, num2]

def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()

# time complexity: O(N)
# space complexity: O(1)