# Given the head of a LinkedList and two positions ‘p’ and ‘q’,
# reverse the LinkedList from position ‘p’ to ‘q’.

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


def reverse_sub_list(head, p, q):
	if p == q:
		return head

	current, previous = head, None

	i = 0

	while current and i < p - 1:
		previous = current
		current = current.next
		i += 1

	lastNodeOfFirstPart = previous
	lastNodeOfSubList = current
	next = None

	i = 0

	while current and i < q - p + 1:
		next = current.next
		current.next = previous
		previous = current
		current = next
		i += 1

	if lastNodeOfFirstPart:
		lastNodeOfFirstPart.next = previous
	else:
		head = previous

	lastNodeOfSubList.next = current

	return head

def main():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)

	print("Nodes of original LinkedList are: ", end='')
	head.print_list()
	result = reverse_sub_list(head, 2, 4)
	print("Nodes of reversed LinkedList are: ", end='')
	result.print_list()


main()
