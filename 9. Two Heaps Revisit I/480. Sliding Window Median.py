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

		windowStart = 0

		for windowEnd in range(len(nums)):
			num = nums[windowEnd]

			if not self.maxHeap or -self.maxHeap[0] >= num:
				heappush(self.maxHeap, -num)
			else:
				heappush(self.minHeap, num)

			self.balanceHeaps()

			if windowEnd - windowStart + 1 == k:
				result.append(self.findMedian())
				outNum = nums[windowStart]
				windowStart += 1

				if outNum <= -self.maxHeap[0]:
					self.remove(self.maxHeap, -outNum)
				else:
					self.remove(self.minHeap, outNum)

				self.balanceHeaps()

		return result

	def balanceHeaps(self):
		if len(self.maxHeap) > len(self.minHeap) + 1:
			heappush(self.minHeap, -heappop(self.maxHeap))
		elif len(self.maxHeap) < len(self.minHeap):
			heappush(self.maxHeap, -heappop(self.minHeap))

	def findMedian(self):
		if len(self.maxHeap) == len(self.minHeap):
			return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
		else:
			return -self.maxHeap[0] / 1.0

	def remove(self, heap, num):
		i = heap.index(num)

		heap[i] = heap[-1]
		del heap[-1]

		if i < len(heap):
			heapq._siftup(heap, i)
			heapq._siftdown(heap, 0, i)


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


# time complexity: O(N*K)
# space complexity: O(K)