# Given a set with distinct elements, find all of its distinct subsets.
from collections import deque


def find_subsets(nums):
    subsets = []

    subsets.append([])

    for num in nums:
        n = len(subsets)

        for i in range(n):
            set = list(subsets[i])
            set.append(num)
            subsets.append(set)

    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()

# time complexity: O(2 ^ N)
# space complexity: O(2 ^ N)