# Given a string, find if its letters can be rearranged in such a way that
# no two same characters come next to each other.

from heapq import *


def rearrange_string(str):
	wordFreq = {}
	for word in str:
		wordFreq[word] = wordFreq.get(word, 0) + 1

	maxHeap = []
	for word, count in wordFreq.items():
		heappush(maxHeap, [-count, word])

	previousChar, previousFrequency = None, 0

	resultString = []
	while maxHeap:
		print(maxHeap)
		firstCount, first = heappop(maxHeap)
		if previousChar and -previousFrequency > 0:
			heappush(maxHeap, [previousFrequency, previousChar])
		resultString.append(first)
		previousChar = first
		previousFrequency = firstCount + 1

	return "".join(resultString) if len(resultString) == len(str) else ""

def main():
	print("Rearranged string:  " + rearrange_string("aappp"))
	print("Rearranged string:  " + rearrange_string("Programming"))
	print("Rearranged string:  " + rearrange_string("aapa"))


main()

# time complexity: O(N * logN)
# space complexity: O(N)