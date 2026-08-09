from typing import List
from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = sorted(zip(position, speed), reverse=True)
        
        stack = []
        
        for p, s in data:
            reach_time = (target - p) / s
            
            if not stack or stack[-1] < reach_time:
                stack.append(reach_time)
        
        return len(stack)