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


class MaximumPathSum:
	def find_maximum_path_sum(self, root):
		self.maxPathSum = 0
		self.calculateMaxPathSum(root)

		return self.maxPathSum

	def calculateMaxPathSum(self, root):
		if not root:
			return 0

		leftMaxPathSum = self.calculateMaxPathSum(root.left)
		rightMaxPathSum = self.calculateMaxPathSum(root.right)

		rootMaxPathSum = root.val + max(leftMaxPathSum, rightMaxPathSum)

		self.maxPathSum = max(self.maxPathSum, rootMaxPathSum +
						 min(leftMaxPathSum, rightMaxPathSum))

		return self.maxPathSum


def main():
	maximumPathSum = MaximumPathSum()
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)

	print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
	root.left.left = TreeNode(1)
	root.left.right = TreeNode(3)
	root.right.left = TreeNode(5)
	root.right.right = TreeNode(6)
	root.right.left.left = TreeNode(7)
	root.right.left.right = TreeNode(8)
	root.right.right.left = TreeNode(9)
	print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

	root = TreeNode(-1)
	root.left = TreeNode(-3)
	print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))


main()
