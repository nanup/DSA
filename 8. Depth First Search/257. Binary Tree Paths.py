# Given a binary tree, return all root-to-leaf paths.

class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def find_paths(root):
	allPaths = []
	findPath(root, [], allPaths)
	return allPaths

def findPath(currentNode, currentPath, allPaths):
	if not currentNode:
		return currentNode

	currentPath.append(currentNode.val)

	if not currentNode.left and not currentNode.right:
		allPaths.append(list(currentPath))
	else:
		findPath(currentNode.left, currentPath, allPaths)
		findPath(currentNode.right, currentPath, allPaths)

	del currentPath[-1]

def main():

	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(4)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)

	print("Tree paths: " + str(find_paths(root)))


main()

# time complexity: O(N ^ 2)
# space complexity: O(N logN)