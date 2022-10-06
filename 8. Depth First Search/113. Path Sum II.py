# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that
# the sum of all the node values of each path equals ‘S’.

class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def find_paths(root, sum):
	allPaths = []
	findPathsRecursive(root, sum, [], allPaths)
	return allPaths

def findPathsRecursive(currentNode, sum, currentPath, allPaths):
	if not currentNode:
		return

	currentPath.append(currentNode.val)

	if currentNode.val == sum and not currentNode.left and not currentNode.right:
		allPaths.append(list(currentPath))
	else:
		findPathsRecursive(currentNode.left, sum - currentNode.val, currentPath, allPaths)
		findPathsRecursive(currentNode.right, sum - currentNode.val, currentPath, allPaths)

	del currentPath[-1]

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(4)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	sum = 23
	print("Tree paths with sum " + str(sum) +
		  ": " + str(find_paths(root, sum)))


main()

# time complexity: O(N ^ 2)
# space complexity: O(N * logN)