# Given an array, find the sum of all numbers between
# the K1’th and K2’th smallest elements of that array.
from heapq import *


def find_sum_of_elements(nums, k1, k2):
    maxHeap = []
    for num in nums:
        heappush(maxHeap, -num)
        if len(maxHeap) > k2:
            heappop(maxHeap)

    heappop(maxHeap)
    result = 0

    for _ in range(k2 - k1 -1):
        result += -heappop(maxHeap)
    return result


def main():

    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()

# time complexity: O(N * logN)
# space complexity: O(N)