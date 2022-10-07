# Given a binary tree and a number sequence, find if the sequence
# is present as a root-to-leaf path in the given tree.

class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def find_path(root, sequence):
	if not root:
		return len(sequence) == 0

	return findPath(root, sequence, 0)

def findPath(currentNode, sequence, index):
	if not currentNode:
		return False

	if index >= len(sequence) or currentNode.val != sequence[index]:
		return False

	if not currentNode.left and not currentNode.right and currentNode.val == sequence[index]:
		if len(sequence) - 1 != index:
			return False
		return True

	return findPath(currentNode.left, sequence, index + 1) or findPath(currentNode.right, sequence, index + 1)


def main():

	root = TreeNode(1)
	root.left = TreeNode(0)
	root.right = TreeNode(1)
	root.left.left = TreeNode(1)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(5)

	print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
	print("Tree has path sequence: " + str(find_path(root, [1, 0, 1, 6])))


main()

# time complexity: O(N)
# space complexity: O(N)