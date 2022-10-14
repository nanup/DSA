# Design a class that simulates a Stack data structure,
# implementing the following two operations:

# 1. push(int num): Pushes the number ‘num’ on the stack.
# 2. pop(): Returns the most frequent number in the stack.
#    If there is a tie, return the number which was pushed later.
from heapq import *

class FrequencyStack:
	numFreqs = {}

	def push(self, num):
		if num not in self.numFreqs:
			self.numFreqs[num] = 0
		self.numFreqs[num] += 1

	def pop(self):
		maxHeap = []

		for num, numFreq in self.numFreqs.items():
			heappush(maxHeap, (-numFreq, num))

		resultFreq, result = heappop(maxHeap)
		waitlist = []
		
		while result == maxHeap[0][1]:
			waitlist.append((resultFreq, result))
			resutFreq, result = heappop(maxHeap)

		if waitlist:
			for resultFreq, result in waitlist:
				heappush(maxHeap, (resultFreq, result))

		self.numFreqs[result] -= 1

		return result


def main():
	frequencyStack = FrequencyStack()
	frequencyStack.push(1)
	frequencyStack.push(2)
	frequencyStack.push(3)
	frequencyStack.push(2)
	frequencyStack.push(1)
	frequencyStack.push(2)
	frequencyStack.push(5)
	print(frequencyStack.pop())
	print(frequencyStack.pop())
	print(frequencyStack.pop())


main()
