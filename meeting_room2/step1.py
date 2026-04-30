from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        used_count = {}
        for interval in intervals:
            used_count[interval.start] = used_count.get(interval.start, 0) + 1
            used_count[interval.end] = used_count.get(interval.end, 0) - 1
        current = 0
        max_room = 0
        for key in sorted(used_count):
            current += used_count[key]
            max_room = max(max_room, current)
        return max_room