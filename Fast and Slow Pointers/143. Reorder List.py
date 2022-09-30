# Given the head of a Singly LinkedList, write a method to modify
# the LinkedList such that the nodes from the second half of the LinkedList
# are inserted alternately to the nodes from the first half in reverse order.

from __future__ import print_function


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def print_list(self):
		temp = self
		while temp is not None:
			print(str(temp.value) + " ", end='')
			temp = temp.next
		print()


def reorder(head):
	middleNode = findMiddleOfLinkedList(head)
	reversedHead = reverseLinkedList(middleNode)

	left, right = head, reversedHead

	while left and right and left.next != right:
		leftNext = left.next
		left.next = right
		left = leftNext

		rightNext = right.next
		right.next = left
		right = rightNext


def findMiddleOfLinkedList(head):
	slow, fast = head, head

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	return slow


def reverseLinkedList(head):
	prev = None

	while head:
		next = head.next
		head.next = prev
		prev = head
		head = next

	return prev


def main():
	head = Node(2)
	head.next = Node(4)
	head.next.next = Node(6)
	head.next.next.next = Node(8)
	head.next.next.next.next = Node(10)
	head.next.next.next.next.next = Node(12)
	reorder(head)
	head.print_list()


main()

# time complexity: O(N)
# space complexity: O(1)