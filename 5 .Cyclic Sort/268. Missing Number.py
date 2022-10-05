# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
# Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

def findMissingNumber(nums):
    i = 0

    while i < len(nums):
        j = nums[i]
        if j < len(nums) and j != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)


def main():
    print(findMissingNumber([8, 3, 5, 2, 4, 6, 0, 1]))


main()
