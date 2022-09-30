# Any number will be called a happy number if,
# after repeatedly replacing it with a number equal to the sum of the square of all of its digits,
# leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
# Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

def find_happy_number(num):
	slow, fast = num, num

	while True:
		slow = squaredDigitsSum(slow)
		fast = squaredDigitsSum(squaredDigitsSum(fast))

		if fast == 1:
			return True

		if fast == slow:
			return False

		

def squaredDigitsSum(num):
    sum = 0

    while num > 0:
        digit = num % 10
        sum += digit ** 2
        num = num // 10

    return sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()


# time complexity: O(N)
# space complexity: O(1)