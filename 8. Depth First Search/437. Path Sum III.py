# Given a binary tree and a number āSā, find all paths in the tree such that
# the sum of all the node values of each path equals āSā.
# Please note that the paths can start or end at any node but
# all paths must follow direction from parent to child (top to bottom).

class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def count_paths(root, S):
	return countPathsRecursive(root, S, [])
	
def countPathsRecursive(currentNode, S, currentPath):
	if not currentNode:
		return 0

	currentPath.append(currentNode.val)

	pathSum, pathCount = 0, 0

	for i in range(len(currentPath) - 1, -1, -1):
		pathSum += currentPath[i]

		if pathSum == S:
			pathCount += 1

	pathCount += countPathsRecursive(currentNode.left, S, currentPath)
	pathCount += countPathsRecursive(currentNode.right, S, currentPath)

	del currentPath[-1]

	return pathCount

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(4)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Tree has paths: " + str(count_paths(root, 11)))


main()

# time complexity: O(N ^ 2)
# space complexity:  O(N)