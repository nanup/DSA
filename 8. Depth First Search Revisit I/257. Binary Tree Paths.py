# Given a binary tree, return all root-to-leaf paths.

class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def find_paths(root, sum):
	allPaths = []
	findPaths(root, sum, allPaths, [])
	return allPaths

def findPaths(currentNode, sum, allPaths, currentPath):
	if not currentNode:
		return None

	currentPath.append(currentNode.val)

	if not currentNode.left and not currentNode.right:
		allPaths.append(list(currentPath))

	findPaths(currentNode.left, sum - currentNode.val, allPaths, currentPath)
	findPaths(currentNode.right, sum - currentNode.val, allPaths, currentPath)

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

# time complexity: O(N)
# space compelxity: O(N * logN)