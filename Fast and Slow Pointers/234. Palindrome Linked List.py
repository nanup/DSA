# Given the head of a Singly LinkedList, write a method to check
# if the LinkedList is a palindrome or not.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
	isPalindrome = True

	slow, fast = head, head

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	middle =  slow

	reverseHead = reverseLinkedList(middle)

	prev = None

	while reverseHead:
		next = reverseHead.next
		if head.value != reverseHead.value:
			isPalindrome = False
		reverseHead.next = prev
		reverseHead = next
		prev = reverseHead

		head = head.next

	return isPalindrome

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
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()

# time complexity: O(N)
# space complexity: O(1)