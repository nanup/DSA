# Given an array of lowercase letters sorted in ascending order,
# find the smallest letter in the given array greater than a given ‘key’.

# Assume the given array is a circular list,
# which means that the last letter is assumed to be connected with the first letter.

def search_next_letter(letters, key):
    if key > letters[len(letters) - 1] or key < letters[0]:
        return letters[0]

    start, end = 0, len(letters) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return letters[start % len(letters)]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()

# time complexity: O(log N)
# space complexity: O(1)