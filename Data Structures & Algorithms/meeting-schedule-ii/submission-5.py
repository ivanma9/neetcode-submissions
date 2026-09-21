"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # [(0,40),(5,10),(15,20)]
        intervals.sort(key=lambda x:x.start)

        rooms = [] # store end
        heapq.heapify(rooms)
        ct = 0

        for interval in intervals:
            st,ed = interval.start, interval.end
            if rooms and st >= rooms[0]:
                # replace room
                heapq.heappop(rooms)
                heapq.heappush(rooms, ed)
            else:
                #need another room
                heapq.heappush(rooms,ed)

            ct = max(ct, len(rooms))
        return ct