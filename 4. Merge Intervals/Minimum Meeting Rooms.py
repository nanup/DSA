# Given a list of intervals representing the start and end time of ‘N’ meetings,
# find the minimum number of rooms required to hold all the meetings.

from heapq import *


class Meeting:
	def __init__(self, start, end):
		self.start = start
		self.end = end


def min_meeting_rooms(meetings):
	meetings.sort(key=lambda x: x.start)

	# minRooms = 1

	# end = meetings[0].end

	# for i in range(1, len(meetings)):
	# 	rooms = 1

	# 	copy = i

	# 	meeting = meetings[i]

	# 	while i < len(meetings) and end > meeting.start:
	# 		rooms += 1
	# 		i += 1

	# 	if i != len(meetings):
	# 		end = meetings[i].end

	# 	if rooms > minRooms:
	# 		minRooms = rooms

	# return minRooms

	minRooms = 0

	minHeap = []

	for meeting in meetings:
		while (len(minHeap) > 0 and meeting.start >= minHeap[0].end):
			heappop(minHeap)

		heappush(minHeap, meeting)

		minRooms = max(minRooms, len(minHeap))

	return minRooms


def main():
	print("Minimum meeting rooms required: " + str(min_meeting_rooms(
		[Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
	print("Minimum meeting rooms required: " +
		  str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
	print("Minimum meeting rooms required: " +
		  str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
	print("Minimum meeting rooms required: " +
		  str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
	print("Minimum meeting rooms required: " +
		  str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 8), Meeting(3, 10), Meeting(6, 9)])))


main()
