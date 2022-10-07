# Given a binary tree where each node can only have a digit (0-9) value,
# each root-to-leaf path will represent a number.
# Find the total sum of all the numbers represented by all paths.

class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def find_sum_of_path_numbers(root):
	return findSum(root, 0)

def findSum(currentNode, pathSum):
	if not currentNode:
		return 0

	pathSum = 10 * pathSum + currentNode.val

	if not currentNode.left and not currentNode.right:
		return pathSum

	return findSum(currentNode.left, pathSum) + findSum(currentNode.right, pathSum)


def main():
	root = TreeNode(1)
	root.left = TreeNode(0)
	root.right = TreeNode(1)
	root.left.left = TreeNode(1)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(5)
	print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()

# time complexity: O(N)
# space comeplexity: O(N)