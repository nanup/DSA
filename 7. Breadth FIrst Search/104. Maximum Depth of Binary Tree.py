# Given a binary tree, find its maximum depth (or height).

from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def find_maximum_depth(root):
	if not root:
		return 0

	queue = deque()

	queue.append(root)

	depth = 0

	while queue:
		levelSize = len(queue)

		depth += 1

		for _ in range(levelSize):
			node = queue.popleft()

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

	return depth


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
	root.left.left = TreeNode(9)
	root.right.left.left = TreeNode(11)
	print("Tree Maximum Depth: " + str(find_maximum_depth(root)))


main()

# time complexity: O(N)
# space complexity: O(N)