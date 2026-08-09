from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        warmer = [0] * len(temperatures)
        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                i, _ = stack.pop()
                warmer[i] = index - i
            
            stack.append((index, temperature))
        
        return warmer