# Given a binary tree, return all root-to-leaf paths.

class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def find_paths(root):
	allPaths = []
	findPaths(root, allPaths, [])
	return allPaths

def findPaths(currentNode, allPaths, currentPath):
	if not currentNode:
		return None

	currentPath.append(currentNode.val)

	if not currentNode.left and not currentNode.right:
		allPaths.append(list(currentPath))

	findPaths(currentNode.left, allPaths, currentPath)
	findPaths(currentNode.right, allPaths, currentPath)

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

# time complexity: O(N)
# space compelxity: O(N * logN)