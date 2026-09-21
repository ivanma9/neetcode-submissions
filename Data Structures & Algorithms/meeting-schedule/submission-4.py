"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: return True
        intervals.sort(key=lambda x: x.start)
        curMeeting = intervals[0]
        for upcomingMeeting in intervals[1:]:
            if curMeeting.end > upcomingMeeting.start:
                return False
            else:
                curMeeting = upcomingMeeting
        return True