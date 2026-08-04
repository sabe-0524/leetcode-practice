from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water_area = 0
        max_left = height[left]
        max_right = height[right]
        while left < right:
            height_left = height[left]
            height_right = height[right]
            if height_left < height_right:
                water_area += max(max_left - height_left, 0)
                max_left = max(max_left, height_left)
                left += 1
            else:
                water_area += max(max_right - height_right, 0)
                max_right = max(max_right, height_right)
                right -= 1
        
        return water_area