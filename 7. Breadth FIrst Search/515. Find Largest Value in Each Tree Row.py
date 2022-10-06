# Find the largest value on each level of a binary tree.

from collections import deque
import math


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def find_level_averages(root):
	result = []

	if not root:
		return result

	queue = deque()

	queue.append(root)

	while queue:
		levelSize = len(queue)

		currentNodes = []

		maxVal = -math.inf

		for _ in range(levelSize):
			node = queue.popleft()

			maxVal = max(maxVal, node.val)

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

		result.append(maxVal)

	return result


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.left.right = TreeNode(2)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Level averages are: " + str(find_level_averages(root)))


main()

# time complexity: O(N)
# space complexity: O(N)