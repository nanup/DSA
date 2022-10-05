# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
# The array has only one duplicate but it can be repeated multiple times.
# Find that duplicate number without using any extra space.
# You are, however, allowed to modify the input array.

def findDuplicates(nums):
    i = 0

    while i < len(nums):
        j = nums[i]

        if j != nums[j - 1]:
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i]

    return -1


def main():
    print(findDuplicates([1, 4, 4, 3, 2]))
    print(findDuplicates([2, 1, 3, 3, 5, 4]))
    print(findDuplicates([2, 4, 1, 4, 4]))


main()

# time complexity: O(N)
# space complexity: O(1)
