from dataclasses import dataclass
from bisect import bisect_right
from collections import defaultdict

@dataclass
class ValueWithTime:
    value: str
    timestamp: int

class TimeMap:

    def __init__(self):
        self.t_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.t_map[key].append(ValueWithTime(value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.t_map[key]
        if not pairs:
            return ""
        
        index = bisect_right(pairs, timestamp, key=lambda x: x.timestamp)
        
        if index == 0:
            return ""

        return pairs[index - 1].value
        
