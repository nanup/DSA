# Given a binary tree, populate an array to represent the averages of all of its levels.

from collections import deque


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

		for _ in range(levelSize):
			node = queue.popleft()

			currentNodes.append(node.val)

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

		levelAverage = calculateAverage(currentNodes)

		result.append(levelAverage)

	return result


def calculateAverage(nodeList):
	sum = 0

	for val in nodeList:
		sum += val

	average = sum / len(nodeList)

	return average


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