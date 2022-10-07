# Given an array of numbers and a number ‘k’,
# find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

from heapq import *
import heapq


class SlidingWindowMedian:
	def __init__(self):
		self.minHeap = []
		self.maxHeap = []

	def find_sliding_window_median(self, nums, k):
		result = []

		windowStart, windowEnd = 0, 0

		while windowEnd < len(nums):
			num = nums[windowEnd]

			if not self.maxHeap or -self.maxHeap[0] >= num:
				heappush(self.maxHeap, -num)
			else:
				heappush(self.minHeap, num)

			self.balanceHeaps()

			if windowEnd - windowStart + 1 == k:
				if len(self.maxHeap) == len(self.minHeap):
					median = -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
				else:
					median = -self.maxHeap[0] / 1.0

				result.append(median)

				outNum = nums[windowStart]

				if outNum <= -self.maxHeap[0]:
					self.remove(self.maxHeap, -outNum)
				else:
					self.remove(self.minHeap, outNum)

				self.balanceHeaps()

				windowStart += 1

			windowEnd += 1

		return result

	def balanceHeaps(self):
		if len(self.maxHeap) > len(self.minHeap) + 1:
			heappush(self.minHeap, -heappop(self.maxHeap))
		elif len(self.maxHeap) < len(self.minHeap):
			heappush(self.maxHeap, -heappop(self.minHeap))

	def remove(self, heap, num):
		index = heap.index(num)

		heap[index] = heap[-1]
		del heap[-1]

		if index < len(heap):
			heapq._siftup(heap, index)
			heapq._siftdown(heap, 0, index)

def main():

	slidingWindowMedian = SlidingWindowMedian()
	result = slidingWindowMedian.find_sliding_window_median(
		[1, 2, -1, 3, 5], 2)
	print("Sliding window medians are: " + str(result))

	slidingWindowMedian = SlidingWindowMedian()
	result = slidingWindowMedian.find_sliding_window_median(
		[1, 2, -1, 3, 5], 3)
	print("Sliding window medians are: " + str(result))


main()

# time complexity: O(N * K)
# space complexity: O(N)