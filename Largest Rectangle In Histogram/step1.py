from typing import List
from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        max_area = 0
        for i, height in enumerate(heights):
            if not stack or heights[stack[-1]] <= height:
                stack.append(i)
                continue
              
            poped_bars = deque()
            while stack and heights[stack[-1]] > height:
                poped_bars.appendleft(heights[stack.pop()])
            
            stack.append(i)
            
            len_bars = len(poped_bars)
            for j, bar in enumerate(poped_bars):
                max_area = max(max_area, (len_bars - j) * bar)
        
        len_stack = len(stack)
        for i, bar in enumerate(stack):
            max_area = max(max_area, (len_stack - i) * heights[bar])
        
        return max_area
            
            