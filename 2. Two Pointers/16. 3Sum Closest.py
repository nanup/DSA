# Given an array of unsorted numbers and a target number,
# find a triplet in the array whose sum is as close to the target number as possible,
# return the sum of the triplet.
import math


def tripletSumCloseToTarget(arr, targetSum):
    arr.sort()

    smallestDiff = math.inf

    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1

        while left < right:
            currentDiff = targetSum - arr[i] - arr[left] - arr[right]

            if currentDiff == 0:
                return 0

            if abs(currentDiff) < abs(smallestDiff) or (abs(currentDiff) == abs(smallestDiff) and currentDiff > smallestDiff):
                smallestDiff = currentDiff

            if currentDiff > 0:
                left += 1
            else:
                right -= 1

    return targetSum - smallestDiff


def main():
    print(tripletSumCloseToTarget([-2, 0, 1, 2], 2))
    print(tripletSumCloseToTarget([-3, -1, 1, 2], 1))


main()

# time complexity: O(N ^ 2)
# space complexity: O(N)