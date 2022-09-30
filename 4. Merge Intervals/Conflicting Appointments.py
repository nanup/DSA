# Given an array of intervals representing ‘N’ appointments,
# find out if a person can attend all the appointments.

def can_attend_all_appointments(intervals):
	intervals.sort(key = lambda x: x[0])

	if len(intervals) < 2:
		return True

	start, end = intervals[0][0], intervals[0][1]

	for i in range(1, len(intervals)):
		interval = intervals[i]

		if end > interval[0]:
			return False
		else:
			start = interval[0]
			end = interval[1]

	return True


def main():
	print("Can attend all appointments: " +
		  str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
	print("Can attend all appointments: " +
		  str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
	print("Can attend all appointments: " +
		  str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()

# time complexity: O(N * log N)
# space compelxity: O(N)
