# Given an array of unsorted numbers and a target number,
# find all unique quadruplets in it,
# whose sum is equal to the target number.\

def searchQuadraplets(arr, target):
	arr.sort()

	result = []

	for i in range(len(arr) - 3):
		if i > 0 and arr[i] == arr[i - 1]:
			continue

		for j in range(i + 1, len(arr) - 2):
			if j > i + 1 and arr[j] == arr[j - 1]:
				continue

			left = j + 1
			right = len(arr) - 1

			while left < right:
				currentSum = arr[i] + arr[j] + arr[left] + arr[right]

				if currentSum == target:
					result.append([arr[i], arr[j], arr[left], arr[right]])

					left += 1
					right -= 1

					while left < right and arr[left] == arr[left - 1]:
						left += 1

					while left < right and arr[right] == arr[right + 1]:
						right -= 1

				elif currentSum < target:
					left += 1
				else:
					right -= 1

	return result


def main():
	# print(searchQuadraplets([4, 1, 2, -1, 1, -3], 1))
	# print(searchQuadraplets([2, 0, -1, 1, -2, 2], 2))
	print(searchQuadraplets([1,0,-1,0,-2,2], 0))


main()

# time complexity: O(N ^ 3)
# space complexity: O(N)