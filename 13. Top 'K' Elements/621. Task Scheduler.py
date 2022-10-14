# You are given a list of tasks that need to be run, in any order, on a server.
# Each task will take one CPU interval to execute but once a task has finished,
# it has a cooling period during which it can’t be run again.
# If the cooling period for all tasks is ‘K’ intervals,
# find the minimum number of CPU intervals that the server needs to finish all tasks.

# If at any time the server can’t execute any task then it must stay idle.
from heapq import *


def schedule_tasks(tasks, k):
	taskFreqs = {}
	for task in tasks:
		taskFreqs[task] = taskFreqs.get(task, 0) + 1

	maxHeap = []
	for task, taskFreq in taskFreqs.items():
		heappush(maxHeap, (-taskFreq, task))

	intervalCount = 0
	while maxHeap:
		waitlist = []
		n = k + 1

		while n > 0 and maxHeap:
			taskFreq, task = heappop(maxHeap)
			intervalCount += 1
			if -taskFreq > 1:
				waitlist.append((taskFreq + 1, task))
			n -= 1

		for taskFreq, task in waitlist:
			heappush(maxHeap, (taskFreq, task))

		if maxHeap:
			intervalCount += n

	return intervalCount


def main():
	print("Minimum intervals needed to execute all tasks: " +
		  str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
	print("Minimum intervals needed to execute all tasks: " +
		  str(schedule_tasks(['a', 'b', 'a'], 3)))


main()

# time complexity: O(N * log N)
# space complexity: O(N)