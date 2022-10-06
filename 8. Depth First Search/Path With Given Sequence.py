# Given a binary tree and a number sequence,
# find if the sequence is present as a root-to-leaf path in the given tree.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    if not root:
        return len(sequence) == 0

    return findPath(root, sequence, 0)


def findPath(root, sequence, sequenceIndex):
    if not root:
        return False

    seqLen = len(sequence)
    if sequenceIndex >= seqLen or root.val != sequence[sequenceIndex]:
        return False

    if not root.left and not root.right and seqLen - 1 == sequenceIndex:
        return True
    else:
        return findPath(root.left, sequence, sequenceIndex + 1) or findPath(root.right, sequence, sequenceIndex + 1)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()


# time complexity: O(N)
# space complexity: O(N)