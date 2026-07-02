"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        print([(v.start, v.end) for v in intervals])
        for i in range(1, len(intervals)):
            print(intervals[i - 1].end, intervals[i].start)
            #print(i, v)
            if intervals[i - 1].end > intervals[i].start:
                return False

        return True