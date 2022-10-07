# Given a binary tree, find the root-to-leaf path with the maximum sum.

import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMaxSumPath(root):
    maxPathSum = -math.inf
    return findMaxSumPathRec(root, maxPathSum, 0)


def findMaxSumPathRec(currentNode, maxPathSum, currentPathSum):
    if not currentNode:
        return maxPathSum

    currentPathSum += currentNode.val

    if not currentNode.left and not currentNode.right:
        maxPathSum = max(maxPathSum, currentPathSum)

    maxPathSum = max(
        findMaxSumPathRec(currentNode.left, maxPathSum, currentPathSum),
        findMaxSumPathRec(currentNode.right, maxPathSum, currentPathSum))

    return maxPathSum


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree path with maximum sum: " + str(findMaxSumPath(root)))


main()

# time complexity: O(N)
# space complexity: O(N)