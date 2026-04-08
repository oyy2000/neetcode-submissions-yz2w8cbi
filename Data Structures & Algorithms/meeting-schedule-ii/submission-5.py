"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        length = len(intervals)
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        i, j = 0, 0
        count = 0
        while i < length and j < length:
            if start[i] < end[j]:
                i += 1
                count = max(count, i - j)
            else:
                j +=1
        return count

    