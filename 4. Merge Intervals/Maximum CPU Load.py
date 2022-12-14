# We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load
# when it is running. Our goal is to find the maximum CPU load at any time
# if all the jobs are running on the same machine.

from heapq import *


class job:
	def __init__(self, start, end, cpu_load):
		self.start = start
		self.end = end
		self.cpu_load = cpu_load

	def __lt__(job1, job2):
		if job1.start < job2.start:
			return job1
		else:
			return job2


def find_max_cpu_load(jobs):

	maxCPULoad = 0

	# for i in range(len(jobs)):
	# 	CPULoad = jobs[i].cpu_load

	# 	for j in range(len(jobs)):
	# 		if i != j:
	# 			if jobs[i].start < jobs[j].start and jobs[i].end > jobs[j].start:
	# 				CPULoad += jobs[j].cpu_load

	# 	maxCPULoad = max(maxCPULoad, CPULoad)

	jobs.sort(key = lambda x: x.start)

	minHeap = []

	cpuLoad = 0

	for i in range(len(jobs)):
		job = jobs[i]

		while len(minHeap) > 0 and job.start >= minHeap[0].end:
			cpuLoad -= minHeap[0].cpu_load
			heappop(minHeap)

		heappush(minHeap, job)

		cpuLoad += job.cpu_load
		
		maxCPULoad = max(maxCPULoad, cpuLoad)
			
	return maxCPULoad

def main():
	print("Maximum CPU load at any time: " +
		  str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
	print("Maximum CPU load at any time: " +
		  str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
	print("Maximum CPU load at any time: " +
		  str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()

# time complexity: O(N ^ 2)
# space complexity: O(1)

# time complexity: O(N logN)
# space complexity: O(N)