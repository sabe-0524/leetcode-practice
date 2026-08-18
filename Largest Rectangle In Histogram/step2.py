from typing import List
from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        max_area = 0
        
        for i, current_height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > current_height:
                h = heights[stack.pop()]
                
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                max_area = max(max_area, h * width)
                
            stack.append(i)
        
        return max_area