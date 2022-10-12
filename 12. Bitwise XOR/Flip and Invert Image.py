# Given a binary matrix representing an image,
# we want to flip the image horizontally, then invert it.

def flip_and_invert_image(matrix):
	c = len(matrix)
	for row in matrix:
		for i in range((c + 1) // 2):
			row[i], row[c - i - 1] = row[c - i - 1] ^ 1, row[i] ^ 1
	
	return matrix


def main():
	print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
	print(flip_and_invert_image(
		[[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()

# time complexity: O(N)
# space complexity: O(1)