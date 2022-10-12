# Given a string, sort it based on the decreasing frequency of its characters.
from heapq import *

def sort_character_by_frequency(str):
	wordFreq = dict()

	for word in str:
		wordFreq[word] = wordFreq.get(word, 0) + 1

	maxHeap = []
	for word, count in wordFreq.items():
		heappush(maxHeap, (-count, word))

	result = ""
	while maxHeap:
		count, word = heappop(maxHeap)
		for i in range(-count):
			result += word
	return result

	


def main():

    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()

# time complexity: O(N * logN)
# space complexity: O(N)