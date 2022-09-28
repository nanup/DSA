# Given an array of unsorted numbers, find all unique triplets 
# in it that add up to zero.

def searchTriplets(arr):
	arr.sort()

	triplets = []

	for i in range(len(arr)):
		if  i > 0 and arr[i - 1] == arr[i]:
			continue
		target = -arr[i]
		startIndex = i + 1
		searchPairs(arr, target, startIndex, triplets)

	return triplets


def searchPairs(arr, target, startIndex, triplets):
	left, right = startIndex, len(arr) - 1

	while left < right:
		currentSum = arr[left] + arr[right]

		if currentSum == target:
			triplets.append([-target, arr[left], arr[right]])
			
			left += 1
			right -= 1

			while left < right and arr[left] == arr[left - 1]:
				left += 1  # skip same element to avoid duplicate triplets
			while left < right and arr[right] == arr[right + 1]:
				right -= 1  # skip same element to avoid duplicate triplets

		elif currentSum < target:
			left += 1
		else:
			right -= 1

def main():
	print(searchTriplets([-3, 0, 1, 2, -1, 1, -2]))

main()

# time complexity: O(N^2)
# space complexity: O(N)