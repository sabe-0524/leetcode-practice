from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = max(height)
        max_area = 0
        for i in range(max_height):
            prev = -1
            for j in range(len(height)):
                current = height[j] - i
                if current > 0:
                    if prev != -1:
                        max_area += (j - prev - 1)
                    prev = j
        
        return max_area