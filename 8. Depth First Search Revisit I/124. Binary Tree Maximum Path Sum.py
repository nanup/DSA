# Find the path with the maximum sum in a given binary tree.
# Write a function that returns the maximum sum.
# A path can be defined as a sequence of nodes between any two nodes and
# doesn’t necessarily pass through the root.

import math


class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class MaxTreeNode():
	def find_maximum_path_sum(self, root):
		self.maxPathSum = -math.inf
		self.findPathSum(root)

		return self.maxPathSum

	def findPathSum(self, currentNode):
		if not currentNode:
			return 0

		leftPathSum = self.findPathSum(currentNode.left)
		rightPathSum = self.findPathSum(currentNode.right)

		leftPathSum = max(leftPathSum, 0)
		rightPathSum = max(rightPathSum, 0)

		pathSum = currentNode.val + leftPathSum + rightPathSum

		self.maxPathSum = max(self.maxPathSum, pathSum, 0)

		return currentNode.val + max(leftPathSum, rightPathSum)


def main():
	maxTreeNode = MaxTreeNode()
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)

	print("Maximum Path Sum: " + str(maxTreeNode.find_maximum_path_sum(root)))
	root.left.left = TreeNode(1)
	root.left.right = TreeNode(3)
	root.right.left = TreeNode(5)
	root.right.right = TreeNode(6)
	root.right.left.left = TreeNode(7)
	root.right.left.right = TreeNode(8)
	root.right.right.left = TreeNode(9)
	print("Maximum Path Sum: " + str(maxTreeNode.find_maximum_path_sum(root)))

	root = TreeNode(-1)
	root.left = TreeNode(-3)
	print("Maximum Path Sum: " + str(maxTreeNode.find_maximum_path_sum(root)))


main()

# time complexity: O(N)
# space complexity: O(N)