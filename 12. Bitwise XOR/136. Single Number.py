# In a non-empty array of integers, every number appears twice

# except for one, find that single number.


def find_single_number(arr):

    # x1 = arr[0]

    # for i in range(1, len(arr)):

    # 	x1 = x1 ^ arr[i]

    # return x1

    hashMap = hashMap()

    for num in arr:
        if num not in hashMap:
            hashMap[num] = 0
        else:
            del hashMap[num]

    return list(hashMap.keys())[0]


def main():

    arr = [1, 4, 2, 1, 3, 2, 3]

    print(find_single_number(arr))


main()


# time complexity: O(N)
# space complexity: o(1)


# time complexity: O(N)

# space complexity: O(N)
