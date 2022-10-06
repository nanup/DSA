# Given a binary tree, connect each node with its level order successor.
# The last node of each level should point to a null node.

from __future__ import print_function
from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right, self.next = None, None, None

	# level order traversal using 'next' pointer
	def print_level_order(self):
		nextLevelRoot = self
		while nextLevelRoot:
			current = nextLevelRoot
			nextLevelRoot = None
			while current:
				print(str(current.val) + " ", end='')
				if not nextLevelRoot:
					if current.left:
						nextLevelRoot = current.left
					elif current.right:
						nextLevelRoot = current.right
				current = current.next
			print()


def connect_level_order_siblings(root):
	if not root:
		return root
		
	queue = deque()

	queue.append(root)

	while queue:
		levelSize = len(queue)

		previousNode = None

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
	connect_level_order_siblings(root)

	print("Level order traversal using 'next' pointer: ")
	root.print_level_order()


main()

# time complexity: O(N)
# space complexity: O(N)