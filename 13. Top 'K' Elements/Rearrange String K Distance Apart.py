# Given a string and a number ‘K’, find if the string can be rearranged
# such that the same characters are at least ‘K’ distance apart from each other.
from heapq import *
from collections import deque


def reorganize_string(str, k):
	if k <= 1:
		return str
	
	charFreq = {}
	for char in str:
		charFreq[char] = charFreq.get(char, 0) + 1

	maxHeap = []
	for char, freq in charFreq.items():
		heappush(maxHeap, (-freq, char))

	prevChar, prevFreq = None, 0

	queue = deque()
	resultString = []
	while maxHeap:
		freq, char = heappop(maxHeap)
		queue.append((freq + 1, char))
		if len(queue) == k:
			prevFreq, prevChar = queue.popleft()
			if -prevFreq > 0:
				heappush(maxHeap, (prevFreq, prevChar))
		resultString.append(char)

	return "".join(resultString) if len(resultString) == len(str) else ""

def main():
	print("Reorganized string: " + reorganize_string("mmpp", 2))
	print("Reorganized string: " + reorganize_string("Programming", 3))
	print("Reorganized string: " + reorganize_string("aab", 2))
	print("Reorganized string: " + reorganize_string("aapa", 3))


main()

# time complexity: O(N * logN)
# space complexity: O(N)