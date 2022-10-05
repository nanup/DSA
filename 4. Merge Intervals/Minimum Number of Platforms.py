# Given a list of intervals representing the arrival and departure times
# of trains to a train station, our goal is to find the minimum number of platforms
# required for the train station so that no train has to wait.

def minimumNumberOfPlatforms(intervals):
	intervals.sort(key = lambda x: x[0])

	minPlatforms = 1

	for i in range(len(intervals)):
		platforms = 1

		for j in range(len(intervals)):
			if i != j:
				if intervals[i][0] < intervals[j][0] and intervals[i][1] > intervals[j][0]:
					platforms += 1

		minPlatforms = max(minPlatforms, platforms)

	return minPlatforms

def main():
	print(minimumNumberOfPlatforms([[1,4], [2, 5], [7, 9]]))

main()

# time complexity: O(N ^ 2)
# space complexity: O(1)