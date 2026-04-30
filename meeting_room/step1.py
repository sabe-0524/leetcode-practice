from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        used_count = {}
        for interval in intervals:
            used_count[interval.start] = used_count.get(interval.start, 0) + 1
            used_count[interval.end] = used_count.get(interval.end, 0) - 1
        current = 0
        for key in sorted(used_count):
            current += used_count[key]
            if current > 1:
                return False
        
        return True