# Given an array of sorted numbers, remove all duplicates from it. 
# You should not use any extra space; 
# after removing the duplicates in-place return the new length of the array.

def removeDuplicates(arr):
    left, right = 0, 0

    if len(arr) <= 1:
        return len(arr)

    while right < len(arr):
        if arr[left] != arr[right]:
            left += 1
            arr[left], arr[right] = arr[right], arr[left]

        right += 1

    return left + 1

def main():
    print("Array new length: " + str(removeDuplicates([2, 3, 3, 3, 6, 9, 9])))

main()

# time complexity: O(N)
# space complexity: O(1)