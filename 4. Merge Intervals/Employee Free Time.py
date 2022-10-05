# For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
# Our goal is to find out if there is a free interval that is common to all employees.
# You can assume that each list of employee working hours is sorted on the start time.

from __future__ import print_function
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        self.employeeIndex = employeeIndex  # index of employee in schedule list
        self.intervalIndex = intervalIndex  # index of employee in employee list

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    if not schedule:
        return []

    result, minHeap = [], []

    n = len(schedule)

    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))

    previousInterval = minHeap[0].interval

    while minHeap:
        queueTop = heappop(minHeap)

        # if previousInterval is not overlapping with next interval, insert a free interval
        if previousInterval.end < queueTop.interval.start:
            result.append(Interval(previousInterval.end, queueTop.interval.start))

            previousInterval = queueTop.interval

        else:
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval

        # if employee has more than one interval available
        employeeSchedule = schedule[queueTop.employeeIndex]

        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            heappush(minHeap, EmployeeInterval(
                employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex, queueTop.intervalIndex + 1))

    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()

# time complexity: O(N logK)
# space complexity: O(K)