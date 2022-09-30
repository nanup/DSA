# Given the head of a Singly LinkedList that contains a cycle,
# write a function to find the starting node of the cycle.

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycleLength = calculateCycleLength(slow)
            return findCycleStart(cycleLength, head)


def calculateCycleLength(node):
    current = node
    cycleLength = 0

    while True:
        current = current.next
        cycleLength += 1

        if current == node:
            break

    return cycleLength


def findCycleStart(cycleLength, head):
    first, second = head, head

    while cycleLength > 0:
        first = first.next
        cycleLength -= 1

    while first != second:
        first = first.next
        second = second.next

    return first


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()

# time complexity: O(N)
# space complexity: O(1)
