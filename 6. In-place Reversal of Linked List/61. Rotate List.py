# Given the head of a Singly LinkedList and a number ‘k’,
# rotate the LinkedList to the right by ‘k’ nodes.

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate(head, rotations):
    listLength = calculateListLength(head)

    rotations %= listLength

    prev, curr = None, head

    firstNode = curr

    i = 0
    while i < listLength - rotations:
        prev = curr
        curr = curr.next
        i += 1

    prev.next = None
    head = curr

    while i < listLength:
        prev = curr
        curr = curr.next
        i += 1

    prev.next = firstNode

    return head


def calculateListLength(head):
    length = 0

    while head:
        head = head.next
        length += 1

    return length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()


# time complexity: O(N)
# space complexity: O(1)