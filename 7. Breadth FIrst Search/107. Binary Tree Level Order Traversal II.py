from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()

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

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        result.appendleft(currentNodes)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()

# time complexity: O(N)
# space complexity: O(N)