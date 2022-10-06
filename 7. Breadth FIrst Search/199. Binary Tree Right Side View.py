# Given a binary tree, return an array containing nodes in its right view.
# The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []

    if not root:
        return result

    queue = deque()

    queue.append(root)

    while queue:
        levelSize = len(queue)

        levelIndex = 0

        for _ in range(levelSize):
            node = queue.popleft()

            levelIndex += 1

            if levelIndex == levelSize:
                result.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()

# time complexity: O(N)
# space complexity: O(N)