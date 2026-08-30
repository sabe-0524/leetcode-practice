from dataclasses import dataclass
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
        
        left = 0
        right = len(pairs)
        while left < right:
            middle = (left + right) // 2
            if pairs[middle].timestamp <= timestamp:
                left = middle + 1
            else:
                right = middle
        
        index = left
        
        if index == 0:
            return ""

        return pairs[index - 1].value
        
