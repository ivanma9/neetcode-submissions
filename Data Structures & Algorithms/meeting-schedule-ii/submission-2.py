"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x.start)
        rooms = [intervals[0].end] # sorted heap of all overlapping intervals this will just be end time
        heapq.heapify(rooms)
        for interval in intervals[1:]:
            # if the start time is less than the first rooms,
            # we must need another room
            if interval.start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
        return len(rooms)





