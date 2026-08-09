from typing import List
from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = len(position)
        data = [(p, s) for p, s in zip(position, speed)]
        data.sort(key=lambda x:x[0])
        
        stack = deque()
        
        for p, s in data:
            reach_time = (target - p) / s
            while stack and stack[-1] <= reach_time:
                fleet -= 1
                stack.pop()
            
            stack.append(reach_time)
        
        return fleet