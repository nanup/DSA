# Given a binary tree, connect each node with its level order successor.
# The last node of each level should point to the first node of the next level.

from __future__ import print_function
from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right, self.next = None, None, None

	# tree traversal using 'next' pointer
	def print_tree(self):
		print("Traversal using 'next' pointer: ", end='')
		current = self
		while current:
			print(str(current.val) + " ", end='')
			current = current.next


def connect_all_siblings(root):
	if not root:
		return root

	queue = deque()

	queue.append(root)

	previousNode = None

	while queue:
		levelSize = len(queue)

		for _ in range(levelSize):
			node = queue.popleft()

			if previousNode:
				previousNode.next = node
			previousNode = node

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

	return root


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	connect_all_siblings(root)
	root.print_tree()


main()

# time complexity: O(N)
# space complexity: O(N)