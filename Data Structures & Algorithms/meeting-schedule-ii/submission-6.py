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
        count = 0
        room_used = 0
        s = e = 0
        while s < length:
            if start[s] < end[e]:
                s += 1
                room_used += 1
            else:
                e += 1
                room_used -= 1
            count = max(room_used, count)
        return count

    