# For a given positive number N in base-10,
# return the complement of its binary representation as a base-10 integer.

def calculate_bitwise_complement(num):
	bitCount, n = 0, num
	while n > 0:
		bitCount += 1
		n = n >> 1

	allBitsSet = pow(2, bitCount) - 1

	return num ^ allBitsSet

def main():
	print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
	print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


main()

# time complexity: O(b)
# space complexity: O(1)