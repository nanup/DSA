# Given a binary tree and a node, find the level order successor of the given node in the tree.
# The level order successor is the node that appears right after the given node in the level order traversal.

from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def find_successor(root, key):
	if not root:
		return root

	queue = deque()

	queue.append(root)

	seen = False

	while queue:
		levelSize = len(queue)

		for _ in range(levelSize):
			node = queue.popleft()

			if seen:
				return node

			if node.val == key:
				seen = True

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	result = find_successor(root, 12)
	if result:
		print(result.val)
	result = find_successor(root, 9)
	if result:
		print(result.val)


main()

# time complexity: O(N)
# space complexity: O(N)