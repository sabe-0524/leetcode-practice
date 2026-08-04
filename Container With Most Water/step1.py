from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most = 0
        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            most = max(most, (right - left) * min(left_height, right_height))
            if left_height > right_height:
                right -= 1
            else:
                left += 1
        
        return most