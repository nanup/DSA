# Given a number ‘n’, write a function to return all
# structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def find_unique_trees(n):
	if n <= 0:
		return []
	return find_unique_trees_rec(1, n)
	
def find_unique_trees_rec(start, end):
	result = []

	if start > end:
		result.append(None)
		return result

	for i in range(start, end + 1):
		leftSubTrees = find_unique_trees_rec(start, i - 1)
		rightSubTrees = find_unique_trees_rec(i + 1, end)

		for leftTree in leftSubTrees:
			for rightTree in rightSubTrees:
				root = TreeNode(i)
				root.left = leftTree
				root.right = rightTree
				result.append(root)

	return result


def main():
	print("Total trees: " + str(len(find_unique_trees(2))))
	print("Total trees: " + str(len(find_unique_trees(3))))


main()

# time complexity: O(N * 2 ^ N)
# space complexity: O(2 ^ N)