# Find the minimum depth of a binary tree. The minimum depth is
# the number of nodes along the shortest path from the root node to the nearest leaf node.

from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def find_minimum_depth(root):
	result = []

	if not root:
		return result

	queue = deque()

	queue.append(root)

	minNodes = 0

	while queue:
		levelSize = len(queue)

		minNodes += 1

		for _ in range(levelSize):
			node = queue.popleft()

			if not node.left and not node.right:
				return minNodes

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
	root.left.left = TreeNode(9)
	root.right.left.left = TreeNode(11)
	print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()

# time complexity: O(N)
# space complexity: O(N)